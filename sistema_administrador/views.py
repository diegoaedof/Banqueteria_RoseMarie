from django.shortcuts import render
from gestor_cotizaciones.models.contacto import Mensaje


def panel_administracion(request):
    context= {}
    return render(request, 'panel_administracion.html' , context)

def mi_perfil(request):
    context= {}
    return render(request, 'mi_perfil.html', context)

def factura(request):
    context= {}
    return render(request, 'factura.html', context)

def cotizaciones(request):
    solicitudes =Mensaje.objects.all()
    context= {}
    return render(request, 'cotizaciones.html',{'solicitudes': solicitudes})

def agenda(request):
    context= {}
    return render(request, 'agenda.html', context)

def clientes(request):
    context = {}
    return render(request, 'clientes.html', context)

def productos(request):
    context = {}
    return render(request, 'productos.html', context)


