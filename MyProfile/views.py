from django.http import HttpResponseRedirect
from django.shortcuts import render
from login_signup.models import UserProfileInfo
from django.contrib.auth.models import User
from .forms import NameForm
from django.urls import reverse
from django.contrib import messages
from .models import AppointmentInfo

import datetime


# Create your views here.
def profileShowing(request,*args,**kwargs):
    current_user = request.user.username
    u = User.objects.get(username=current_user)
    id = u.userprofileinfo.id
    object = UserProfileInfo.objects.get(pk=id)
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        u.username = username
        u.email = email
        u.save()
        object.registration_number = request.POST['reg_no']
        object.hall_name = request.POST['hall']
        object.department_name = request.POST['dept_name']
        object.admission_year = request.POST['addmission_year']
        object.phone_number = request.POST['phone_no']
        object.blood_group = request.POST['blood_grp']
        object.save()
        messages.success(request, 'Your profile has been updated successfully!')
        return HttpResponseRedirect(reverse('second'))
    else:
        contex = {
        'obj':u
        }
        return render(request,'MyProfile/my_profile.html',contex)


def appointmet_view(request,*args,**kwargs):

    if request.method == "POST":
        current_user = request.user.username
        u = User.objects.get(username=current_user)
        object = AppointmentInfo()
        object.username=current_user
        object.registration_number=u.userprofileinfo.registration_number
        object.blood_group = u.userprofileinfo.blood_group
        object.date_of_birth=u.userprofileinfo.date_of_birth
        date = request.POST['date']
        phone = request.POST['phone_no']
        description = request.POST['description']
        object.appointment_date=date
        object.phone_number=phone
        object.disease_description=description
        object.gender = u.userprofileinfo.gender
        object.save()
        contex = {
            'date':date,
            'phone':phone,
            'description':description
        }
        messages.success(request, 'Appointment has been successful! Please bring the Medical Healt Card with you')
        return HttpResponseRedirect(reverse('home'))
    else:
        return render(request,'MyProfile/appointment.html')

def appointment_list_view(request,*args,**kwargs):
    list = AppointmentInfo.objects.order_by('appointment_date')
    today_date = datetime.date.today()
    i='yes'
    return render(request,'MyProfile/appointment_list.html',{'list':list,'i':i})

def today_appointment_view(request, *args,** kwargs):
    today_date = datetime.date.today()
    list2 = AppointmentInfo.objects.filter(appointment_date=today_date)
    i = 'no'
    return render(request, 'MyProfile/appointment_list.html', {'list': list2, 'i': i})