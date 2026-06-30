import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fourjs.settings')
django.setup()

from website.models import Worksheet, Question, AnswerOption

def seed_db():
    Worksheet.objects.all().delete()
    
    # Create an 11+ Maths Worksheet
    ws = Worksheet.objects.create(
        title="11+ Non-Verbal Reasoning & Maths Diagnostic",
        subject="Mathematics",
        key_stage="11+ Prep",
        description="A challenging EdPlace-style diagnostic assessment focusing on core 11+ mathematical concepts and reasoning skills."
    )
    
    # Q1
    q1 = Question.objects.create(worksheet=ws, text="If 4x + 7 = 31, what is the value of x?", order=1)
    AnswerOption.objects.create(question=q1, text="5", is_correct=False)
    AnswerOption.objects.create(question=q1, text="6", is_correct=True)
    AnswerOption.objects.create(question=q1, text="7", is_correct=False)
    AnswerOption.objects.create(question=q1, text="8", is_correct=False)
    
    # Q2
    q2 = Question.objects.create(worksheet=ws, text="A train leaves London at 08:45 and arrives in Manchester at 11:20. How long did the journey take?", order=2)
    AnswerOption.objects.create(question=q2, text="2 hours 25 minutes", is_correct=False)
    AnswerOption.objects.create(question=q2, text="2 hours 35 minutes", is_correct=True)
    AnswerOption.objects.create(question=q2, text="3 hours 15 minutes", is_correct=False)
    AnswerOption.objects.create(question=q2, text="3 hours 35 minutes", is_correct=False)
    
    # Q3
    q3 = Question.objects.create(worksheet=ws, text="Which of these fractions is the largest?", order=3)
    AnswerOption.objects.create(question=q3, text="3/4", is_correct=False)
    AnswerOption.objects.create(question=q3, text="5/8", is_correct=False)
    AnswerOption.objects.create(question=q3, text="7/10", is_correct=False)
    AnswerOption.objects.create(question=q3, text="4/5", is_correct=True)
    
    # Create KS2 English Worksheet
    ws2 = Worksheet.objects.create(
        title="KS2 SATs Grammar Mastery",
        subject="English",
        key_stage="Key Stage 2",
        description="Master complex sentences, fronted adverbials, and punctuation for the Year 6 SATs."
    )
    
    q4 = Question.objects.create(worksheet=ws2, text="Identify the fronted adverbial in this sentence: 'Before the sun rose, the birds began to sing.'", order=1)
    AnswerOption.objects.create(question=q4, text="the birds began to sing", is_correct=False)
    AnswerOption.objects.create(question=q4, text="Before the sun rose", is_correct=True)
    AnswerOption.objects.create(question=q4, text="the sun rose", is_correct=False)
    
    print("Successfully seeded EdPlace-style worksheets!")

if __name__ == '__main__':
    seed_db()
