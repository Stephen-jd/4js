import os
import re

replacements = {
    "website/templates/website/primary.html": [
        (r'<h3>Year 1 &amp; 2', r'<h3 id="ks1">Year 1 &amp; 2'),
        (r'<h3>Year 3, 4 &amp; 5', r'<h3 id="ks2">Year 3, 4 &amp; 5'),
        (r'<h3>Year 6 SATs', r'<h3 id="sats">Year 6 SATs')
    ],
    "website/templates/website/secondary.html": [
        (r'<h3>Key Stage 3', r'<h3 id="ks3">Key Stage 3'),
        (r'<h3>Key Stage 4', r'<h3 id="ks4">Key Stage 4')
    ],
    "website/templates/website/gcse.html": [
        (r'<h3>Mathematics</h3>', r'<h3 id="maths">Mathematics</h3>'),
        (r'<h3>English', r'<h3 id="english">English'),
        (r'<h3>Combined Science', r'<h3 id="science">Combined Science'),
        (r'<h3>Triple Science', r'<h3 id="triple">Triple Science'),
        (r'<h3>Computer Science', r'<h3 id="cs">Computer Science'),
        (r'<h3>Humanities', r'<h3 id="humanities">Humanities')
    ],
    "website/templates/website/alevel.html": [
        (r'STEM Excellence', r'<span id="maths"></span><span id="science"></span>STEM Excellence'),
        (r'Social Sciences', r'<span id="cs"></span>Social Sciences')
    ],
    "website/templates/website/entrance_exams.html": [
        (r'<h3>11\+ Grammar', r'<h3 id="11plus">11+ Grammar'),
        (r'<h3>12\+ &amp; 13\+', r'<h3 id="13plus">12+ &amp; 13+'),
        (r'<h3>UCAT &amp; BMAT', r'<h3 id="ucat">UCAT &amp; BMAT')
    ],
    "website/templates/website/home.html": [
        (r'class="taylorfit-container"', r'id="plan-builder" class="taylorfit-container"')
    ]
}

for filepath, reps in replacements.items():
    full_path = os.path.join("c:/Users/steph/Downloads/theos", filepath)
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        for old, new in reps:
            content = re.sub(old, new, content)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
            print(f"Updated {filepath}")
