from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=150, null=True)
    lastname = models.CharField(max_length=150, null=True)
    photo = models.ImageField(upload_to='image/teacher', null=True)
    email_pro = models.EmailField(max_length=150, verbose_name="professional email", null=True)
    email_per = models.EmailField(max_length=150, verbose_name="personal email", null=True)

    class Meta:
        db_table = "Teacher"



