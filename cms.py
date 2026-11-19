import hashlib
import hmac
import html
import json
import os
import re
import secrets
import time
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Lock
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
DIST = ROOT
DATA = ROOT / 'content'
ORIGIN = 'http://127.0.0.1:8753'
PAGES = {name: DIST / (name + '.html') for name in ('index','about','services','causes','team','media','contact','donate')}
DATA.mkdir(mode=0o700, exist_ok=True)
keyfile = DATA / 'admin-password.txt'
if not keyfile.exists():
    with os.fdopen(os.open(keyfile, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600), 'w') as f:
        f.write(secrets.token_urlsafe(18) + '\n')
password = keyfile.read_text().strip()
statefile = DATA / 'edits.json'
lock = Lock()
sessions = {}
last_failure = 0

# The tokenization operates only on our generated templates. Edits are escaped
# as text or validated URL attributes before insertion.
PARTS = re.compile(r'<[^>]+>|[^<]+')
ATTR = re.compile(r'\b(href|src|alt)="([^"]*)"')
SHARED = re.compile(r'(<header>.*?</header>)|(<footer>.*?</footer>)|(<main id="main">.*?</main>)', re.S)

def transform(template, page, edits):
    fields = {}
    def region(match):
        group = 'header' if match[1] else 'footer' if match[2] else page
        counter = 0
        def field(value, kind):
            nonlocal counter
            key = f'{group}:{counter}'
            counter += 1
            fields[key] = {'id':key, 'kind':kind, 'value':edits.get(key, html.unescape(value))}
            return html.escape(edits[key], quote=True) if key in edits else value
        def token(m):
            part = m[0]
            if part.startswith(('<img ', '<a ')):
                def attr(a):
                    kind, value = a.groups()
                    return f'{kind}="{field(value, kind)}"'
                return ATTR.sub(attr, part)
            if not part.startswith('<') and part.strip():
                return field(part, 'text')
            return part
        return PARTS.sub(token, match[0])
    rendered = SHARED.sub(region, template)
    return rendered, fields

def load():
    return json.loads(statefile.read_text()) if statefile.exists() else {}

def validate_url(value, kind):
    if not value or value.startswith('//') or any(c.isspace() or c=='\\' for c in value):
        return False
    try:
        u = urlsplit(value)
    except ValueError:
        return False
    if u.scheme == 'https':
        return bool(u.hostname and not u.username and not u.password)
    if kind=='href' and u.scheme in {'mailto','tel'}:
        return bool(u.path and not u.netloc)
    return not u.scheme and not u.netloc and (not u.path or u.path in {p.name for p in DIST.iterdir()})

class Handler(BaseHTTPRequestHandler):
    def send(self, status, body, mime, cookie=None):
        if isinstance(body, str):
            body = body.encode()
        self.send_response(status)
        self.send_header('Content-Type', mime)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Cache-Control', 'no-store')
        self.send_header('Content-Security-Policy', "default-src 'none'; img-src 'self' https:; style-src 'self'; script-src 'self'; connect-src 'self'; form-action 'self'; frame-ancestors 'none'; base-uri 'none'")
        if cookie:
            self.send_header('Set-Cookie', cookie)
        self.end_headers()
        self.wfile.write(body)

    def api(self, status, obj, cookie=None):
        self.send(status,json.dumps(obj), 'application/json',cookie)

    def identity(self):
        cookies = SimpleCookie(self.headers.get('Cookie',''))
        session = cookies.get('cpf_admin')
        with lock:
            return bool(session and sessions.get(session.value,0) > time.monotonic())

    def allowed_host(self):
        return self.headers.get('Host') == '127.0.0.1:8753'

    def do_GET(self):
        if not self.allowed_host():
            return self.api(403,{'error':'Invalid host'})
        url = urlsplit(self.path)
        path = url.path
        if path == '/api/content':
            if not self.identity():
                return self.api(401,{'error':'Sign in first'})
            page = url.query.removeprefix('page=')
            if page not in PAGES:
                return self.api(400,{'error':'Unknown page'})
            return self.api(200,list(transform(PAGES[page].read_text(),page,load())[1].values()))
        if path in {'/admin','/admin.js'}:
            name = 'admin.html' if path=='/admin' else 'admin.js'
            return self.send(200,(ROOT/name).read_bytes(),'text/html; charset=utf-8' if name.endswith('html') else 'text/javascript')
        page = 'index' if path=='/' else path[1:].removesuffix('.html')
        if page in PAGES:
            result = transform(PAGES[page].read_text(),page,load())[0]
            if page=='index':
                result=result.replace('<body>','<body class="home">',1)
            return self.send(200,result,'text/html; charset=utf-8')
        assets={'style.css':'text/css','logo.png':'image/png','story.png':'image/png','dance-fit.jpg':'image/jpeg', 'outreach-kelaniya.jpg':'image/jpeg', 'outreach-online-safety.jpg':'image/jpeg', 'outreach-kotte.jpg':'image/jpeg'}
        name=path[1:]
        if name in assets:
            return self.send(200,(DIST/name).read_bytes(),assets[name])
        return self.api(404,{'error':'Not found'})

    def do_POST(self):
        global last_failure
        if not self.allowed_host() or self.headers.get('Origin') != ORIGIN:
            return self.api(403,{'error':'Invalid request origin'})
        try:
            size = int(self.headers.get('Content-Length','0'))
            if self.headers.get_content_type()!='application/json' or not 0<size<=250000:
                raise ValueError()
            req=json.loads(self.rfile.read(size))
            if not isinstance(req,dict):
                raise ValueError()
        except (ValueError,UnicodeError):
            return self.api(400,{'error':'Invalid request'})
        if self.path == '/api/login':
            supplied = req.get('password')
            now=time.monotonic()
            with lock:
                if now-last_failure < 1.5:
                    return self.api(429,{'error':'Wait a moment before trying again'})
                if not isinstance(supplied,str) or not hmac.compare_digest(hashlib.sha256(supplied.encode()).digest(),hashlib.sha256(password.encode()).digest()):
                    last_failure=now
                    return self.api(401,{'error':'Incorrect password'})
                token=secrets.token_urlsafe(32)
                sessions[token]=now+4*3600
            return self.api(200,{'ok':True},f'cpf_admin={token}; HttpOnly; SameSite=Strict; Path=/; Max-Age=14400')
        if not self.identity():
            return self.api(401,{'error':'Sign in first'})
        if self.path != '/api/content':
            return self.api(404,{'error':'Not found'})
        page=req.get('page')
        changes=req.get('changes')
        if not isinstance(page,str) or page not in PAGES or not isinstance(changes,dict):
            return self.api(400,{'error':'Invalid page or changes'})
        with lock:
            edits=load()
            fields=transform(PAGES[page].read_text(),page,edits)[1]
            for key,value in changes.items():
                if key not in fields or not isinstance(value,str) or len(value)>4000:
                    return self.api(400,{'error':'Invalid content field'})
                kind=fields[key]['kind']
                if kind in {'href','src'} and not validate_url(value,kind):
                    return self.api(400,{'error':'Use an HTTPS link, an existing site file or a valid contact link'})
            edits.update(changes)
            tmp=statefile.with_suffix('.tmp')
            tmp.write_text(json.dumps(edits,ensure_ascii=False))
            tmp.replace(statefile)
        return self.api(200,{'ok':True})

if __name__ == '__main__':
    ThreadingHTTPServer(('127.0.0.1',8753),Handler).serve_forever()
