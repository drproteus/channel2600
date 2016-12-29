"""channel2600 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from chan.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^board/([a-z]+)/$', board_index),
    url(r'^board/([a-z]+)/(\d+)/$', board_index),
    url(r'^thread/(\d+)/$', thread),
    url(r'^board/([a-z]+)/new_thread/$', new_thread),
    url(r'^thread/(\d+)/reply/$', reply),
    url(r'^thread/(\d+)/posts/$', full_thread),
]
