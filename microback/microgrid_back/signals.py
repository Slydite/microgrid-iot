# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MeasurementsOne
from .schema import Subscription

@receiver(post_save, sender=MeasurementsOne)
def send_measurement_subscription(sender, instance, **kwargs):
    group_name = f"measurement_subscription_{instance.sensor_id}"
    Subscription.broadcast(payload={'measurement': instance}, group=group_name)
