from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User


class EvaluationForm(ModelForm):
    class Meta:
        model = Evaluation
        fields = "__all__"


class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = '__all__'


class ModuleForm(ModelForm):
    class Meta:
        model = Module
        fields = '__all__'
