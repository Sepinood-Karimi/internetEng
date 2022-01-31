from django.db import models


# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    create_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    problem = models.CharField(max_length=1000)
    entry_date = models.DateTimeField(auto_now_add=True)
