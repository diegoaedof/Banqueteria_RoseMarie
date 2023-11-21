from django.shortcuts import render, redirect
from .forms import ProductoForm, ServicioForm
from .models import Producto, Servicio
from gestor_cotizaciones.models.contacto import Mensaje
from publico.forms import MensajeForm

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
    form = MensajeForm(instance=mens)
    return render(request, 'contactar.html', {'id': solicitud_id, 'form': form})


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