"""hello_async URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from hello_async.views import index, async_view, sync_view, smoke_some_meats


urlpatterns = [
    path("admin/", admin.site.urls),
    path("async/", async_view),
    path("sync/", sync_view),
    path("smoke_some_meats/", smoke_some_meats),
    path("", index),
]