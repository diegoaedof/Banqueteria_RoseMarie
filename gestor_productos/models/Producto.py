from django.db import models


class Producto(models.Model):
    LISTA_UNIDADES_DE_MEDIDA = [
        ("Kg", "Kilogramos"),
        ("u.", "unidades"),
        ("g", "gramos"),
        ("L", "Litros"),
        ("ml", "mililitros")
    ]
    nombre = models.CharField("Nombre del producto", max_length=100)
    unidad_de_medida = models.CharField(max_length=2, choices=LISTA_UNIDADES_DE_MEDIDA)
    stock = models.FloatField()
    proveedor = models.CharField("Nombre de proveedor", blank=True, max_length=30)
    precio_venta_unidad = models.FloatField()

    def __str__(self):
        return self.nombre
