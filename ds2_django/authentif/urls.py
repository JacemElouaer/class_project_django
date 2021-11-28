from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('student/register/', register_student,  name="student_register"),
    path('teacher/register/', register_teacher,  name="teacher_register")
]