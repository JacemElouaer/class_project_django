# Generated by Django 3.2.9 on 2021-11-27 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=150, null=True)),
                ('lastname', models.CharField(max_length=150, null=True)),
                ('photo', models.ImageField(null=True, upload_to='image/teacher')),
                ('email_pro', models.EmailField(max_length=150, null=True, verbose_name='professional email')),
                ('email_per', models.EmailField(max_length=150, null=True, verbose_name='personal email')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Teacher',
            },
        ),
    ]
