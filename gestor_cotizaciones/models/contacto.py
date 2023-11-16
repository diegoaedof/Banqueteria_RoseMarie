from django.db import models


class Mensaje(models.Model):
    opciones_mensaje = [
        ("SC", "Solicitud de Cotización"),
        ("C", "Consulta"),
        ("S", "Sugerencia"),
        ("F", "Felicitaciones")
    ]
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    asunto = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=11)
    tipo_de_mensaje = models.CharField(max_length=2, choices=opciones_mensaje)

    def __str__(self):
        return f"{self.__class__}: {self.nombre} {self.apellidos}"

opciones_evento = [
    ("A", "Matrimonio"),
    ("B", "Cumpleaños"),
    ("C", "Cheese and Wine"),
    ("D", "Gala 4to Medio")
]

# Hereda del modelo Mensaje, por herencia Multi-tabla (django docs).
class SolicitudCotizacion(Mensaje):
    tipo_de_evento = models.CharField(max_length=3, choices=opciones_evento)
    cantidad_de_personas = models.IntegerField()
    servicios = models.CharField(max_length=200)
    fecha = models.DateTimeField()

