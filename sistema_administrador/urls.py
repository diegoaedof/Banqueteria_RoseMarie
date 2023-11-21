from django.urls import path
from . import views

urlpatterns = [
    path('panel_administracion', views.panel_administracion, name='panel_administracion'),
    path('productos', views.productos, name='productos'),
    path('productos_stock', views.productos_stock, name='productos_stock'),
    path('productos_add', views.productos_add, name='productos_add'),
    path('mi_perfil', views.mi_perfil, name='mi_perfil'),
    path('factura', views.factura, name='factura'),
    path('cotizaciones', views.cotizaciones, name='cotizaciones'),
    path('agenda', views.agenda, name='agenda'),
    path('clientes', views.clientes, name='clientes'),
    path('servicios', views.servicios, name='servicios'),
    path('servicios_add', views.servicios_add, name='servicios_add'),
    path('contactar', views.contactar, name='contactar'),
    path('contactar/<int:id>/', views.contactar, name='contactar'),
    path('agendar', views.agendar, name='agendar'),
]