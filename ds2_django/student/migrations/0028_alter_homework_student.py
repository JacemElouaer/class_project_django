# Generated by Django 3.2.9 on 2021-12-17 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0027_auto_20211217_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student', verbose_name='Student homeworks'),
        ),
    ]
