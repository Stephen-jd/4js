import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fourjs.settings')
django.setup()

from website.models import SyllabusSubject, SyllabusModule, PastPaper

def populate():
    SyllabusSubject.objects.all().delete()
    
    maths = SyllabusSubject.objects.create(name='Mathematics', level='GCSE', description='Complete AQA and Edexcel Mathematics Syllabus.')
    SyllabusModule.objects.create(subject=maths, title='Number', topics='Structure and calculation, Fractions, decimals, percentages, Measures and accuracy, Surds and Standard Form')
    SyllabusModule.objects.create(subject=maths, title='Algebra', topics='Algebraic notation, Solving equations & inequalities, Sequences, Graphs of quadratics & cubics')
    SyllabusModule.objects.create(subject=maths, title='Geometry', topics='Properties and constructions, Mensuration, Vectors, Trigonometry')
    
    science = SyllabusSubject.objects.create(name='Combined Science', level='GCSE', description='Complete AQA and Edexcel Combined Science Syllabus.')
    SyllabusModule.objects.create(subject=science, title='Biology', topics='Cell biology, Infection and response, Bioenergetics, Homeostasis, Ecology')
    SyllabusModule.objects.create(subject=science, title='Chemistry', topics='Atomic structure, Quantitative chemistry, Organic chemistry, Atmosphere')
    SyllabusModule.objects.create(subject=science, title='Physics', topics='Energy, Electricity, Particle model, Forces, Waves, Magnetism')

    for year in range(2018, 2024):
        for board in ['AQA', 'Edexcel']:
            PastPaper.objects.create(subject=maths, board=board, year=year, paper_name='Paper 1 (Non-Calculator)', link=f'https://example.com/maths/{board}/{year}/p1.pdf')
            PastPaper.objects.create(subject=maths, board=board, year=year, paper_name='Paper 2 (Calculator)', link=f'https://example.com/maths/{board}/{year}/p2.pdf')
            PastPaper.objects.create(subject=maths, board=board, year=year, paper_name='Paper 3 (Calculator)', link=f'https://example.com/maths/{board}/{year}/p3.pdf')
            
            PastPaper.objects.create(subject=science, board=board, year=year, paper_name='Biology Paper 1', link=f'https://example.com/science/{board}/{year}/b1.pdf')
            PastPaper.objects.create(subject=science, board=board, year=year, paper_name='Chemistry Paper 1', link=f'https://example.com/science/{board}/{year}/c1.pdf')
            PastPaper.objects.create(subject=science, board=board, year=year, paper_name='Physics Paper 1', link=f'https://example.com/science/{board}/{year}/p1.pdf')

    print("Successfully populated database with massive AI dataset!")

if __name__ == '__main__':
    populate()
