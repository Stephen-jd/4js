from django.contrib import admin
from .models import TaylorFitSubmission, ContactInquiry

@admin.register(TaylorFitSubmission)
class TaylorFitSubmissionAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'year_group', 'target_exams', 'created_at')
    list_filter = ('year_group', 'created_at')

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
