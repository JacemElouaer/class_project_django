# Generated by Django 3.2.9 on 2021-12-13 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0003_remove_module_evaluation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='note',
            field=models.FloatField(max_length=2, null=True),
        ),
    ]
