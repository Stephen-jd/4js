from django.db import models

class TaylorFitSubmission(models.Model):
    student_name = models.CharField(max_length=100)
    year_group = models.CharField(max_length=50)
    target_exams = models.CharField(max_length=200) # Stored as comma separated
    target_grade = models.CharField(max_length=100)
    guidance = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - Year {self.year_group}"

class ContactInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class Worksheet(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    key_stage = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.key_stage} {self.subject})"

class Question(models.Model):
    worksheet = models.ForeignKey(Worksheet, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Q: {self.text[:50]}"

class AnswerOption(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} {'(Correct)' if self.is_correct else ''}"


class SyllabusSubject(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50, choices=[('GCSE', 'GCSE'), ('A-Level', 'A-Level'), ('KS3', 'KS3'), ('Primary', 'Primary')])
    description = models.TextField()

    def __str__(self):
        return f"{self.level} - {self.name}"

class SyllabusModule(models.Model):
    subject = models.ForeignKey(SyllabusSubject, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    topics = models.TextField(help_text="Comma separated topics")

    def __str__(self):
        return f"{self.subject.name} - {self.title}"

class PastPaper(models.Model):
    subject = models.ForeignKey(SyllabusSubject, on_delete=models.CASCADE, related_name='past_papers')
    board = models.CharField(max_length=50, choices=[('AQA', 'AQA'), ('Edexcel', 'Edexcel'), ('OCR', 'OCR')])
    year = models.IntegerField()
    paper_name = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return f"{self.board} {self.year} - {self.paper_name}"
