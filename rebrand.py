import os

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple replacement, avoiding breaking anything major
    new_content = content.replace("4JS", "4JS")
    new_content = new_content.replace("4js", "4js")
    
    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk('c:\\Users\\steph\\Downloads\\theos'):
    if '.git' in root or '__pycache__' in root or 'staticfiles' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.py', '.js', '.json', '.css', '.md')):
            replace_in_file(os.path.join(root, file))
