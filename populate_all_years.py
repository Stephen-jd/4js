import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fourjs.settings')
django.setup()

from website.models import SyllabusSubject, SyllabusModule, PastPaper

def populate():
    SyllabusSubject.objects.all().delete()
    
    # Generate for Years 1 through 13
    for year in range(1, 14):
        # Maths
        maths = SyllabusSubject.objects.create(name='Mathematics', level=f'Year {year}', description=f'Complete National Curriculum for Year {year} Mathematics.')
        SyllabusModule.objects.create(subject=maths, title='Number & Place Value', topics='Counting, Number bonds, Place value representation')
        SyllabusModule.objects.create(subject=maths, title='Calculations', topics='Addition, Subtraction, Multiplication, Division')
        if year >= 7:
            SyllabusModule.objects.create(subject=maths, title='Algebra & Geometry', topics='Equations, Functions, Shapes, Angles')
        
        # English
        english = SyllabusSubject.objects.create(name='English', level=f'Year {year}', description=f'Complete National Curriculum for Year {year} English.')
        SyllabusModule.objects.create(subject=english, title='Reading & Comprehension', topics='Phonics, Inference, Poetry, Non-fiction texts')
        SyllabusModule.objects.create(subject=english, title='Writing & SPaG', topics='Grammar, Punctuation, Spelling, Creative Writing')

        # Science
        science = SyllabusSubject.objects.create(name='Science', level=f'Year {year}', description=f'Complete National Curriculum for Year {year} Science.')
        SyllabusModule.objects.create(subject=science, title='Scientific Enquiry', topics='Observation, Testing, Data collection')
        SyllabusModule.objects.create(subject=science, title='Biology & Physics', topics='Plants, Animals, Light, Sound, Forces')

        # Past Papers (Only relevant for Year 2, 6, 9, 11, 13, but user requested massive DB for all years)
        # We will generate mock past papers for every year and board
        for exam_year in [2021, 2022]:
            for board in ['AQA', 'Edexcel']:
                PastPaper.objects.create(subject=maths, board=board, year=exam_year, paper_name='Maths Assessment Paper', link=f'https://example.com/maths/{year}/{board}.pdf')
                PastPaper.objects.create(subject=english, board=board, year=exam_year, paper_name='English Assessment Paper', link=f'https://example.com/english/{year}/{board}.pdf')
                PastPaper.objects.create(subject=science, board=board, year=exam_year, paper_name='Science Assessment Paper', link=f'https://example.com/science/{year}/{board}.pdf')

    print("Successfully populated Year 1-13 massive AI dataset!")

if __name__ == '__main__':
    populate()
