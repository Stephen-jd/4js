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
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.name}"
