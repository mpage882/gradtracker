from django.shortcuts import  render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# code reference - https://ordinarycoders.com/blog/article/django-user-register-login-logout

# Create your views here.
def registerUser(request):
    if request.method != 'POST':
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You are now signed up.")
            return redirect("msgrad_app:dashboard")
        else:
            messages.error(request, "Error.Unable to register.")
    context = {"form": form}
    return render(request, "users/register.html", context)

def loginUser(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("msgrad_app:dashboard")
			# else:
			# 	messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")

	form = AuthenticationForm()
	return render(request=request, template_name="users/login.html", context={"form":form})

def logoutUser(request):
    logout(request)
    #messages.info(request, "You are now logged out.")
    return render (request, "users/logout.html")