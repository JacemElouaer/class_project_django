# Generated by Django 3.2.9 on 2021-12-15 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_remove_student_module'),
        ('module', '0005_remove_module_teacher'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='relation_S_T_M',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='student.studentgroup')),
                ('module', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='module.module')),
                ('teacher', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
            ],
        ),
    ]