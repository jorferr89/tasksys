from django.urls import path
from apps.proyectos.views import *

app_name = 'app.proyectos'

urlpatterns = [
    path('', ProyectosListView.as_view(), name='proyectos'),
]