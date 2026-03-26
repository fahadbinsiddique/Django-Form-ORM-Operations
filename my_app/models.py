from django.db import models


# Create your models here.
class Student_Model(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Course_Model(models.Model):
    title = models.CharField(max_length=100)
    fee = models.IntegerField()
    duration = models.IntegerField()
    instructor_name = models.CharField()

    def __str__(self):
        return self.title


class Enrollment_Model(models.Model):
    student_name = models.CharField(max_length=100)
    course_title = models.CharField(max_length=50)
    status = models.CharField(max_length=12)

    def __str__(self):
        return self.student_name
