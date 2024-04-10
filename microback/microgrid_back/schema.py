# import graphene
# from graphene import ObjectType, Field
# from graphene_django.types import DjangoObjectType
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import MeasurementsOne
# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync

# # Define GraphQL types for Django models
# class MeasurementOneType(DjangoObjectType):
#     class Meta:
#         model = MeasurementsOne

# # Define a class to handle subscription field
# class Subscription(ObjectType):
#     measurement_subscription = Field(MeasurementOneType, sensor_id=graphene.Int())

#     def resolve_measurement_subscription(self, info, sensor_id):
#         # Subscription logic will be handled by Django Channels
#         pass

# # Register subscription to Django model post_save signal
# @receiver(post_save, sender=MeasurementsOne)
# def send_measurement_update(sender, instance, **kwargs):
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)(
#         f"sensor_{instance.sensor_id}",
#         {
#             'type': 'measurement.update',
#             'measurement': {
#                 'id': instance.id,
#                 'voltage': str(instance.voltage),
#                 'time': instance.time.isoformat()
#             }
#         }
#     )

# # Define the GraphQL Query and Subscription
# class Query(ObjectType):
#     all_measurements_one = graphene.List(MeasurementOneType)

#     def resolve_all_measurements_one(self, info):
#         # Query all MeasurementsOne objects
#         return MeasurementsOne.objects.all()

# schema = graphene.Schema(query=Query, subscription=Subscription)
#your_project/schema.py
import graphene

from microgrid_back.graphql.subscriptions import Subscription


class Query(graphene.ObjectType):
    base = graphene.String()


class Subscription(Subscription):
    pass


schema = graphene.Schema(
    query=Query,
    subscription=Subscription
)
