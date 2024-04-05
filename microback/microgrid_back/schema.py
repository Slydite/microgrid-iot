import graphene
from graphene import ObjectType, String, Int, List, Field
from graphene_django.types import DjangoObjectType
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MeasurementsOne, MeasurementsTwo, MeasurementsThree, MeasurementsFour, MeasurementsFive, MeasurementsSix

# Define GraphQL types for Django models
class MeasurementOneType(DjangoObjectType):
    class Meta:
        model = MeasurementsOne

class MeasurementTwoType(DjangoObjectType):
    class Meta:
        model = MeasurementsTwo

class MeasurementThreeType(DjangoObjectType):
    class Meta:
        model = MeasurementsThree

class MeasurementFourType(DjangoObjectType):
    class Meta:
        model = MeasurementsFour

class MeasurementFiveType(DjangoObjectType):
    class Meta:
        model = MeasurementsFive

class MeasurementSixType(DjangoObjectType):
    class Meta:
        model = MeasurementsSix

# Define a class to handle subscription field
class Subscription(ObjectType):
    measurement_subscription = Field(MeasurementOneType)

# Define a subscription resolver function
def resolve_measurement_subscription(root, info, sensor_id):
    async def generator():
        async for measurement in MeasurementsOne.objects.filter(sensor_id=sensor_id):
            yield measurement
    return generator()

# Register subscription to Django model post_save signal
@receiver(post_save, sender=MeasurementsOne)
def send_measurement_subscription(sender, instance, **kwargs):
    Subscription.broadcast(payload={"measurement": instance}, group=instance.sensor_id)

# Define the GraphQL Query and Subscription
class Query(ObjectType):
    all_measurements_one = List(MeasurementOneType)

    # Resolver for all_measurements_one
    def resolve_all_measurements_one(root, info):
        # Query all MeasurementsOne objects
        return MeasurementsOne.objects.all()

schema = graphene.Schema(query=Query, subscription=Subscription)
