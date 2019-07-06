"""CKG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from User import views

urlpatterns = [
    url(r'^app/user/index/', views.index),
    url(r'^app/user/getcode/',views.getcode),
    url(r'^app/user/check_vcode/',views.check_vcode),
    url(r'^app/user/get_profile/',views.get_profile),
    url(r'^app/user/set_profile/',views.set_profile),
    url(r'^app/user/upload_avatar/',views.upload_avatar),
]
