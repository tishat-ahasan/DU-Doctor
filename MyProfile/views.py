from django.shortcuts import render

# Create your views here.
def profileShowing(request):
    return render(request,'MyProfile/my_profile.html')