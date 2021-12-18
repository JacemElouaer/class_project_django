from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from .serializers import *
from .forms import *
from .utils import *
from teacher.models import relation_G_T_M
from django.core.exceptions import ObjectDoesNotExist

''' general  comment about view:
--> Student views
--> StudentGroup views 
--> homework
'''


# Create your views here.

# Student View----
@csrf_exempt
@api_view(['GET', 'POST'])
def students(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Student Group View
@csrf_exempt
@api_view(['GET', 'POST'])
def StudentGroups(request):
    try:
        groupStudent = StudentGroup.objects.all()
    except StudentGroup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializer(groupStudent)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def GETStudentGroup(request, id):
    try:
        GroupStudent = StudentGroup.objects.get(id=id)
    except StudentGroup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = GroupSerializer(GroupStudent)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = GroupSerializer(GroupStudent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        StudentGroup.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'POST'])
def Abcences(request):
    try:
        absences = Absence.objects.all()
    except Absence.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializer(absences)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = AbsenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def oneStudentGroup(request, id):
    try:
        absence = Absence.objects.get(id=id)
    except Absence.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = AbsenceSerializer(absence)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = AbsenceSerializer(absence, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        absence.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Homework View
@csrf_exempt
@api_view(['GET', 'POST'])
def HomeWorks(request):
    try:
        homeworks = HomeWork.objects.all()
    except HomeWork.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = HomeworkSerializer(homeworks)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = HomeworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Homework(request, id):
    try:
        homework = HomeWork.objects.get(id=id)
    except HomeWork.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = HomeworkSerializer(homework)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = StudentSerializer(homework, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        homework.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def logged_Student(request):
    current_user = request.user
    try:
        current_student = Student.objects.get(user=current_user)
    except Student.DoesNotExist:
        return None
    return current_student


def home(request):
    current_user = request.user
    try:
        current_student = Student.objects.get(user=current_user)
    except Student.DoesNotExist:
        context = {"current_student": "not valid"}
        return render(request, "index.html", current_student)

    number = Number_of_student_in_user_group(current_student)
    number_modules = Number_of_Modules_applicated(current_student)
    #homework_percentage = ended_percentage_homework(current_student)
    Absences = getAbsences(current_student)
    print(Absences)
    context = {"current_student": current_student,
               "number": number, "number_modules": number_modules,
                "Absences": Absences}
    return render(request, "index.html", context)


def group(request):
    current_student = logged_Student(request)
    student_of_group, student_Group = GroupStudent(current_student)
    print(student_of_group)
    context = {"groups_student": student_of_group, "current_student": current_student, "student_Group": student_Group}
    return render(request, 'group.html', context)


def homework(request):
    current_student = logged_Student(request)
    homeworks, homeworks_evaluation = StudentHomework(current_student)

    context = {"current_student": current_student,
               "homeworks": homeworks,
               "homeworks_evaluation": homeworks_evaluation}
    print(homeworks, "this is homew eval", homeworks_evaluation)
    return render(request, 'homework.html', context)


def profile(request):
    context = {}
    return render(request, 'profile.html', context)


def module(request):
    current_user = request.user
    current_student = Student.objects.get(user=current_user)
    try:
        current_group = StudentGroup.objects.get(id=current_student.group.id)
    except ObjectDoesNotExist:
        context = {"current_group": current_group}
        return render(request, 'Module.html', context)
    try:
        relations = relation_G_T_M.objects.filter(group=current_group)
    except ObjectDoesNotExist:
        relations = None
    # labels, number_absence = taux_absence_per_module(relations)
    # numbers = []
    # for absence in  number_absence:
    #     if not absence:
    #         numbers.append(0)
    #     else:
    #         numbers.append(absence[0].num_absence)
    n_session , n_absence =  number_session(current_student , relations)
    n_present =  n_session - n_absence

    context = {
        "current_user" : current_user ,
        "current_group": current_group, 'relations': relations , "n_session":n_session , "n_present":n_present, "n_absence":n_absence
    }
    return render(request, 'Module.html', context)


def AbsenceForm(request, id):
    context = {}
    return render(request, 'layouts/Absence.html', context)


def updatehomework(request, id):
    homework = HomeWork.objects.get(id=id)
    form = SubmitHomeWorkForm(instance=homework)
    if request.method == "POST":
        form = SubmitHomeWorkForm(request.POST, instance=homework)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/student/home')
    context = {'form': form}
    return render(request, "homework/homework.html", context)
