from django.db import models


class Servicio(models.Model):
    LISTA_UNIDADES_DE_MEDIDA = [
        ("DD","Dias"),
        ("hh","Horas"),
        ("u.","unidades")
    ]
    nombre = models.CharField("Nombre del Servicio", max_length = 100, unique=True)
    unidad_de_medida = models.CharField(max_length=2, choices=LISTA_UNIDADES_DE_MEDIDA)
    valor_por_unidad = models.FloatField()

    def __str__(self):
        return self.nombre
