from django.shortcuts import render

from django.db.models import Sum

from .models import Subject, Course


# Create your views here.

# Returns Home Page
def index(request):
    return render(request, 'msgrad_app/index.html')

def dashboard(request):
    """Shows list of courses on subject page"""
    subjects = Subject.objects.all()
    context = {'subjects': subjects,
            }

    return render(request, 'msgrad_app/dashboard.html', context)

    
def subject(request, subject_id):
    """Shows list of courses on subject page"""
    subject = Subject.objects.get(id=subject_id)
    courses = subject.course_set.all()

    context = {'subject': subject,
               'courses': courses,
            }
    return render(request, 'msgrad_app/subject.html', context)


