from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", views.index),
    path("login/", views.login_page),
    path("dashboard/", views.dashboard)
]
