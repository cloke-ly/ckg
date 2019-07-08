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
from Social import views as v2

urlpatterns = [
    url(r'^app/user/index/', views.index),
    url(r'^app/user/getcode/',views.getcode),
    url(r'^app/user/check_vcode/',views.check_vcode),
    url(r'^app/user/get_profile/',views.get_profile),
    url(r'^app/user/set_profile/',views.set_profile),
    url(r'^app/user/upload_avatar/',views.upload_avatar),

    url(r'^app/social/rcmd_user/',v2.rcmd_user),
    url(r'^app/social/like/',v2.like),
    url(r'^app/social/super_like/',v2.super_like),
    url(r'^app/social/dislike/',v2.dislike),
    url(r'^app/social/rewind/',v2.rewind),
    url(r'^app/social/show_liked_me/',v2.show_liked_me),
    url(r'^app/social/friend_list/',v2.friend_list),






]
