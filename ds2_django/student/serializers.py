from rest_framework.serializers import ModelSerializer
from .models import *


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class GroupSerializer(ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = '__all__'


class HomeworkSerializer(ModelSerializer):
    class Meta:
        model = HomeWork
        fields = '__all__'


class AbsenceSerializer(ModelSerializer):
    class Meta:
        model = Absence
        fields = '__all__'

