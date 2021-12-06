from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('student_register', register_student,  name="student_register"),
    path('teacher_register', register_teacher,  name="teacher_register"),
    path('student_login', login_student,  name="student_login"),
    path('teacher_login', login_teacher,  name="teacher_login"),

]