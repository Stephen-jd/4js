import os
import re

urls_path = "c:/Users/steph/Downloads/theos/website/urls.py"
with open(urls_path, 'r', encoding='utf-8') as f:
    content = f.read()

if 'path(\'syllabus_explorer/' not in content:
    content = content.replace(']', "    path('syllabus_explorer/', views.syllabus_explorer, name='syllabus_explorer'),\n]")
    with open(urls_path, 'w', encoding='utf-8') as f:
        f.write(content)
