from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# form code by https://studygyaan.com/django/how-to-create-sign-up-registration-view-in-django

"""--Registration Form--"""
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=100)
    last_name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = ("first_name","last_name","email","username","password1", "password2")

  