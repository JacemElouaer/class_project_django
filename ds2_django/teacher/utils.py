from .models import *
from student.models import StudentGroup, Student, HomeWork
from module.models import Session
from django.db.models import Count


def number_of_homework(students):
    number_of_homeworks = HomeWork.objects.filter(student__in=students).count()
    return number_of_homeworks


def chart_group_homework(relations_G_T_M):
    groups = []
    for relation in relations_G_T_M:
        groups.append(relation.group)
    data = [HomeWork.objects.filter(group=group).count() for group in groups]
    labels = [group.name for group in groups]
    return labels, data


def chart_group_absence(relations_G_T_M):
    groups = []
    for relation in relations_G_T_M:
        groups.append(relation.group)

    students = Student.objects.filter(group__in=groups).filter(absence)
    nombre



