import os

models_code = """
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
"""

models_path = "c:/Users/steph/Downloads/theos/website/models.py"
with open(models_path, 'a', encoding='utf-8') as f:
    f.write('\n' + models_code)
