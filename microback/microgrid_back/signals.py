# # signals.py
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import MeasurementsOne
# from .schema import Subscription

# @receiver(post_save, sender=MeasurementsOne)
# def send_measurement_subscription(sender, instance, **kwargs):
#     group_name = f"measurement_subscription_{instance.sensor_id}"
#     Subscription.broadcast(payload={'measurement': instance}, group=group_name)
# your_app/signals.py
from django.db.models.signals import post_save, post_delete
from graphene_subscriptions.signals import post_save_subscription, post_delete_subscription

from .models import MeasurementsOne

post_save.connect(post_save_subscription, sender=MeasurementsOne, dispatch_uid="your_model_post_save")
post_delete.connect(post_delete_subscription, sender=MeasurementsOne, dispatch_uid="your_model_post_delete")

# your_app/apps.py
from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'your_app'

    def ready(self):
        import microgrid_back.signals