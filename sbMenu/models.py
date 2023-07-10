from django.db import models
from datetime import datetime


# Create your models here.

class hamburguesa(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True)
    historia = models.TextField(blank=True)
    calorias = models.DecimalField(max_digits=8, decimal_places=2)
    proteinas = models.DecimalField(max_digits=8, decimal_places=2)
    carbohidratos = models.DecimalField(max_digits=8, decimal_places=2)
    grasas = models.DecimalField(max_digits=8, decimal_places=2)
    sodio = models.DecimalField(max_digits=8, decimal_places=2)
    foto = models.ImageField(upload_to='hamburguesas/', blank=True, null=True)
    precio = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre
    
class carritoItem(models.Model):
    hamburguesa = models.ForeignKey(hamburguesa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    cantidad = models.IntegerField(default=1)


class compra(models.Model):
    fecha = models.DateTimeField(default=datetime.now)  # Campo de fecha con valor predeterminado de la fecha actual
    total = models.DecimalField(max_digits=8, decimal_places=2)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Compra {self.id}"