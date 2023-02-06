"""web_concurrency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import time
from random import choice
from django.contrib import admin
from django.urls import path

from django.http import HttpResponse


def test1(request):
    return HttpResponse("hello world")


def test2(request):
    tmp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if choice(tmp) >= 9:
        time.sleep(0.5)
    else:
        time.sleep(0.05)

    return HttpResponse("hello world")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("test2/", test2),
]
