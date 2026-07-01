import os
import re
import django

# Fix tagline in base.html
html_path = "c:/Users/steph/Downloads/theos/website/templates/website/base.html"
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add tagline next to the logo
if "Striving for Distinction" not in html:
    html = re.sub(
        r'(<a href="\{% url \'home\' %\}" class="navbar-logo">.*?)(</a>)',
        r'\1<span style="font-size: 0.8rem; font-weight: normal; color: var(--text-light); margin-left: 8px;">Striving for Distinction</span>\2',
        html,
        flags=re.DOTALL
    )
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

# Fix PDF links in DB
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fourjs.settings')
django.setup()

from website.models import PastPaper

for paper in PastPaper.objects.all():
    query = f"{paper.board} {paper.subject.name} {paper.year} past paper".replace(" ", "+")
    paper.link = f"https://www.google.com/search?q={query}"
    paper.save()

print("Tagline added and PDF links fixed!")
