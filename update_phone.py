import os

files_to_update = [
    "generate_kb.py",
    "static/js/chatbot.js",
    "static/js/taylorfit.js",
    "website/knowledge_base.json",
    "website/templates/website/base.html",
    "website/templates/website/home.html",
    "website/templates/website/index.html",
    "website/views.py"
]

for f_path in files_to_update:
    if os.path.exists(f_path):
        with open(f_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace formatted and unformatted versions
        content = content.replace("7854 885030", "7534 715058")
        content = content.replace("7854885030", "7534715058")
        
        with open(f_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Phone numbers updated.")
