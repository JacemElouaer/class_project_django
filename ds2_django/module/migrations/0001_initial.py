# Generated by Django 3.2.9 on 2021-11-27 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.FloatField(max_length=2)),
                ('comment', models.TextField(max_length=250, null=True)),
            ],
            options={
                'db_table': 'Evaluation',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(null=True, verbose_name='start date')),
                ('end_date', models.DateTimeField(null=True, verbose_name='start date')),
                ('class_number', models.IntegerField()),
                ('objectif', models.TextField(max_length=150)),
                ('resume', models.TextField(max_length=150)),
                ('status', models.CharField(choices=[('In_progress', 'In progress'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], max_length=100)),
                ('tools', models.CharField(choices=[('software', 'software'), ('hardware', 'hardware')], max_length=100)),
                ('type', models.CharField(choices=[('Normal', 'Normal'), ('Catch-up', 'Catch-up'), ('Support', 'Support'), ('training', 'training')], max_length=100)),
            ],
            options={
                'db_table': 'Session',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True, unique=True)),
                ('type', models.CharField(choices=[('valid', 'valid'), ('invalid', 'invalid')], max_length=150)),
                ('evaluation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='module.evaluation')),
            ],
            options={
                'db_table': 'Module',
            },
        ),
    ]
