# Generated by Django 3.2.9 on 2021-11-26 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_auto_20211126_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='bio',
        ),
    ]
