from django.shortcuts import render

# Create your views here.

# Returns Home Page
def index(request):
    return render(request, 'msgrad_app/index.html')