from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from microgrid_back import consumers

application = ProtocolTypeRouter({
    # ...
    'websocket': URLRouter([
        path('ws/sensor/', consumers.SensorConsumer),
    ]),
    # ...
})