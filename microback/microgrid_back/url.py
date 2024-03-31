from django.urls import path, include

urlpatterns = [
    path('microgrid_back/', include('microgrid_back.urls'))
]