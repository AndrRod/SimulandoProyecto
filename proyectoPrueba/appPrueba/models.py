from django.db import models
from django.db.models.base import Model

# Create your models here.

class deudores(models.Model):
    nombre = models.CharField(max_length=20)
    dni = models.IntegerField()
    expediente = models.IntegerField()
    def __str__(self):
        return f'El Sr./Sra. {self.nombre}, dni: {self.dni} se encuentra afectado en {self.expediente} expedienes'