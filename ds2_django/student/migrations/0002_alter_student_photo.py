# Generated by Django 3.2.9 on 2021-11-19 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(null=True, upload_to='image/student'),
        ),
    ]
