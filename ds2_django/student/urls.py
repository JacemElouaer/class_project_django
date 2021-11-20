from django.urls import path
from .views import *

urlpatterns = [
    path('students', students, name="all_students"),
    path('students/<int:id>', student_detail, name="RUD_students"),
]
