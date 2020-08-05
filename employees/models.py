import datetime

from django.db import models
from django.utils import timezone


class Employee(models.Model):
    name = models.CharField(max_length=200)
    employee_id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'{self.name}'


class BioData(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    age = models.IntegerField()
    sex = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.employee.name}'


class Payroll(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    salary = models.FloatField()

    def __str__(self):
        return f'{self.employee.name}'
