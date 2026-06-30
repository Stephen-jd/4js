from django.contrib import admin
from .models import TaylorFitSubmission, ContactInquiry, Worksheet, Question, AnswerOption

@admin.register(TaylorFitSubmission)
class TaylorFitSubmissionAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'year_group', 'target_exams', 'created_at')
    list_filter = ('year_group', 'created_at')
    search_fields = ('student_name', 'target_exams')

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email')

class AnswerOptionInline(admin.TabularInline):
    model = AnswerOption
    extra = 4

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    show_change_link = True

@admin.register(Worksheet)
class WorksheetAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'key_stage', 'created_at')
    list_filter = ('subject', 'key_stage')
    search_fields = ('title', 'description')
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'worksheet', 'order')
    list_filter = ('worksheet__subject', 'worksheet__key_stage')
    inlines = [AnswerOptionInline]
