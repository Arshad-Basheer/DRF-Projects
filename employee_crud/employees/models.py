from django.db import models
from django.db.models import ImageField
from django.db.models.fields import DateField


# Create your models here.
class Employee(models.Model):
    empid = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    place = models.CharField(max_length=30)
    gender_choices = [ ('male','Male'),('female','Female') ]
    gender = models.CharField(max_length=20,choices=gender_choices)
    salary = models.IntegerField()
    joining_date = models.DateField()
    designation = models.CharField()
    image = models.ImageField(upload_to='employees',null=True)