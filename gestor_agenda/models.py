from django.db import models
from gestor_productos.models import Servicio, Producto

class Evento(models.Model):
    titulo = models.CharField(max_length=50)
    tipo_evento = models.CharField(max_length=30)
    cantidad_personas = models.IntegerField()
    inicio = models.DateTimeField()
    termino = models.DateTimeField()
    # servicios = models.ManyToManyField()
    # productos = models.ManyToManyField()
