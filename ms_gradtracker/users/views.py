from django.shortcuts import render, redirect
from django.contrib import messages 
from .forms import RegistrationForm
from django.contrib.auth  import login

# code reference - https://skolo-online.medium.com/python-django-user-registration-login-logout-custom-styling-c2f2901e162a

# Create your views here.
def register(request):
    '''REGISTRATION FORM'''
    if request.method != 'POST':
        form = RegistrationForm()

    # Create and save form
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, "Account was created.")
            login(new_user)
            return redirect('msgrad_app:index')
    
    context = {'form': form}
    return render(request, 'users/register.html', context)

