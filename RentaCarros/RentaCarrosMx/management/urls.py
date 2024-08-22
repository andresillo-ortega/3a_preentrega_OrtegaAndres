from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar-cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('agregar-carro/', views.agregar_carro, name='agregar_carro'),
    path('agregar-renta/', views.agregar_renta, name='agregar_renta'),
    path('buscar/', views.buscar, name='buscar'),
]