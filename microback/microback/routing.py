from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from microgrid_back.consumers import GraphQLSubscriptionConsumer
from microgrid_back import consumers

application = ProtocolTypeRouter({
    # ...
    'websocket': URLRouter([
        path('ws/sensor/', consumers.SensorConsumer),
    ]),
    # ...
})