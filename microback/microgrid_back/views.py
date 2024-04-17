# views.py
#from django.shortcuts import render
#from .models import Measurements

#def print_measurements(request):
    # Query the database to retrieve data from Measurements
#    measurements = Measurements.objects.all()
    
    # Print the data
#    for measurement in measurements:
#        print(f"Voltage: {measurement.voltage}, Time: {measurement.time}")
    
#    return render(request, 'measurements.html', {'measurements': measurements})
# microback/micro_back/views.py

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
        model_mapping = {
            1: MeasurementsOne,
            2: MeasurementsTwo,
            3: MeasurementsThree,
            4: MeasurementsFour,
            5: MeasurementsFive,
            6: MeasurementsSix
        }
        if table_no in model_mapping:
            model_class = model_mapping[table_no]
            measurements = model_class.objects.filter(sensor_id=sensor_id).order_by('-time')[:1000]
            data = [{'voltage': measurement.voltage, 'time': measurement.time} for measurement in measurements]
            return JsonResponse({'measurements': data})
        else:
            return JsonResponse({'error': 'Invalid parameters'}, status=400)



