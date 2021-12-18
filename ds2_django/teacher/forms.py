from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"




class relation_H_T_M_Form(ModelForm):
    class Meta:
        model: relation_H_T_M
        fields = "__all__"


class relation_G_T_M_Form(ModelForm):
    class Meta:
        model: relation_G_T_M
        fields = "__all__"