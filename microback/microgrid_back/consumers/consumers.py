# import asyncio
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.db import database_sync_to_async
# from microgrid_back.models import MeasurementsOne
# class GraphQLSubscriptionConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#     async def disconnect(self, close_code):
#         pass

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         sensor_id = data.get('sensor_id')

#         if sensor_id is not None:
#             await self.subscribe(sensor_id)

#     async def subscribe(self, sensor_id):
#         while True:
#             measurements = await self.get_measurements(sensor_id)
#             await self.send(text_data=json.dumps({'measurements': measurements}))

#             # Sleep for some time before fetching new data (adjust as needed)
#             await asyncio.sleep(5)

#     @database_sync_to_async
#     def get_measurements(self, sensor_id):
#         measurements = MeasurementsOne.objects.filter(sensor_id=sensor_id)
#         return [{'id': measurement.id, 'voltage': measurement.voltage, 'time': measurement.time} for measurement in measurements]
from channels.generic.websocket import AsyncWebsocketConsumer

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Your connect logic
        await self.accept()

    async def disconnect(self, close_code):
        # Your disconnect logic
        pass

    async def receive(self, text_data=None, bytes_data=None):
        # Your receive logic
        pass
