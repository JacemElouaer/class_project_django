from django.urls import path
from .views import *




urlpatterns = [
    path('students', students, name="all_students"),
    path('students/<int:id>', student_detail, name="RUD_students"),
    path("home", home, name="studenthome"),
    path("group", group, name="studentGroup"),
    path("homework", homework, name="studentHomework"),
    path("profile", profile, name="studentProfile"),
    path("module", module, name="studentModule"),
    path("EditAbsence/<int:id>", AbsenceForm, name="AbsenceForm"),
    path("update_homework/<int:id>", updatehomework, name="updatehomework"),


]
