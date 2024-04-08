from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from microgrid_back.schema import schema 
from microgrid_back.views import all_measurements


urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path('microgrid_back/', include('microgrid_back.urls')),
    
    
]
