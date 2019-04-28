from django.shortcuts import render

# Create your views here.
def profileShowing(request):
    # print(user.username)
    return render(request,'MyProfile/my_profile.html')