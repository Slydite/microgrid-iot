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
from .models import Measurements

# View to fetch all measurements
@csrf_exempt
def all_measurements(request):
    if request.method == 'GET':
        measurements = Measurements.objects.all()
        data = [{'voltage': measurement.voltage, 'time': measurement.time} for measurement in measurements]
        return JsonResponse({'measurements': data})

# View to add a new measurement
@csrf_exempt
def add_measurement(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        voltage = data.get('voltage')
        if voltage is not None:
            measurement = Measurements.objects.create(voltage=voltage)
            return JsonResponse({'status': 'Measurement added successfully', 'id': measurement.id})
        else:
            return JsonResponse({'error': 'Voltage field is required'}, status=400)
