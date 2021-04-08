from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_number = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.first_name