from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TeacherForm ,StudentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


# Create your views here.


def register_teacher(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        teacher_form = TeacherForm(request.POST)
        if not teacher_form.is_valid():
            print({{teacher_form.errors}})
        if form.is_valid() and teacher_form.is_valid():
            user = form.save()
            teacher_profile = teacher_form.save(commit=False)
            teacher_profile.user = user
            teacher_profile.save()
            return HttpResponse("this is done")
    else:
        form = UserCreationForm()
        teacher_form = TeacherForm()

    context = {'form': form, 'teacher_form': teacher_form}

    return render(request, 'registration/registration_teacher.html', context)


def register_student(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        student_form = StudentForm(request.POST)
        if not StudentForm.is_valid():
            print({{StudentForm.errors}})
        if form.is_valid() and StudentForm.is_valid():
            user = form.save()
            teacher_profile = StudentForm.save(commit=False)
            teacher_profile.user = user
            teacher_profile.save()
            return HttpResponse("this is done")
    else:
        form = UserCreationForm()
        student_form = StudentForm()

    context = {'form': form, 'teacher_form': student_form}

    return render(request, 'registration/registration_student.html', context)
