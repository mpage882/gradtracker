"""Defines URL patterns for MSGrad_app"""

from django.urls import path

from .import views

app_name = 'msgrad_app'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]