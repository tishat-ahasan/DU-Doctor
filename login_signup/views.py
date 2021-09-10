# login_signup/views.py
from django.contrib import messages
from django.shortcuts import render
from login_signup.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request,'login_signup/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('second'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

         # print(user_form.pass)
        username = request.POST.get('username')
        password = request.POST.get('password2')
        gender = request.POST.get('gender')
        print(username)
        print(password)
        print(gender)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            print(user.password)
            user.set_password(password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
            return render(request,'index.html',{})
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'login_signup/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                messages.success(request, 'Login Successful!')
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.success(request, 'Your account was inactive.')
                return HttpResponseRedirect(reverse('home'))
        else:
            messages.success(request, 'Invalid Password!')
            return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, 'login_signup/login.html', {})