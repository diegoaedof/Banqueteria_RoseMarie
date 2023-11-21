from django.shortcuts import render, redirect
from .forms import ProductoForm, ServicioForm
from .models import Producto, Servicio
from gestor_cotizaciones.models.contacto import Mensaje
<<<<<<< HEAD
from gestor_cotizaciones.models.contacto import SolicitudCotizacion
from publico.forms import SolicitudCotizacionForm
=======
>>>>>>> develop
from publico.forms import MensajeForm
from django.contrib import messages

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

def contactar(request):
   

    solicitud_id = request.POST.get('solicitud_id')
    mens=Mensaje.objects.get(id=solicitud_id)
    form_soli=SolicitudCotizacionForm(instance=mens)
    return render(request, 'contactar.html', {'id': solicitud_id, 'form': form_soli})

def agendar(request):
    solicitud_id = request.POST.get('id')
    mens=Mensaje.objects.get(id=solicitud_id)
    nombre = request.POST['nombre']
    apellidos = request.POST['apellidos']
    asunto = request.POST['asunto']
    tipo_de_mensaje = request.POST['tipo_de_mensaje']
    email = request.POST['email']
    telefono = request.POST['telefono']
    tipo_de_evento = request.POST['tipo_de_evento']
    cantidad_de_personas = request.POST['cantidad_de_personas']
    servicios = request.POST['servicios']
    fecha = request.POST['fecha']
    print("XXXXXXXXXXXXXXXXXXXXXX")
    print(mens.id)
    repite= SolicitudCotizacion.objects.get(mensaje_ptr_id=solicitud_id)
    if (repite== None ):
        soli=SolicitudCotizacion.objects.create(
        mensaje_ptr_id=solicitud_id,
        nombre=nombre,
        apellidos=apellidos,
        asunto=asunto,
        tipo_de_mensaje=tipo_de_mensaje,
        email=email,
        telefono=telefono,
        tipo_de_evento = tipo_de_evento,
        cantidad_de_personas = cantidad_de_personas,
        servicios = servicios,
        fecha = fecha
    )
    else:
       messages.warning(request, "El código del producto debe tener 5 carácteres")
    return render(request, 'agenda.html')

def agenda(request):
    context= {}
    return render(request, 'agenda.html', context)

def clientes(request):
    context = {}
    return render(request, 'clientes.html', context)

def productos(request):
    context = {}
    return render(request, 'productos.html', context)

def productos_stock(request):
    productos = Producto.objects.all()
    return render(request, 'productos_stock.html', {'productos': productos})

def productos_add(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos_stock')  # Redirect to a success page
    else:
        form = ProductoForm()

    context = {'form': form}
    return render(request, 'productos_add.html', context)

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html',  {'servicios': servicios})

def servicios_add(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicios')  # Reemplaza 'lista_servicios' con el nombre de tu vista de lista de servicios
    else:
        form = ServicioForm()

    return render(request, 'servicios_add.html', {'form': form})