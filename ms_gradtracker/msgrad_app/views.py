from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages

from .models import Subject, Course

from .forms import addCourseForm




# Create your views here.

# Returns Home Page
def index(request):
    return render(request, 'msgrad_app/index.html')

def dashboard(request):
    """Shows list of courses on subject page"""
    subjects = Subject.objects.all().order_by('id')
    context = {'subjects': subjects,
            }

    return render(request, 'msgrad_app/dashboard.html', context)


def subject(request, subject_id):
    """Shows list of courses on subject page"""
    subject = Subject.objects.get(id=subject_id)
    courses = subject.course_set.order_by('-id')

    context = {'subject': subject,
               'courses': courses,
            }
    return render(request, 'msgrad_app/subject.html', context)

# Adds course to subject
def add_course(request, subject_id):
    subject = Subject.objects.get(id=subject_id)

    if request.method != 'POST':
        form = addCourseForm()
    else:
        form = addCourseForm(data=request.POST)

        if form.is_valid():
            add_course = form.save(commit=False)
            add_course.subject = subject
            add_course.save()
            return redirect('msgrad_app:subject', subject_id=subject_id)
    
    context = {'subject': subject,
               'form': form,
            }
    return render(request, 'msgrad_app/add_course.html', context)

# Allows user to edit course
def edit_course(request, course_id):
    course = Course.objects.get(id=course_id)
    subject = course.subject

    if request.method != 'POST':
        form = addCourseForm(instance=course)
    else:
        form = addCourseForm(instance=course, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('msgrad_app:subject', subject_id=subject.id)
    
    context = {'subject': subject,
               'form': form,
               'course': course
            }
    return render(request, 'msgrad_app/edit_course.html', context)


# Deletes course
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    subject = course.subject
    context = {'course': course, 'subject': subject}

    if request.method != 'POST':
        return render(request, 'msgrad_app/delete_course.html', context)
    
    else:
        course.delete()
        messages.success(request, 'Course is now deleted.')
        return redirect('msgrad_app:subject', subject_id=subject.id)

    
