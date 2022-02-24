# Generated by Django 4.0.2 on 2022-02-23 16:36

import datetime
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
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('team', models.CharField(max_length=100)),
                ('project_status', models.CharField(choices=[('Finish', 'Finish'), ('Pending', 'Pending'), ('Started', 'Started'), ('In Discussion', 'In Discussion')], default=4, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Workreport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, max_length=100)),
                ('team', models.CharField(blank=True, max_length=100)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.CharField(blank=True, max_length=100)),
                ('comment', models.TextField()),
                ('updated_by', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Worksheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=100)),
                ('working_on', models.CharField(max_length=100)),
                ('work_status', models.CharField(max_length=20)),
                ('entry_date', models.DateTimeField(default=datetime.datetime.now)),
                ('description', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='profile_pic')),
                ('designation', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]