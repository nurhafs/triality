from django.db import models

# Create your models here.
class Activity(models.Model):
    actname = models.CharField(max_length=30, default='')

class Participant(models.Model):
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE)
    name = models.CharField(max_length=20, default='')
    contact_number = models.CharField(max_length=12, default='')