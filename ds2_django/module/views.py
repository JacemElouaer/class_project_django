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
def modules(request):
    if request.method == "GET":
        modules = Module.objects.all()
        serializer = ModuleSerializer(modules, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def modules(request, id):
    try:
        module = Module.objects.get(id=id)
    except Module.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ModuleSerializer(module)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = ModuleSerializer(module, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        module.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'POST'])
def evaluation(request):
    if request.method == "GET":
        evaluations = Module.objects.all()
        serializer = EvaluationSerializer(evaluations, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = EvaluationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def evluations(request, id):
    try:
        evaluation = Module.objects.get(id=id)
    except Module.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = EvaluationSerializer(evaluation)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = EvaluationSerializer(evaluation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        evaluation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@csrf_exempt
@api_view(['GET', 'POST'])
def session(request):
    if request.method == "GET":
        sessions = Module.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def sessions(request, id):
    try:
        session = Module.objects.get(id=id)
    except Module.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = SessionSerializer(session)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = SessionSerializer(session, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

