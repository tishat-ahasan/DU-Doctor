from django.http import HttpResponseRedirect
from django.shortcuts import render
from login_signup.models import UserProfileInfo
from django.contrib.auth.models import User
from .forms import NameForm
from django.urls import reverse
from django.contrib import messages


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
