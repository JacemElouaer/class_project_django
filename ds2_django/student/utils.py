from .models import *
from teacher.models import relation_G_T_M
from module.models import Session
from django.db.models import Count


# ---------------------------  home  methods ----------------------------------

def Number_of_student_in_user_group(current_student):
    Students_number = Student.objects.all().filter(group=current_student.group).count
    return Students_number


def Number_of_Modules_applicated(current_student):
    try:
        Modules_Number = relation_G_T_M.objects.filter(group=current_student.group).count()
    except relation_G_T_M.DoesNotExist:
        return None
    return Modules_Number


def getAbsences(current_student):
    try:
        absences = Absence.objects.filter(student=current_student)
    except Absence.DoesNotExist:
        absences = None
    return absences


# class homework():
# def ended_percentage_homework(current_student):


def ended_percentage_homework(current_student):
    student_Group = current_student.group
    try:
        number_ended_homework_group = HomeWork.objects.get(group=student_Group).filter(status='ended').count()
    except HomeWork.DoesNotExist:
        number_ended_homework_group = 0
    try:
        number_ended_homework_student = HomeWork.objects.filter(student=current_student).filter(status='ended').count()
    except HomeWork.DoesNotExist:
        number_ended_homework_student = 0
    try:
        number_homework_group = HomeWork.objects.get(group=student_Group).count()
    except HomeWork.DoesNotExist:
        number_homework_group = 0
    try:
        number_homework_student = HomeWork.objects.filter(student=current_student).count()
    except  HomeWork.DoesNotExist:
        number_homework_group = 0

    Total_ended_homework = number_ended_homework_group + number_ended_homework_student
    Total_homework_number = number_homework_group + number_homework_student
    if Total_homework_number == 0:
        return 0
    return round(Total_ended_homework / Total_homework_number) * 100


# --------------------------------- Group methods ---------------------------------


def GroupStudent(current_student):
    student_Group = current_student.group
    groups_student = Student.objects.filter(group=student_Group)
    return groups_student, student_Group


def StudentHomework(current_student):
    try:
        homeworks = HomeWork.objects.filter(student=current_student)
        homeworks_evaluation = HomeWork.objects.filter(student=current_student).filter(evaluation__isnull=False)
    except HomeWork.DoesNotExist:
        homeworks = None
        homeworks_evaluation = None

    return homeworks, homeworks_evaluation



# --------------------------------------- Absence -----------------------------
def taux_absence_per_module(relations_G_T_M):
    modules = []
    for relation in relations_G_T_M:
        modules.append(relation.module)
    labels = modules
    number_absence = [Session.objects.filter(module=module).annotate(num_absence=Count('absence')) for module in modules]
    return labels, number_absence


def number_session(current_student,relations):
    modules = []
    for relation in relations:
        modules.append(relation.module)
    n_session = Session.objects.filter(module__in=modules).count()
    n_absence = Absence.objects.filter(student= current_student).count()
    return n_session , n_absence





