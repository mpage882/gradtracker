from django.db import models

# Create your models here.
class Subject(models.Model):
    # subject name - Arts, English, etc.
    name = models.CharField(max_length=80)
    # total credits for one subject
    credit_amount = models.IntegerField()

    def __str__(self):
        # "Returns a string representation of the model"
        return self.name


class Course(models.Model):
    # links to Subject subject
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    credit_amount = models.IntegerField()
    gpa = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    
    def __str__(self):
        # "Returns a string representation of the model"
        return self.name