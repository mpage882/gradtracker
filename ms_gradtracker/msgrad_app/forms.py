from django import forms

from .models import Course

class addCourseForm (forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'credit_amount', 'gpa']
        labels = {'name': 'Course name',
                  'credit_amount': 'Credits',
                  'gpa': 'GPA',
                }
        widgets = {'name': forms.TextInput(attrs={'cols':40}),
                   'credit_amount': forms.TextInput(attrs={'cols':4}),
                   'gpa': forms.TextInput(attrs={'cols':4}),
                }