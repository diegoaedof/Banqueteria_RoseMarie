from django.db import models


#Resolver herencia para el formulario
class MensajeFormulario(models.Model):
    nombre = models.CharField("Nombre del Cliente", max_length=30)
    apellidos = models.CharField("Apellidos del Cliente", max_length=50)
    asunto = models.TextField("Asunto o título del mensaje", max_length=2000)
    tipo_de_mensaje = models.TextChoices("Tipo de Mensaje","SOLICITUD_DE_COTIZACION CONSULTA SUGERENCIA FELICITACIONES")
    email = models.EmailField()
    telefono = models.CharField(max_length=11)

class SolicitudCotizacion(MensajeFormulario):
    tipo_de_evento = models.IntegerChoices("Tipo de Evento", "MATRIMONIO CUMPLEAÑOS GALA_4TO_MEDIO")
    cantidad_de_personas = models.IntegerField()
    servicios = models.CharField(max_length=200)
    productos = models.CharField(max_length=200)
    fechas = models.DateField()




