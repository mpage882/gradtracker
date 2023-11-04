from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


# Create your models here.
class Subject(models.Model):
   
    name = models.CharField(max_length=80)
    credit_amount = models.DecimalField(default=0, max_digits=2, decimal_places=1)
    user_credits = models.DecimalField(default=0, max_digits=3, decimal_places=1)
    
   
    def totalCredits(self):
        courses = Course.objects.filter(subject=self)
        credits = 0
        for course in courses:
            credits += course.credit_amount
        self.user_credits = credits
        self.save()
        return self.user_credits

    def __str__(self):
        return self.name


class Course(models.Model):

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100)
    credit_amount = models.DecimalField(default=0, max_digits=2, decimal_places=1)
    gpa = models.DecimalField(default=0, max_digits=3, decimal_places=2)    

    
    def __str__(self):
        return self.name

class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=80)
    firstName = models.CharField(max_length=80)
    lastName = models.CharField(max_length=80)
    totalCredits = models.DecimalField(default=0, max_digits=3, decimal_places=1)
    

    def __str__(self):
        return self.student.username