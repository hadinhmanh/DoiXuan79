from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path

app_name = "doixuan79"

urlpatterns = [
    

    path("", views.index, name="index"),
] 