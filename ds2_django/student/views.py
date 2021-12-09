from django.views.decorators.csrf import csrf_exempt
from rest_framework import response
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import *
from .serializers import *
from .models import *
import numpy as np


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
def StudentGroup(request, id):
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
def StudentGroup(request, id):
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
