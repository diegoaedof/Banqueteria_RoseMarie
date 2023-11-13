from django.db import models


class Mensaje(models.Model):
    opciones_mensaje = [
        "Solicitud de Cotización",
        "Consulta",
        "Sugerencia",
        "Felicitaciones"
    ]
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    asunto = models.TextField(max_length=2000)
    email = models.EmailField()
    telefono = models.CharField(max_length=11)
    tipo_de_mensaje = models.CharField(max_length=len(opciones_mensaje[0]), choices=opciones_mensaje)

    def __str__(self):
        return f"{self.__class__}: {self.nombre} {self.apellidos}"


# Hereda del modelo Mensaje, por herencia Multi-tabla (django docs).
class SolicitudCotizacion(Mensaje):
    opciones_evento = [
        "Matrimonio",
        "Cumpleaños",
        "Cheese and Wine",
        "Gala 4to Medio"
    ]
    tipo_de_evento = models.CharField(max_length=len(opciones_evento[2]), choices=opciones_evento)
    cantidad_de_personas = models.IntegerField()
    servicios = models.CharField(max_length=200)
    fecha = models.DateTimeField()

