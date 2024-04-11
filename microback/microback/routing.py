# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from django.urls import path
# from microgrid_back.consumers import GraphQLSubscriptionConsumer

# application = ProtocolTypeRouter({
#     'websocket': AuthMiddlewareStack(
#         URLRouter([
#             path('ws/microgrid_back/', GraphQLSubscriptionConsumer.as_asgi()),
#         ])
#     ),
# })
from django.urls import path
from microgrid_back.consumers import consumers

websocket_urlpatterns = [
    path('ws/some_path/', consumers.as_asgi()),
]

