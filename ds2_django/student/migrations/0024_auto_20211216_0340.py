# Generated by Django 3.2.9 on 2021-12-16 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0023_alter_student_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='absence',
            name='student',
        ),
        migrations.AddField(
            model_name='student',
            name='absence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.absence', verbose_name='Absent Student'),
        ),
    ]