# Generated by Django 2.2 on 2019-04-26 20:15

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
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20, null=True)),
                ('registration_number', models.CharField(default='2016-814-413', max_length=70)),
                ('hall_name', models.CharField(blank=True, default='Dr. muhammad sahidullah hall', max_length=100, null=True)),
                ('department_name', models.CharField(blank=True, max_length=100, null=True)),
                ('admission_year', models.PositiveIntegerField(blank=True, default=1980, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=10, null=True)),
                ('date_of_birth', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
