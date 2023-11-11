from django import forms
from gestor_cotizaciones.models import MensajeFormulario
from gestor_cotizaciones.models import SolicitudCotizacion
from gestor_productos.models.Producto import Producto
from gestor_productos.models.Servicio import Servicio

class MensajeForm(forms.ModelForm):
    class Meta:
        model = MensajeFormulario
        fields = ['nombre', 'apellidos', 'asunto', 'tipo_de_mensaje', 'email', 'telefono']

class SolicitudCotizacionForm(forms.ModelForm):
    class Meta:
        model = SolicitudCotizacion
        fields = ['nombre', 'apellidos', 'asunto', 'tipo_de_mensaje', 'email', 'telefono', 'tipo_de_evento', 'cantidad_de_personas', 'servicios', 'productos', 'fechas']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'unidad_de_medida', 'stock', 'proveedor', 'precio_venta_unidad']

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'unidad_de_medida', 'valor_por_unidad']
