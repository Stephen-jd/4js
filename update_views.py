import os

views_code = """
from website.models import SyllabusSubject

def syllabus_explorer(request):
    subjects = SyllabusSubject.objects.prefetch_related('modules', 'past_papers').all()
    years = list(range(1, 14))
    return render(request, 'website/syllabus_explorer.html', {'subjects': subjects, 'years': years})
"""

views_path = "c:/Users/steph/Downloads/theos/website/views.py"
with open(views_path, 'a', encoding='utf-8') as f:
    f.write('\n' + views_code)
