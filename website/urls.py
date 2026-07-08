from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('primary/', views.primary, name='primary'),
    path('secondary/', views.secondary, name='secondary'),
    path('gcse/', views.gcse, name='gcse'),
    path('alevel/', views.alevel, name='alevel'),
    path('entrance-exams/', views.entrance_exams, name='entrance_exams'),
    path('why-us/', views.why_us, name='why_us'),
    path('api/taylorfit/', views.submit_taylorfit, name='submit_taylorfit'),
    path('api/contact/', views.submit_contact, name='submit_contact'),
    path('api/chatbot/', views.chatbot_query, name='chatbot_query'),
    path('worksheets/', views.worksheets_list, name='worksheets_list'),
    path('worksheets/<int:worksheet_id>/', views.take_worksheet, name='take_worksheet'),
    path('syllabus_explorer/', views.syllabus_explorer, name='syllabus_explorer'),
    path('terms/', views.terms, name='terms'),
]
