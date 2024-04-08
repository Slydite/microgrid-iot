import graphene
from graphene import Field  # Import Field from graphene module

from graphene_django.types import DjangoObjectType
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MeasurementsOne, MeasurementsTwo, MeasurementsThree, MeasurementsFour, MeasurementsFive, MeasurementsSix
import asyncio

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

async def get_latest_measurement():
    # Fetch the latest measurement asynchronously
    try:
        latest_measurement = await asyncio.to_thread(MeasurementsOne.objects.latest, 'time')
        return latest_measurement
    except MeasurementsOne.DoesNotExist:
        return None

class MeasurementTypeOneSubscription(graphene.ObjectType):
    measurement_one = Field(MeasurementOneType)

    async def resolve_measurement_one(root, info):
        # Your logic to fetch real-time data from MeasurementsOne table goes here
        # For example:
        latest_measurement = await asyncio.to_thread(MeasurementsOne.objects.latest, 'time')
        return latest_measurement

# Assuming you already have Query and Mutation defined in your schema
schema = graphene.Schema(subscription=MeasurementTypeOneSubscription)
