from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"


