from django.db import models

# Create your models here.


class Student(models.Model):
    student_name = models.CharField(max_length = 100)
    student_email = models.EmailField()
    address = models.CharField(max_length = 100)
    age = models.IntegerField()

    def __str__(self):
        return self.student_name
    

    

