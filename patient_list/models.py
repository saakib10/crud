from django.db import models

class PatientDetails(models.Model):
    serial = models.IntegerField()
    name = models.TextField(max_length=30)
    doctor = models.TextField(max_length=30)
