from django.forms import ModelForm
from teacher.models import Teacher
from student.models import Student
from django.contrib.auth.models import User


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ('firstname', 'lastname', 'email_pro', 'email_per', 'slug')


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('firstname', 'lastname', 'birthday', 'email', 'state', 'group')
