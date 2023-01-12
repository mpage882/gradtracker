"""Defines URL patterns for MSGrad_app"""

from django.urls import path

from .import views

app_name = 'msgrad_app'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('subjects/<int:subject_id>/', views.subject, name='subject'),
    path('add_course/<int:subject_id>/', views.add_course, name='add_course'),

]