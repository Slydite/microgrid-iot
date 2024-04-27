from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.postgres.fields import ArrayField

class NestedDecimalArrayField(ArrayField):
    def __init__(self, *args, **kwargs):
        kwargs['base_field'] = ArrayField(models.DecimalField(max_digits=5, decimal_places=2), size=2)
        super().__init__(*args, **kwargs)

class MeasurementsOne(models.Model):
    sensor_id = models.PositiveIntegerField()
    voltage = NestedDecimalArrayField()
    time = models.DateTimeField(auto_now_add=True)
    rmsvalue =models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f"Voltage: {self.voltage}, Time: {self.time}"


class MeasurementsTwo(models.Model):
    sensor_id = models.PositiveIntegerField()
    voltage = NestedDecimalArrayField()
    time = models.DateTimeField(auto_now_add=True)
    rmsvalue =models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f"Voltage: {self.voltage}, Time: {self.time}, Sensor ID: {self.sensor_id}"

class MeasurementsThree(models.Model):
    sensor_id = models.PositiveIntegerField()
    voltage = NestedDecimalArrayField()
    time = models.DateTimeField(auto_now_add=True)
    rmsvalue =models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f"Voltage: {self.voltage}, Time: {self.time}, Sensor ID: {self.sensor_id}"
class MeasurementsFour(models.Model):
    sensor_id = models.PositiveIntegerField()
    voltage = NestedDecimalArrayField()
    time = models.DateTimeField(auto_now_add=True)
    rmsvalue =models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f"Voltage: {self.voltage}, Time: {self.time}, Sensor ID: {self.sensor_id}"
class MeasurementsFive(models.Model):
    sensor_id = models.PositiveIntegerField()
    voltage = NestedDecimalArrayField()
    time = models.DateTimeField(auto_now_add=True)
    rmsvalue =models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f"Voltage: {self.voltage}, Time: {self.time}, Sensor ID: {self.sensor_id}"

class MeasurementsSix(models.Model):
    sensor_id = models.PositiveIntegerField()
    voltage = NestedDecimalArrayField()
    time = models.DateTimeField(auto_now_add=True)
    rmsvalue =models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f"Voltage: {self.voltage}, Time: {self.time}, Sensor ID: {self.sensor_id}"
