from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request,*args , **kwargs):
    print(request.user)
    #return HttpResponse("<h1> hello world! </h1>")
    return render(request,'home.html',{})

def second_view(request,*args , **kwargs):
    print(request.user)
    contex = {
        "user_name" : "this is user name",
        "my_list"   : [10,20,30,40]
    }
    return render(request,'second.html',contex)