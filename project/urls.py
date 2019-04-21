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
from Pages.views import *
from Product.views import (
    product_create_view,
    )
from Blog.views import article_detail_view

urlpatterns = [
    path('product/', include('Product.urls')),
    path('', home_view, name='home'),
    path('second/', second_view, name='second'),
    path('next_page/', next_page , name='nextPage'),
    path('about_page/', about_page , name='aboutPage'),
    path('create/', product_create_view, name='details'),
    path('article/', article_detail_view, name='article_detail'),
    path('admin/', admin.site.urls),
]
