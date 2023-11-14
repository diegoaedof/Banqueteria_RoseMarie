from django.shortcuts import render,redirect
from publico.forms import MensajeForm
from gestor_cotizaciones.models.contacto import Mensaje

def index(request):
    form = MensajeForm()
    return render(request, 'index.html',{'form': form})

def form(request):
    form = MensajeForm()
    nombre = request.POST['nombre']
    apellidos = request.POST['apellidos']
    asunto = request.POST['asunto']
    tipo_de_mensaje = request.POST['tipo_de_mensaje']
    email = request.POST['email']
    telefono = request.POST['telefono']

    Mensaje.objects.create(
        nombre=nombre,
        apellidos=apellidos,
        asunto=asunto,
        tipo_de_mensaje=tipo_de_mensaje,
        email=email,
        telefono=telefono
    )
    return render(request, 'index.html',{'form': form})
