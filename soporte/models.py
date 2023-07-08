from typing import Any
from django.db import models

# Create your models here.


class tipoMensaje(models.Model):
    mensajeId = models.AutoField(primary_key = True, db_column=" mensajeId")
    descripcion = models.CharField(max_length = 15, null= False)

    def __str__(self):
        return str(
            self.descripcion
        )
    
class ciudad(models.Model):
    ciudadId = models.AutoField(primary_key = True, db_column=" ciudadId")
    descripcion = models.CharField(max_length = 15, null= False)

    def __str__(self):
        return str(
            self.descripcion
        )
    

class feedback(models.Model):
    nombre=models.CharField(max_length=50)
    correo=models.CharField(max_length=30)
    mensajeId = models.ForeignKey('tipoMensaje',on_delete=models.CASCADE, null= True)
    ciudadId = models.ForeignKey('ciudad',on_delete=models.CASCADE, null= True)
    comentario=models.CharField(max_length=400)
    
    #para que en la pag admin muestre nombre y tipo de mensaje
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.mensajeId)
    



