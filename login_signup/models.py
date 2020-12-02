# dappx/models.py

from django.db import models
from django.contrib.auth.models import User

import datetime
# Create your models here.

class UserProfileInfo(models.Model):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # portfolio_site = models.URLField(blank=True)

    # profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    gender = models.CharField(max_length=20, choices=gender_choices)
    registration_number = models.CharField(max_length=70, default='2016-814-413')
    hall_name = models.CharField(max_length=100, default='Dr. muhammad sahidullah hall',null=True,blank=True)
    department_name = models.CharField(max_length=100,null=True,blank=True)
    admission_year = models.PositiveIntegerField(default=2010,null=True,blank=True)
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    blood_group = models.CharField(max_length=10,null=True,blank=True)
    date_of_birth = models.DateField(default=datetime.date.today)

def __str__(self):
    return self.user.username