from django.shortcuts import render, redirect, get_object_or_404

from .models import Subject, Course, Student

from .forms import addCourseForm

from django.contrib.auth.decorators import login_required

from django.db.models import Sum,Q
from django.http import Http404



# Create your views here.

# Returns Home Page
def index(request):
    return render(request, 'msgrad_app/index.html')

@login_required
def dashboard(request):
    """Shows list of subjects on dashboard page"""
    subjects = Subject.objects.all().order_by('id').annotate(studentCredits=Sum('course__credit_amount', 
        filter=Q(course__student_id=request.user)))
    courses = Course.objects.filter(student=request.user)
    totalCredits = 0 
    requiredCredits = 0 

    for subject in subjects:
        requiredCredits += subject.credit_amount

    for course in courses:
        totalCredits += course.credit_amount
 
    missingCredits = requiredCredits - totalCredits
    data = [totalCredits, missingCredits]
    labels = ['Your Credits', 'Missing Credits']
    
    context = {'subjects': subjects,
                'courses': courses,
                'totalCredits': totalCredits,
                'requiredCredits': requiredCredits,
                'labels': labels,
                'data': data
               }
    return render(request, 'msgrad_app/dashboard.html', context)


@login_required
def subject(request, subject_id):
    """Shows list of courses on subject page"""
    subject = Subject.objects.get(id=subject_id)
    courses = subject.course_set.filter(student=request.user).order_by('-id')
    totalCredits = courses.aggregate(total=Sum('credit_amount'))
    #print(totalCredits)
    context = {'subject': subject,
               'courses': courses,
               'totalCredits': totalCredits,
            #    'student':student
            }
    return render(request, 'msgrad_app/subject.html', context)


# Adds course to subject
@login_required
def add_course(request, subject_id):
    subject = Subject.objects.get(id=subject_id)

    if request.method != 'POST':
        form = addCourseForm()
    else:
        form = addCourseForm(data=request.POST)

        if form.is_valid():
            add_course = form.save(commit=False)
            add_course.subject = subject
            add_course.owner = request.user
            add_course.student_id = request.user.id
            add_course.save()
            return redirect('msgrad_app:subject', subject_id=subject_id)
    
    context = {'subject': subject,
               'form': form,
            }
    return render(request, 'msgrad_app/add_course.html', context)


# Allows user to edit course
@login_required
def edit_course(request, course_id):
    course = Course.objects.get(id=course_id)
    subject = course.subject
    if course.owner != request.user:
        raise Http404

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
@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    subject = course.subject
    context = {'course': course, 'subject': subject}

    if request.method != 'POST':
        return render(request, 'msgrad_app/delete_course.html', context)
    
    else:
        course.delete()
        #messages.success(request, 'Course is now deleted.')
        return redirect('msgrad_app:subject', subject_id=subject.id)

    
