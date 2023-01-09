from django.shortcuts import render

from .models import Subject

# Create your views here.

# Returns Home Page
def index(request):
    return render(request, 'msgrad_app/index.html')

def dashboard(request):
    """Shows list of subjects and graph"""
    subjects = Subject.objects.order_by('credit_amount')
    context = {'subjects': subjects}
    return render(request, 'msgrad_app/dashboard.html', context)