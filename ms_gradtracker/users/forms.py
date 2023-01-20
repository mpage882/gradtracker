from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# form code by: https://ordinarycoders.com/blog/article/django-user-register-login-logout

"""--Registration Form--"""
class RegistrationForm(UserCreationForm):
    firstName = forms.CharField(required=True, max_length=100, label="First Name")
    lastName = forms.CharField(required=True, max_length=100, label="Last Name")
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = ("firstName","lastName","email",
        "username","password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        # Note - User has first_name, last_name, & email
        #  so you will be storing your vars to them.
        user.first_name = self.cleaned_data['firstName']
        user.last_name = self.cleaned_data['lastName']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    

  