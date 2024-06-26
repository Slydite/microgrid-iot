import graphene
from graphene_django.types import DjangoObjectType
from .models import Measurements

class MeasurementsType(DjangoObjectType):
    class Meta:
        model = Measurements

class Query(graphene.ObjectType):
    all_measurements = graphene.List(MeasurementsType)

    def resolve_all_measurements(self, info):
        return Measurements.objects.all()

class CreateMeasurement(graphene.Mutation):
    class Arguments:
        voltage = graphene.Float(required=True)

    measurement = graphene.Field(MeasurementsType)

    def mutate(self, info, voltage):
        measurement = Measurements.objects.create(voltage=voltage)
        return CreateMeasurement(measurement=measurement)

class UpdateMeasurement(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        voltage = graphene.Float(required=True)

    measurement = graphene.Field(MeasurementsType)

    def mutate(self, info, id, voltage):
        measurement = Measurements.objects.get(pk=id)
        measurement.voltage = voltage
        measurement.save()
        return UpdateMeasurement(measurement=measurement)

class DeleteMeasurement(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        measurement = Measurements.objects.get(pk=id)
        measurement.delete()
        return DeleteMeasurement(ok=True)

class Mutation(graphene.ObjectType):
    create_measurement = CreateMeasurement.Field()
    update_measurement = UpdateMeasurement.Field()
    delete_measurement = DeleteMeasurement.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
