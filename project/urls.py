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
from django.conf import settings
from django.conf.urls.static import static

from MyProfile.views import profileShowing
from login_signup import views as login_signup_view
from MyProfile.views import *
from Pages.views import *
from OnlineAdvice.views import *
from PostNotice.views import *

urlpatterns = [

    path('', home_view, name='home'),
    path('second/', second_view, name='second'),
    path('xyz/', profileShowing, name='profile'),
    path('next_page/', next_page , name='nextPage'),
    path('about_page/', about_page , name='aboutPage'),
    path('admin/', admin.site.urls),
    url(r'^login_signup/',include('login_signup.urls')),
    url(r'^logout/$', login_signup_view.user_logout, name='logout'),
    url(r'^my_profile/$',profileShowing,name='my_profile'),
    url(r'^profile/$',profile_view,name='profile'),
    url(r'^online_advice/$', MessageListView.as_view(), name='online_advice'),
    url(r'^new_message/$', MessageCreateView.as_view(), name='new_message'),
    url(r'^show_notice/$', showNotice.as_view(), name='show_notice'),
    url(r'^post_notice/$', postNotice.as_view(), name='post_notice'),
    url(r'^appointment/$', appointmet_view, name='appointment'),
    url(r'^appointment_list/$', appointment_list_view, name='appointment_list'),
    url(r'^today_appointment/$', today_appointment_view, name='today_appointment'),
    url(r'^edit_appointment_with_pk/(?P<pk>\d+)/$', edit_appointment_view, name='edit_appointment_with_pk'),
    url(r'^contacts/$', contact_view, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)