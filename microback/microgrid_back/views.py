# # views.py
# #from django.shortcuts import render
# #from .models import Measurements

# #def print_measurements(request):
#     # Query the database to retrieve data from Measurements
# #    measurements = Measurements.objects.all()
    
#     # Print the data
# #    for measurement in measurements:
# #        print(f"Voltage: {measurement.voltage}, Time: {measurement.time}")
    
# #    return render(request, 'measurements.html', {'measurements': measurements})
# # microback/micro_back/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
from .models import MeasurementsOne
from .models import MeasurementsTwo,MeasurementsFive,MeasurementsThree, MeasurementsFour, MeasurementsSix
@csrf_exempt
def hello_world(request):
    return HttpResponse("hello world")

# View to fetch all measurements

@csrf_exempt
def measurements_by_sensor_id(request, table_no, sensor_id):
    if request.method == 'GET':
        if table_no == 1:
            measurements = MeasurementsOne.objects.filter(sensor_id=sensor_id)
        elif table_no == 2:
            measurements = MeasurementsTwo.objects.filter(sensor_id=sensor_id)
        elif table_no == 3:
            measurements = MeasurementsThree.objects.filter(sensor_id=sensor_id)
        elif table_no == 4:
            measurements = MeasurementsFour.objects.filter(sensor_id=sensor_id)
        elif table_no == 5:
            measurements = MeasurementsFive.objects.filter(sensor_id=sensor_id)
        elif table_no == 6:
            measurements = MeasurementsSix.objects.filter(sensor_id=sensor_id)    
        else:
            return JsonResponse({'error': 'Invalid parameters'}, status=400)
        
        data = [{'voltage': measurement.voltage, 'time': measurement.time} for measurement in measurements]
        
        return JsonResponse({'measurements': data})



