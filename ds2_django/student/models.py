from django.db import models
from module.models import Session, Module, Evaluation
from django.contrib.auth.models import User
import os


def file_path(instance, filename):
    path = "documents/"
    format = "uploaded-" + filename
    return os.path.join(path, format)


class Student(models.Model):
    Std_state = (
        ("nouveau", "nouveau"),
        ("redoublant", "redoublant"),
        ("derogataire", "derogataire")
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    lastname = models.CharField(max_length=150, null=True)
    firstname = models.CharField(max_length=150, null=True)
    photo = models.ImageField(upload_to='image/student',blank=True, null=True)
    email = models.EmailField(max_length=150, null=True)
    state = models.CharField(max_length=150, null=True, choices=Std_state)
    group = models.ForeignKey("StudentGroup", null=True,blank=True ,on_delete=models.CASCADE)

    class Meta:
        db_table = "Student"

    def __str__(self):
        return self.firstname

    def full_name(self):
        return self.firstname + " " + self.lastname


class StudentGroup(models.Model):
    Level = (
        ("level_1", "level 1"),
        ("level_2", "level 2")
    )
    name = models.CharField(max_length=15, null=True, verbose_name="Group  name")
    mail_Group = models.CharField(max_length=15, null=True, verbose_name="Group email")
    level = models.CharField(max_length=25, null=True, verbose_name="Group Level", choices=Level)

    class Meta:
        db_table = "StudentGroup"

    def __str__(self):
        return str(self.id)+ "/" + self.name


class Absence(models.Model):
    Reason = (
        ("different type", "different type")
        , ("other type", "other type")
    )
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE,verbose_name="Absent Student")
    session = models.ForeignKey(Session, null=True, on_delete=models.CASCADE, verbose_name="Absent Session")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Absent Date")
    justification = models.TextField(max_length=250, null=True, verbose_name="Absent justification")
    reason = models.CharField(max_length=15, null=True, verbose_name="Reason of absence", choices=Reason)

    class Meta:
        db_table = "Student_absence"

    def __str__(self):
        return self.reason


class HomeWork(models.Model):
    Status = (
        ("ended", "ended"),
        ("untended", "untended")
    )
    title = models.CharField(max_length=30, null=True, verbose_name="Homework title")
    launch_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, verbose_name="Homework deadline")
    description = models.TextField(max_length=250, null=True)
    order = models.FileField(upload_to=file_path, null=True, blank=True)
    file = models.FileField(upload_to=file_path, null=True, blank=True)
    lien_github = models.CharField(max_length=255, blank=True, null=True)
    module = models.ForeignKey(Module, null=True, verbose_name="Homework module", on_delete=models.CASCADE)
    status = models.CharField(max_length=15, null=True, choices=Status)
    student = models.ForeignKey(Student, verbose_name="Student homeworks", null=True, blank=True,
                                   on_delete=models.CASCADE)
    group = models.ForeignKey("StudentGroup", verbose_name="Student homeworks group", null=True, blank=True,
                                 on_delete=models.CASCADE)
    evaluation = models.OneToOneField(Evaluation, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "Students_groups_homework"

    def __str__(self):
        return self.title
