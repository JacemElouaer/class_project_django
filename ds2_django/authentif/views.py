from django.shortcuts import render, redirect
from django.http import HttpResponse
from  django.contrib import messages
from .decorators import unauthenticated_user
from .forms import TeacherForm, StudentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user


# Create your views here.

@unauthenticated_user
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

    return render(request, 'registration/teacher_register.html' ,  context)

@unauthenticated_user
def register_student(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        student_form = StudentForm(request.POST)
        if not student_form.is_valid():
            print(StudentForm.is_valid())
        if form.is_valid() and student_form.is_valid():
            studentuser = form.save()
            student_form = student_form.save(commit=False)
            print(studentuser)
            student_form.user = studentuser
            student_form.save()
            return HttpResponse("this is done")
    else:
        form = UserCreationForm()
        student_form = StudentForm()

    context = {'form': form, 'student_form': student_form}

    return render(request, 'registration/student_register.html', context)

@unauthenticated_user
def login_student(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,  password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'username OR password is incorrect !!' )


    context = {}
    return render(request, 'login/student_login.html' ,  context)

@unauthenticated_user
def login_teacher(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/teacher/home")
        else:
            messages.info(request, 'username OR password is incorrect !!' )
    context = {}
    return render(request, 'login/teacher_login.html', context)


def logout_user(request):
    logout(request)
    return redirect('/home')


