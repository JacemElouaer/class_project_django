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

def home(request):
    context = {}
    return render(request ,'pages/home.html', context)


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


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, id):
    try:
        student = Teacher.objects.get(id=id)
    except Teacher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = TeacherSerializer(student)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = TeacherSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



