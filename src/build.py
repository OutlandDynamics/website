"""Builds the Outland Dynamics static site into ../website from templates here.
Usage: python3 build.py <privacy-policy.md> <out-dir>
"""
import re, sys, pathlib, markdown

src_md, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
SUPPORT = "support@outlanddynamics.com"

def page(title, desc, current, body, theme="odin"):
    def link(href, label):
        cur = ' aria-current="page"' if href == current else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@300;500;600&display=swap">
<link rel="stylesheet" href="style.css">
</head>
<body class="theme-{theme}">
<header class="site-header"><div class="wrap">
  <a class="brand" href="index.html">OUTLAND DYNAMICS</a>
  <nav aria-label="Main">{link("index.html", "Home")}{link("odin.html", "ODIN")}{link("install.html", "Install")}{link("support.html", "Support")}{link("privacy.html", "Privacy")}</nav>
</div></header>
<main>
{body}
</main>
<footer class="site-footer"><div class="wrap">
  <span>© 2026 Outland Dynamics LLC · Fort Collins, Colorado</span>
  <nav aria-label="Footer">{link("support.html", "Support")}{link("privacy.html", "Privacy policy")}</nav>
</div></footer>
</body>
</html>
"""

home = (pathlib.Path(__file__).parent / "home.html").read_text()
company = (pathlib.Path(__file__).parent / "company.html").read_text()
install = (pathlib.Path(__file__).parent / "install.html").read_text()
support = (pathlib.Path(__file__).parent / "support.html").read_text().replace("{SUPPORT}", SUPPORT)

# Privacy policy from the repo's draft: drop the draft blockquote, fill the contact,
# and turn UNSURE markers into visible highlights for the owner's review.
md = src_md.read_text()
md = re.sub(r"^# .*\n", "", md, count=1)
md = re.sub(r"^> \*\*Draft.*?\n(> .*\n)*", "", md, flags=re.M)
md = md.replace("Contact: UNSURE (the owner to add a support email address or web page).",
                f"Contact: [{SUPPORT}](mailto:{SUPPORT}) or [our support page](support.html).")
md = md.replace("Questions about this policy: UNSURE (contact address to be added by the owner).",
                f"Questions about this policy: [{SUPPORT}](mailto:{SUPPORT}).")
html = markdown.markdown(md, extensions=["tables"])
html = html.replace("<table>", '<div class="table-scroll"><table>').replace("</table>", "</table></div>")
html = re.sub(r"<strong>UNSURE:?</strong>:?|UNSURE:?", '<span class="unsure">UNSURE</span>', html)
unsure_count = html.count('class="unsure"')
privacy = f"""<div class="page-head"><div class="wrap">
  <h1>ODIN privacy policy</h1>
  <p>How the ODIN app and server handle your information.</p>
  <div class="draft-banner">Draft for review: {unsure_count} items marked UNSURE need a decision before this page goes live.</div>
</div></div>
<div class="wrap"><article class="prose">
{html}
</article></div>"""

out.mkdir(parents=True, exist_ok=True)
(out / "index.html").write_text(page("Outland Dynamics", "Outland Dynamics is an independent technology company in Fort Collins, Colorado, making things you own outright: software today, with games and hardware to come.", "index.html", company, theme="co"))
(out / "odin.html").write_text(page("ODIN · Outland Dynamics", "ODIN is one app for the movies, TV, comics, books and music you own, played from your own server. Your world. Your network. Your rules.", "odin.html", home))
(out / "install.html").write_text(page("Install ODIN · Outland Dynamics", "How to install ODIN: join a server you were invited to, or set up your own ODIN server at home.", "install.html", install))
(out / "support.html").write_text(page("ODIN Support · Outland Dynamics", "Help and contact for ODIN, the self-hosted media app from Outland Dynamics.", "support.html", support))
(out / "privacy.html").write_text(page("ODIN Privacy Policy · Outland Dynamics", "The privacy policy for the ODIN app and server.", "privacy.html", privacy))
(out / "CNAME").write_text("outlanddynamics.com\n")
print("built; UNSURE items in privacy:", unsure_count)
