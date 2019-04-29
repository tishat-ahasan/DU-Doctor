"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url,include

from MyProfile.views import profileShowing
from login_signup import views as login_signup_view
from MyProfile import views as MyProfile_view
from Pages.views import *
from OnlineAdvice.views import *

from Blog.views import article_detail_view

urlpatterns = [

    path('', home_view, name='home'),
    path('second/', second_view, name='second'),
    path('xyz/', profileShowing, name='profile'),
    path('next_page/', next_page , name='nextPage'),
    path('about_page/', about_page , name='aboutPage'),
    path('article/', article_detail_view, name='article_detail'),
    path('admin/', admin.site.urls),
    url(r'^login_signup/',include('login_signup.urls')),
    url(r'^logout/$', login_signup_view.user_logout, name='logout'),
    url(r'^my_profile/$',MyProfile_view.profileShowing,name='my_profile'),
    url(r'^online_advice/$', MessageListView.as_view(), name='online_advice'),
    url(r'^new_message/$', MessageCreateView.as_view(), name='new_message')

]
