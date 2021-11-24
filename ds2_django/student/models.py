from django.db import models
from module.models import Session, Module


# Create your models here.


class Student(models.Model):
    Std_state = (
        ("nouveau", "nouveau"),
        ("redoublant", "redoublant"),
        ("derogataire", "derogataire")
    )
    lastname = models.CharField(max_length=150, null=True)
    username = models.CharField(max_length=150, null=True)
    birthday = models.DateTimeField(null=True)
    photo = models.ImageField(upload_to='image/student', null=True)
    email = models.EmailField(max_length=150, null=True)
    state = models.CharField(max_length=150, null=True, choices=Std_state)
    group = models.ForeignKey("Group", on_delete=models.CASCADE)
    homework = models.ManyToManyField("Homework", verbose_name="Student homeworks")

    class Meta:
        db_table = "Student"


class Group(models.Model):
    Level = (
        ("level_1", "level 1"),
        ("level_2", "level 2")
    )
    name = models.CharField(max_length=15, null=True, verbose_name="Group  name")
    mail_Group = models.CharField(max_length=15, null=True, verbose_name="Group email")
    level = models.CharField(max_length=25, null=True, verbose_name="Group Level", choices=Level)
    homeworks = models.ManyToManyField("HomeWork", verbose_name="Group Homeworks")


class Absence(models.Model):
    Reason = (
        ("different type", "different type")
        , ("other type", "other type")
    )
    student = models.OneToOneField("Student", null=True, on_delete=models.CASCADE, verbose_name="Absent Student")
    session = models.OneToOneField(Session, null=True, on_delete=models.CASCADE, verbose_name="Absent Session")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Absent Date")
    justification = models.TextField(max_length=250, null=True, verbose_name="Absent justification")
    reason = models.CharField(max_length=15, null=True, verbose_name="Reason of absence", choices=Reason)


class HomeWork(models.Model):
    Status = (
        ("ended", "ended"),
        ("untended", "untended")
    )
    title = models.CharField(max_length=30, null=True, verbose_name="Homework title")
    launch_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, verbose_name="Homework deadline")
    description = models.TextField(max_length=250, null=True)
    module = models.ForeignKey(Module, null=True, verbose_name="Homework module", on_delete=models.CASCADE)
    status = models.CharField(max_length=15, null=True, choices=Status)
