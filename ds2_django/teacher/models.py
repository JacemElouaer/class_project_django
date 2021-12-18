from django.db import models
from django.contrib.auth.models import User
from module.models import Module
from student.models import StudentGroup, HomeWork
from django.utils.text import slugify

# Create your models here.

import os


class Teacher(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=150, null=True)
    lastname = models.CharField(max_length=150, null=True)
    photo = models.ImageField(upload_to='image/teacher', null=True)
    email_pro = models.EmailField(max_length=150, verbose_name="professional email", null=True)
    email_per = models.EmailField(max_length=150, verbose_name="personal email", null=True)
    slug = models.SlugField(blank=True, null=True)
    modules =  models.ManyToManyField(Module, blank=True)

    def __str__(self):
        return self.firstname

    class Meta:
        db_table = "Teacher"

    '''def save(self, *args, **kwargs):
        # do something before
        if self.slug is None :
            self.slug = slugify()
        super().save(*args, **kwargs)
        # do something after'''


class relation_G_T_M(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True , blank=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True ,blank=True)
    group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, null=True ,blank=True)

    class Meta:
        db_table = "relation Student Teacher Model"


class relation_H_T_M(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,null=True ,  blank=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True , blank=True)
    homework = models.ForeignKey(HomeWork, on_delete=models.CASCADE , null=True ,blank=True)

    class Meta:
        db_table = "relation homework Teacher Model"
