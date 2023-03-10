from django.urls import path, include
from . import views

urlpatterns = [
    path('login_empleado/', views.login_empleado, name="login"),
]