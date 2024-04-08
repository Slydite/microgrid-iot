# views.py
# from django.shortcuts import render
# from .models import Measurements

# def print_measurements(request):
#     Query the database to retrieve data from Measurements
#    measurements = Measurements.objects.all()
    
#     Print the data
#    for measurement in measurements:
#        print(f"Voltage: {measurement.voltage}, Time: {measurement.time}")
    
#    return render(request, 'measurements.html', {'measurements': measurements})
# microback/micro_back/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import MeasurementsOne
from .schema import schema

# View to fetch all measurements
@csrf_exempt
def all_measurements(request):
    if request.method == 'GET':
        measurements = MeasurementsOne.objects.filter(id=1)
        data = [{'voltage': measurement.voltage, 'time': measurement.time} for measurement in measurements]
        return JsonResponse({'measurements': data})

# View to add a new measurement
@csrf_exempt
def add_measurement(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        voltage = data.get('voltage')
        if voltage is not None:
            measurement = MeasurementsOne.objects.create(voltage=voltage)
            return JsonResponse({'status': 'Measurement added successfully', 'id': measurement.id})
        else:
            return JsonResponse({'error': 'Voltage field is required'}, status=400)
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
# from .schema import schema
# import json

@csrf_exempt
def GraphQLView(request):
    if request.method == 'POST':
        # Execute the GraphQL query
        body = request.body.decode('utf-8')
        data = json.loads(body)
        result = schema.execute(data.get('query'))
        # Convert the result to JSON response
        return JsonResponse(result.data, safe=False)
    else:
        # GraphQL only supports POST method
        return JsonResponse({'error': 'Method not allowed'}, status=405)

# # Optional: If you want to use GraphiQL for testing, you can create a view for it
# graphiql_view = csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))
