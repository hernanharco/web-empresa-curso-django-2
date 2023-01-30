from django.urls import path
from . import views

urlpatterns = [
    # Paths del core
    path('', views.contact, name='contact'),
]
