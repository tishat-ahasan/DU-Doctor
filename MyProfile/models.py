import datetime

from django.db import models

# Create your models here.
class AppointmentInfo (models.Model):
    username = models.CharField(max_length=35)
    gender = models.CharField(max_length=15,default="Male")
    registration_number = models.CharField(max_length=35,null=True,blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    blood_group = models.CharField(max_length=10, null=True, blank=True)
    date_of_birth = models.DateField(default=datetime.date.today, null=True, blank=True)
    appointment_date = models.DateField(default=datetime.date.today, null=True, blank=True)
    test_result = models.TextField(max_length=500,default="no test")
    medicine = models.TextField(max_length=250,default="no medicine")
    instructions = models.TextField(max_length=300,default="take rest")
    disease_description = models.TextField(max_length=500,default="fever")