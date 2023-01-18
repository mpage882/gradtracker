from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# code reference - https://skolo-online.medium.com/python-django-user-registration-login-logout-custom-styling-c2f2901e162a

# Create your views here.
class UserRegister(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')



