from django.urls import path
from . import views

urlpatterns = [
    path('panel_administracion', views.panel_administracion, name='panel_administracion'),
    path('productos', views.productos, name='productos'),
    path('mi_perfil', views.mi_perfil, name='mi_perfil'),
    path('factura', views.factura, name='factura'),
    path('cotizaciones', views.cotizaciones, name='cotizaciones'),
    path('agenda', views.agenda, name='agenda'),
    path('clientes', views.clientes, name='clientes'),
    path('contactar', views.contactar, name='contactar'),
    path('contactar/<int:id>/', views.contactar, name='contactar'),
]