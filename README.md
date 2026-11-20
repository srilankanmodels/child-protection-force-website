# Child Protection Force website redesign

Eight-page website and local content editor. Run `python3 cms.py` with Python 3.9 or later and open http://127.0.0.1:8753/. The editor is at `/admin`. First startup creates a local password in `content/admin-password.txt`; saved edits remain in `content/edits.json`.

Run `python3 build.py` to regenerate the public HTML from its templates. The CMS is intended for a local preview. The Donate page includes bank transfer and confirmation instructions. When deploying the public files, include `donations-involved/index.html` to keep the old donations address working.

Public content and imagery come from Child Protection Force’s website, its public social posts and the supplied event flyer.
