import os
import re

html_files = [
    "c:/Users/steph/Downloads/theos/website/templates/website/gcse.html",
    "c:/Users/steph/Downloads/theos/website/templates/website/alevel.html",
    "c:/Users/steph/Downloads/theos/website/templates/website/primary.html",
    "c:/Users/steph/Downloads/theos/website/templates/website/secondary.html"
]

for path in html_files:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove the Mock Exams section which contains the huge image
        if '<!-- Mock Exam Section -->' in content:
            content = re.sub(r'<!-- Mock Exam Section -->.*?(?=\{% endblock %\})', '', content, flags=re.DOTALL)
        
        # Remove the hero image block
        content = re.sub(r'<div class="scale-in".*?<img src="https://images.unsplash\.com.*?</div>', '', content, flags=re.DOTALL)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
