from rest_framework.serializers import ModelSerializer
from .models import *


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
