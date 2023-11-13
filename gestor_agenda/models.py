from django.db import models
from gestor_productos.models import Servicio, Producto

class Evento(models.Model):
    titulo = models.CharField()
    tipo_evento = models.CharField()
    cantidad_personas = models.IntegerField()
    inicio = models.DateTimeField()
    termino = models.DateTimeField()
    servicios = models.ManyToManyField(Servicio)
    productos = models.ManyToManyField(Producto)
