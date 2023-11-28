# student/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    roll_number = models.CharField(max_length=10, unique=True)

class Subject(models.Model):
    name = models.CharField(max_length=255)

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    total_marks = models.IntegerField()
