# models.py
from django.db import models

class Driver(models.Model):
    license_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

class Car(models.Model):
    license_plate = models.CharField(max_length=10, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    year = models.IntegerField()
    registration_date = models.DateField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

class Violation(models.Model):
    violation_code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    fine_range = models.CharField(max_length=50)
    warning = models.BooleanField()
    license_suspension_range = models.CharField(max_length=50)

class Penalty(models.Model):
    violation = models.ForeignKey(Violation, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    violation_date = models.DateField()
    violation_time = models.TimeField()
    area = models.CharField(max_length=50)
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2)
    fine_paid = models.BooleanField()
    license_suspension = models.IntegerField()
    base_amount = models.DecimalField(max_digits=10, decimal_places=2)
    officer = models.ForeignKey('Officer', on_delete=models.CASCADE)

class Officer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    badge_number = models.CharField(max_length=20, unique=True)
