from django.db import models


# Create your models here.


class Student(models.Model):
    Std_state = (
        ("nouveau", "nouveau"),
        ("redoublant", "redoublant"),
        ("derogataire", "derogataire")
    )
    lastname = models.CharField(max_length=150, null=True)
    username = models.CharField(max_length=150, null=True)
    bithdate = models.DateTimeField(null=True)
    photo = models.ImageField(upload_to='image/student', null=True)
    email = models.EmailField(max_length=150, null=True)
    state = models.CharField(max_length=150, null=True, choices=Std_state)

    class Meta:
        db_table = "Student"
