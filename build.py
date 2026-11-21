from pathlib import Path
from html import escape
from urllib.parse import quote_plus
P=Path(__file__).resolve().parent
BASE='https://www.childprotectionforce.org/'
nav=[('About','about'),('Services','services'),('Our causes','causes'),('Team','team'),('Media','media'),('Contact','contact'),('Volunteer','volunteer'),('Donate','donate')]
def a(label, path, cls=''):
 return f'<a class="{cls}" href="{path}">{escape(label)}</a>'
def cards(rows):
 return '<div class="grid">'+''.join(f'<article><h3>{escape(title)}</h3><p>{escape(body)}</p></article>' for title,body in rows)+'</div>'
def section(title,content):
 return f'<section class="wrap"><h2>{title}</h2>{content}</section>'
def sub(title,intro,body):
 return f'<section class="inner"><div class="wrap"><h1>{title}</h1><p>{intro}</p></div></section>'+body
services=[('Legal aid','Support navigating the justice system, from the initial complaint through trial and follow-up.'),('Safe shelter','Emergency accommodation for survivors in need of a safe place.'),('Psychosocial support','Trauma-informed psychological assistance to support recovery.'),('Socioeconomic assistance','Practical support to help survivors rebuild stability and reintegrate.')]
causes=[('Safe House Meththa','Support daily meals, schooling and other essentials.'),('Shelter operations','Help sustain safe accommodation for survivors.'),('Legal casework','Support representation and guidance through the justice process.'),('Therapy and reintegration','Help survivors access care and rebuild their lives.')]
volunteer=[('Volunteer your skills','Contribute legal, translation, therapy, media, fundraising or administrative skills.'),('Host a fundraiser','Organize a community fundraiser or awareness campaign.'),('Workplace partnerships','Explore workplace giving and corporate social responsibility partnerships.')]
team=[('Milani Salpitikorala','Founder and attorney-at-law. Leads legal advocacy, strategy and multi-agency collaboration.'),('Hans Billimoria','Board member. Contributes advocacy, strategic communications and governance experience.'),('Amber Habib Vitarana','Board member and founder of Mums in Colombo. Supports outreach and partnerships.'),('Mihiri Salpitikorala','Founding member. Supports the organization’s work to protect children and women.')]
links=[('Research on institutionalized children in Sri Lanka','Research'),('Supporting children to navigate the legal quagmire','Daily Mirror'),('Urgent need to regulate media','Daily FT'),('Child protection crisis larger than economic crisis','Daily FT'),('Has Children’s Day lost its purpose?','The Morning'),('More Boys Are Sexually Abused Than Girls','Roar Media'),('The Importance of Psychological Support','Roar Media'),('The People’s Platform','Video'),('Episode 12 with Milani Salpitikorala','Video'),('NewslineSL','Video'),('Date with Danu','Video'),('Outstanding Role Models of Sri Lanka','Video')]
contact='<address>No. 713, D P Wijesinghe Mawatha<br>Pelawatte, Battaramulla, Sri Lanka</address><p>'+a('+94 77 738 8212','tel:+94777388212')+'<br>'+a('+94 11 279 5738','tel:+94112795738')+'<br>'+a('+94 77 309 4366','tel:+94773094366')+'</p><p>'+a('kanchana@childprotectionforce.org','mailto:kanchana@childprotectionforce.org')+'<br>'+a('milani@childprotectionforce.org','mailto:milani@childprotectionforce.org')+'</p>'
office_map_query=quote_plus('Child Protection Force, 713 D P Wijesinghe Mawatha, Pelawatte, Battaramulla, Sri Lanka')
office_map=(
 f'<iframe title="Google Map of the Child Protection Force office" '
 f'src="https://www.google.com/maps?q={office_map_query}&amp;z=17&amp;output=embed" '
 'width="100%" height="380" loading="lazy"></iframe>'
 f'<p><a class="btn" href="https://www.google.com/maps/dir/?api=1&amp;destination={office_map_query}">Get directions in Google Maps</a></p>'
)

home='''<section class="hero"><div class="wrap split"><div><p class="eyebrow">CHILD PROTECTION IN SRI LANKA</p><h1>Safety, care and access to justice</h1><p>Child Protection Force supports children and women who have survived crime through legal aid, emergency shelter and trauma-informed care.</p><div class="actions"><a class="btn" href="services.html">Find support</a><a class="outline btn" href="donate.html">Support the work</a></div></div><div class="hero-visual">
  <div class="photo"><img src="story.png" alt="Artwork of four children beneath a rainbow"></div>
  <div class="hero-logo" aria-hidden="true"><img src="logo.png" alt="" width="1658" height="1658"></div>
</div></div></section>
<div class="impact"><div class="wrap stats"><div><strong>200+</strong><span>Legal representations annually</span></div><div><strong>800+</strong><span>State officers trained since 2018</span></div><div><strong>2017</strong><span>Child Protection Force founded</span></div></div></div>'''
home+=section('How we help',cards(services)+a('Explore our services','services.html','textlink'))+section('Ways to get involved',cards(volunteer)+a('Explore volunteering','volunteer.html','textlink'))
update='<div class="split campaign"><img src="dance-fit.jpg" alt="Dance Fit Throwback 2026 event poster"><div><h3>Dance Fit Throwback 2026</h3><p>Dance fitness with Candice and Mihiri and music by DJ Niranjan, in aid of Child Protection Force.</p><p>21 November 2026 · 5–9 p.m.<br>Earl’s Court, Cinnamon Lakeside</p><p>No dance experience needed. Join at your own pace. Minimum contribution LKR 2,500, with all proceeds going to Child Protection Force.</p>'+a('Watch the Instagram reel','https://www.instagram.com/reel/Df4IBm3N2e2/','btn')+'</div></div>'
social='<div class="grid social-updates"><article><h3>Dance Fit Throwback on Instagram</h3><p>See the event announcement and the latest video from Child Protection Force.</p><p>'+a('View the event post','https://www.instagram.com/childprotectionforce.sl/p/DfPPYa2ChC4/')+' · '+a('Watch on Instagram','https://www.instagram.com/childprotectionforce.sl/reel/Df6ZkkwuRyt/')+'</p></article><article><h3>Dance Fit Throwback on Facebook</h3><p>Preview the fundraiser and see the organization’s thank-you to its radio partner.</p><p>'+a('Watch on Facebook','https://www.facebook.com/reel/2627436527731402/')+' · '+a('See the partner post','https://www.facebook.com/childprotectionforce/posts/pfbid02Yz9ixVXJXkrsokNAjhi9YRcGctmT43MQ8tJg6w4APYhj5r4PcxYiLKWvQDM7miKol')+'</p></article></div>'
home+=section('Community updates',update+social).replace('<section class="wrap">','<section class="wrap" id="community-updates">',1)
donation_confirmation=(
 '<div class="contact-message" id="confirm-donation"><h2>Confirm a bank transfer</h2>'
 '<p>After making your transfer, fill in these details to open an email draft for Kanchana.</p>'
 '<form id="donation-form" action="mailto:kanchana@childprotectionforce.org">'
 '<div class="contact-fields">'
 '<label>Full name<input name="Full name" autocomplete="name" required maxlength="100"></label>'
 '<label>Email address<input name="Email address" type="email" autocomplete="email" required maxlength="254"></label>'
 '<label>Amount (LKR)<input name="Amount (LKR)" type="number" min="0.01" step="0.01" required></label>'
 '<label>Transfer date<input name="Transfer date" type="date" required></label>'
 '</div>'
 '<label>Transfer reference (optional)<input name="Transfer reference" maxlength="100"></label>'
 '<button class="btn" type="submit">Open confirmation email</button>'
 '</form></div><script src="donation.js" defer></script>'
)
volunteer_form = """
<div class="volunteer-application">
  <aside>
    <h3>Tell us how you can help</h3>
    <p>Share your interests and availability so the team can discuss where your skills might fit.</p>
    <p>Please leave out case details and other sensitive information.</p>
  </aside>
  <form id="contact-form" class="volunteer-form" action="mailto:kanchana@childprotectionforce.org"
        data-subject="Child Protection Force volunteer enquiry">
    <div class="volunteer-fields">
      <label>Full name <input name="name" autocomplete="name" required maxlength="120"></label>
      <label>Email address <input name="email" type="email" autocomplete="email" required maxlength="254"></label>
      <label>Area of interest
        <select name="interest" required>
          <option value="">Choose an area</option>
          <option>Legal and translation support</option>
          <option>Psychosocial support</option>
          <option>Media and communications</option>
          <option>Fundraising and events</option>
          <option>Administration</option>
          <option>Other or open to suggestions</option>
        </select>
      </label>
      <label>Mobile or WhatsApp number (optional)
        <input name="phone" type="tel" autocomplete="tel" maxlength="32">
      </label>
      <label>Availability (optional)
        <input name="availability" placeholder="e.g. weekdays, 9 a.m. to 3 p.m." maxlength="160">
      </label>
    </div>
    <label>Relevant skills or experience (optional)
      <textarea name="message" rows="4" maxlength="1500"></textarea>
    </label>
    <button class="btn" type="submit">Prepare volunteer enquiry</button>
    <small>Your email app opens with a draft for our team. Review it and press Send.</small>
  </form>
</div>
<script src="contact.js" defer></script>
"""
pages={
'volunteer': ('Volunteer', sub('Volunteer with Child Protection Force',
 'Share your time and skills to support children and families in Sri Lanka.',
 section('Ways to help', cards(volunteer)) + section('Tell us about yourself', volunteer_form))),
'index':('Home',home),
'about':('About',sub('About Child Protection Force','A Sri Lankan nonprofit founded in 2017 by attorney-at-law Milani Salpitikorala.',section('Our story','<p>We work with law enforcement, child protection officers, educators and communities to help survivors access immediate care and long-term justice.</p>'+cards([('Mission','Protect and empower survivors through trauma-informed care, justice and reintegration.'),('Vision','A Sri Lanka where every child is safe, survivors are heard and justice is swift and compassionate.'),('Values','The best interests of children, education, survivor-centered practice, collaboration and accountability. The organization draws on the UN Convention on the Rights of the Child and Northern Ireland Principles.')])+a('Meet our team','team.html','textlink')))),
'services':('Services',sub('Our services','Support for children and women who have survived crime.',section('Care and representation',cards(services)+a('Contact Child Protection Force','contact.html','btn')))),
'causes':('Our causes',sub('Our causes','Help fund the care, representation and practical support survivors need.',section('What you can support',cards(causes)+a('See giving options','donate.html','btn')))),
'team':('Team',sub('Our team','Meet the board and founding members.',section('Board and founding members',cards(team)))),
'media':('Media',sub('Media and publications','Research, news coverage and interviews on child protection in Sri Lanka.',section('Publications and features',update+social+cards(links)))),
'contact':('Contact',
 '<div class="wrap contact-page">'
 '<h1>Contact us</h1>'
 '<div class="contact-layout">'
 '<section class="contact-map"><h2>Find us</h2>'+office_map+'</section>'
 '<section class="contact-office"><h2>Office</h2>'+contact+'</section>'
 '</div>'
 '<section class="contact-message"><h2>Contact form</h2>'
 '<p>For general enquiries, fill in your details and open the draft in your email app.</p>'
 '<form id="contact-form" action="mailto:kanchana@childprotectionforce.org">'
 '<div class="contact-fields">'
 '<label>Full name<input name="name" autocomplete="name" required maxlength="100"></label>'
 '<label>Email address<input name="email" type="email" autocomplete="email" required maxlength="254"></label>'
 '</div>'
 '<label>Message<textarea name="message" rows="5" required maxlength="1500"></textarea></label>'
 '<button class="btn" type="submit">Open email draft</button>'
 '</form></section>'
 '</div><script src="contact.js" defer></script>'),
'donate':('Donate',sub('Support Child Protection Force','Give, volunteer or organize a fundraiser.',section('Make a donation','<h3>Bank transfer</h3><dl class="donation-details"><dt>Account name</dt><dd>Child Protection Force</dd><dt>Bank</dt><dd>Nations Trust Bank PLC, Battaramulla branch</dd><dt>Account number</dt><dd>1001 5000 3460</dd><dt>SWIFT code</dt><dd>NTBCLKLX</dd></dl>'+donation_confirmation)+section('What your gift can support',cards(causes))+section('Give supplies or volunteer','<p>In-kind donations can include dry rations, fresh produce, toiletries, baby formula, diapers, clothing and educational materials.</p><p>'+a('Email Safe House Meththa','mailto:meththa@childprotectionforce.org')+' · '+a('Call Kanchana','tel:+94773094366')+'</p>'+cards(volunteer)+'<p>'+a('Tell us how you’d like to volunteer','volunteer.html')+'</p>')))}
programme_posts=[
 ('Kelaniya school principals','Highlights from a child protection awareness programme for school principals in the Kelaniya Zone.','DfUY958tVQG'),
 ('Child protection and online safety','An awareness session for parents of Montessori children during World Children’s Month.','DejQbzHjuVe'),
 ('School principals in Kotte','A full-day child protection awareness session for principals in the Sri Jayawardenepura Kotte education zone.','DdobMnjCXFy')]
programme_covers={'DfUY958tVQG':'outreach-kelaniya.jpg','DejQbzHjuVe':'outreach-online-safety.jpg','DdobMnjCXFy':'outreach-kotte.jpg'}
programme_updates=section('Training and community outreach','<div class="grid outreach">'+''.join(f'<article><div class="outreach-photo"><img loading="lazy" src="{programme_covers[post]}" alt=""></div><h3>{escape(title)}</h3><p>{escape(description)}</p><p>{a("Watch the programme highlights","https://www.instagram.com/childprotectionforce.sl/reel/"+post+"/")}</p></article>' for title,description,post in programme_posts)+'</div>')
for key in ('index','services','media'):
 title,body=pages[key]
 pages[key]=(title,body+programme_updates.replace('<section class="wrap">','<section class="wrap" id="outreach">',1))
search_metadata = {
 'index': ('Child Protection Force Sri Lanka | Legal Aid and Safe Shelter', 'Child Protection Force supports children and women in Sri Lanka through legal aid, emergency shelter, and trauma-informed care.'),
 'about': ('About Child Protection Force Sri Lanka', 'Learn how Child Protection Force works to improve safety, care, and access to justice for children and women in Sri Lanka.'),
 'services': ('Child Protection Services in Sri Lanka | Child Protection Force', 'Explore legal aid, emergency shelter, psychosocial care, and practical reintegration support offered by Child Protection Force.'),
 'causes': ('Causes We Support | Child Protection Force Sri Lanka', 'Learn how to support Safe House Meththa, shelter operations, legal casework, and therapy and reintegration in Sri Lanka.'),
 'team': ('Our Team | Child Protection Force Sri Lanka', 'Meet the board and founding members of Child Protection Force and learn about the team behind its work in Sri Lanka.'),
 'media': ('Media and Publications | Child Protection Force Sri Lanka', 'Explore news, publications, campaign updates, and child protection training and outreach from Child Protection Force.'),
 'contact': ('Contact Child Protection Force | Battaramulla, Sri Lanka', 'Contact Child Protection Force in Battaramulla. Find office directions, telephone numbers, email addresses, and an enquiry form.'),
 'volunteer': ('Volunteer | Child Protection Force Sri Lanka', 'Find ways to volunteer with Child Protection Force and tell the team how you would like to help.'),
 'donate': ('Donate to Child Protection Force Sri Lanka', 'Support child protection in Sri Lanka. Find bank transfer details, confirm a donation, give supplies, or volunteer with Child Protection Force.'),
}
def canonical_url(key):
 return BASE if key == 'index' else BASE + key + '.html'

for key,(title,body) in pages.items():
 menu=''.join(a(label,url+'.html','btn' if url=='donate' else '') for label,url in nav)
 footer_menu=''.join(a(label,url+'.html') for label,url in nav if url!='donate')
 search_title, search_description = search_metadata[key]
 canonical = canonical_url(key)
 stylesheet = "style.css?v=11" if key == "index" else "style.css?v=10"
 (P/(key+'.html')).write_text(f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(search_title)}</title><meta name="description" content="{escape(search_description)}"><link rel="canonical" href="{canonical}"><link rel="icon" type="image/png" sizes="48x48" href="/favicon.png"><link rel="stylesheet" href="{stylesheet}"><script src="/analytics.js" defer></script><body><a class="skip" href="#main">Skip to content</a><header><div class="wrap top"><a class="brand" href="index.html"><img src="logo.png" alt=""><span>Child Protection<br>Force</span></a><nav aria-label="Main navigation">{menu}</nav></div></header><main id="main">{body}</main><footer class="site-footer" id="site-footer">
<div class="wrap footer-main">
  <div class="footer-brand">
    <a href="index.html" class="footer-wordmark"><img src="logo.png" alt="" width="56" height="56"><span>Child Protection<br>Force</span></a>
    <p>Legal aid, safe shelter and trauma-informed care in Sri Lanka.</p>
    <p class="social-links"><a class="social-instagram" href="https://www.instagram.com/childprotectionforce.sl/"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2.5" y="2.5" width="19" height="19" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>Instagram</a> <a class="social-facebook" href="https://www.facebook.com/childprotectionforce/"><svg aria-hidden="true" viewBox="0 0 24 24"><path fill="currentColor" d="M14 22v-9h3l.45-3.5H14V7.3c0-1 .26-1.65 1.72-1.65h1.83V2.5a24 24 0 0 0-2.67-.14c-2.64 0-4.45 1.61-4.45 4.58V9.5H7.45V13h2.98v9z"/></svg>Facebook</a></p>
  </div>
  <div class="footer-explore">
    <h2>Explore</h2>
    <nav aria-label="Footer navigation">{footer_menu}</nav>
  </div>
  <div class="footer-contact">
    <h2>Contact us</h2>
    {contact}
  </div>
</div>
<div class="wrap footer-bottom">
  <small>© Child Protection Force</small>
  <button type="button" id="analytics-preference" hidden>Analytics preferences</button>
  <a class="btn" href="donate.html">Support our work</a>
</div>
</footer></body></html>''')

(P/'sitemap.xml').write_text(
 '<?xml version="1.0" encoding="UTF-8"?>\n'
 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
 + ''.join(f'  <url><loc>{canonical_url(key)}</loc></url>\n' for key in pages)
 + '</urlset>\n', encoding='utf-8')
(P/'robots.txt').write_text(f'User-agent: *\nDisallow: /admin.html\nSitemap: {BASE}sitemap.xml\n', encoding='utf-8')
