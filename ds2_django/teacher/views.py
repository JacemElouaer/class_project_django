from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from rest_framework import response
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from .models import *
from .serializers import *
from .models import *
from .forms import *
from .utils import *
from module.forms import ModuleForm
from module.models import Module
from student.models import StudentGroup, Student, Absence
from student.forms import HomeWorkForm, StudentGroupForm, StudentForm, AbsenceForm
import numpy as np


def home(request):
    context = {}
    return render(request, 'pages/home.html', context)


@csrf_exempt
@api_view(['GET', 'POST'])
def teachers(request):
    if request.method == "GET":
        students = Teacher.objects.all()
        serializer = TeacherSerializer(students, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def teacher(request):
    current_user = request.user
    try:
        current_teacher = Teacher.objects.get(user=current_user)

    except  Teacher.DoesNotExist:
        context = {"current_teacher": "not valid"}
        return render(request, "index.html", context)
    try:
        relations_G_T_M = relation_G_T_M.objects.filter(teacher=current_teacher)
    except relation_G_T_M.DoesNotExist:
        context = {"relations_G_T_M": "not valid"}
        return render(request, "index.html", context)

    context = {"current_teacher": current_teacher, "relations_G_T_M": relations_G_T_M}
    print(current_teacher, relations_G_T_M)
    return render(request, 'pages/home.html', context)


def group(request):
    current_user = request.user
    try:
        current_teacher = Teacher.objects.get(user=current_user)

    except  Teacher.DoesNotExist:
        context = {"current_teacher": "not valid"}
        return render(request, "index.html", context)
    try:
        relations_G_T_M = relation_G_T_M.objects.filter(teacher=current_teacher)
    except relation_G_T_M.DoesNotExist:
        context = {"relations_G_T_M": "not valid"}
        print(context)
        return render(request, "index.html", context)
    groups = []
    chart_group_homework(relations_G_T_M)
    print(groups)
    labels, data = chart_group_homework(relations_G_T_M)

    context = {"current_teacher": current_teacher,
               "relations_G_T_M": relations_G_T_M,
               "labels": labels, "data": data
               }

    print(current_teacher, relations_G_T_M)
    return render(request, 'pages/group.html', context)


def Modules(request):
    current_user = request.user
    current_teacher = Teacher.objects.get(user=current_user)
    modules = Module.objects.filter(id__in=current_teacher.modules.id)
    context = {"current_teacher": current_teacher, "modules": modules}
    return render(request, 'pages/Module.html', context)


def Students(request):
    current_user = request.user
    try:
        current_teacher = Teacher.objects.get(user=current_user)
        relations_G_T_M = relation_G_T_M.objects.filter(teacher=current_teacher)
    except  Teacher.DoesNotExist and relation_G_T_M.DoesNotExist:
        context = {"relations_G_T_M": "not valid"}
        return render(request, "index.html", context)
    groups = []
    for relation in relations_G_T_M:
        groups.append(relation.group)
    number = len(groups)
    students = Student.objects.filter(group__in=groups)
    homework_number = number_of_homework(students)

    context = {"current_teacher": current_teacher, "relations_G_T_M": relations_G_T_M
        , "students": students, "number": number, "homework_number": homework_number}
    print(students)
    return render(request, 'pages/Students.html', context)


def Homework(request):
    current_user = request.user
    current_teacher = Teacher.objects.get(user=current_user)
    relation = relation_H_T_M.objects.filter(teacher=current_teacher)
    context = {"relation": relation, }
    return render(request, 'pages/Homework.html', context)


def group_details(request, id):
    groupwanted = StudentGroup.objects.get(id=id)
    try:
        studentsgroup = Student.objects.filter(group=groupwanted)
    except Student.DoesNotExist:
        context = {"students": None}
        return render(request, 'simplepages/group_details.html', context)
    context = {"students": studentsgroup, "groupwanted": groupwanted}
    print(studentsgroup)
    return render(request, 'simplepages/group_details.html', context)


def addstudenthomework(request):
    current_user = request.user
    current_teacher = Teacher.objects.get(user=current_user)
    print("hello there")
    if request.method == 'POST':
        form = HomeWorkForm(request.POST)
        if form.is_valid():
            homework = form.save()
            relation = relation_H_T_M.objects.create()
            relation.homework = homework
            relation.module = homework.module
            relation.teacher = current_teacher
            relation.save()
            print(relation)
            return redirect("/teacher/Student/")
    else:
        form = HomeWorkForm()
    context = {'form': form}

    return render(request, 'forms/AddStudenthomework.html', context)


def addGrouphomework(request, id):
    current_user = request.user
    current_teacher = Teacher.objects.get(user=current_user)

    if request.method == 'POST':

        form = HomeWorkForm(request.POST)
        print(form)
        if form.is_valid():
            print("hello there")
            homework = form.save()
            relation = relation_H_T_M.objects.create()
            relation.homework = homework
            relation.module = homework.module
            relation.teacher = current_teacher
            relation.save()
            print(relation)
            return redirect("/teacher/group")
    else:
        form = HomeWorkForm()
    context = {'form': form}
    return render(request, 'forms/Addhomework.html', context)


def addGroup(request):
    current_user = request.user
    current_teacher = Teacher.objects.get(user=current_user)

    if request.method == 'POST':

        form = StudentGroupForm(request.POST)

        print(form)
        if form.is_valid():
            group = form.save()
            relation = relation_G_T_M.objects.create()
            relation.teacher = current_teacher
            relation.group = group
            relation.save()
            return redirect("/teacher/group")
    else:
        form = StudentGroupForm()
    context = {'form': form}
    return render(request, 'forms/AddGroup.html', context)


# add teacher

class DeleteGroup(generic.DeleteView):
    template_name = 'forms/DeleteGroup.html'
    model = StudentGroup
    success_url = '/teacher/group'


def addModule(request):
    current_user = request.user
    current_teacher = Teacher.objects.get(user=current_user)
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        print(form)
        if form.is_valid():
            module = form.save()
            current_teacher.modules.add(module)

            return redirect("/teacher/module")
    else:
        form = StudentGroupForm()
    context = {'form': form}
    return render(request, 'forms/AddModule.html', context)


def groupModule(request, id):
    group = StudentGroup.objects.get(id)
    current_user = request.user
    current_teacher = Teacher.objects.get(user=current_user)
    modules = Module.objects.filter(id__in=current_teacher.modules.id)
    current_teacher = Teacher.objects.get(user=current_user)
    relations = relation_G_T_M.objects.filter(group=group, teacher=current_teacher)
    context = {"relations": relations, "modules": modules}
    return render(request, "forms/ModuleGroup.html", context)


def updateGroup(request, id):
    current_user = request.user
    current_teacher = Teacher.objects.get(user=current_user)
    group = StudentGroup.objects.get(id=id)
    form = StudentGroupForm(instance=group)
    if request.method == "POST":
        form = StudentGroupForm(request.POST, instance=group)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/teacher/group/')
    context = {'form': form}
    return render(request, "forms/UpdateGroup.html", context)


def addStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("/teacher/home")
    else:
        form = StudentGroupForm()
    context = {'form': form}
    return render(request, 'forms/AddStudent.html', context)


def updateStudent(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentGroupForm(request.POST, instance=student)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/teacher/group/')
    context = {'form': form}
    return render(request, "forms/UpdateStudent.html", context)


def student_detail(request, id):
    student = Student.objects.get(id=id)
    current_user = request.user
    current_teacher = Teacher.objects.get(user=current_user)
    context = {"student": student, "current_teacher": current_teacher}
    return render(request, 'simplepages/Student_details.html', context)


def Student_absence(request):
    context = {}
    return render(request, 'simplepages/Student_details.html', context)


def student_add_absence(request):
    form = AbsenceForm()
    if request.method == 'POST':
        form = AbsenceForm(request.POST)
        if form.is_valid():
            return redirect("/teacher/Student/")
    else:
        form = AbsenceForm()
    context = {'form': form}
    return render(request, 'forms/AddAbsence.html', context)


def chart(request):
    return render(request, 'chart.html')
