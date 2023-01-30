from django.urls import path
from . import views

urlpatterns = [
    # Paths del core
    path('', views.services, name='services'),
]
