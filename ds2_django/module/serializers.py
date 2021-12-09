from rest_framework.serializers import ModelSerializer
from .models import *


class ModuleSerializer(ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'


class EvaluationSerializer(ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'


class SessionSerializer(ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
