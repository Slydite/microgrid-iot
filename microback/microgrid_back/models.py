from django.db import models

class Measurements(models.Model):
    voltage = models.DecimalField(max_digits=5, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Voltage: {self.voltage}, Time: {self.time}"
