from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User


class StudentGroupForm(ModelForm):
    class Meta:
        model = StudentGroup
        fields = "__all__"


class AbsenceForm(ModelForm):
    class Meta:
        model = Absence
        fields = '__all__'


class HomeWorkForm(ModelForm):
    class Meta:
        model = HomeWork
        fields = '__all__'
