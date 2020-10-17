from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    lecturer = models.CharField(max_length=25)
    sks = models.CharField(max_length=2)
    desc = models.CharField(max_length=200)
    year = models.CharField(max_length=20)
    kls = models.CharField(max_length=10)