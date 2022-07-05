from statistics import mode
from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    std_number = models.IntegerField()


    TEACHER = (
        ("ahmadi", "Ahmadi"),
        ("abdi", "Abdi"),
        ("bahrami", "Bahrami")
    )
    teacher = models.CharField(max_length=7, null=True, blank=True, choices = TEACHER)