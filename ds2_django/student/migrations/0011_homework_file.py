# Generated by Django 3.2.9 on 2021-12-13 23:41

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_rename_students_homework_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=student.models.file_path),
        ),
    ]
