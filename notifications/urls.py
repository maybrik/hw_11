from django.contrib import admin
from django.urls import path, include
from notifications import views

urlpatterns = [
    path('reminder', views.send_reminder, name='notification'),
    ]