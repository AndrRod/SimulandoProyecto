from django.db import models
from django.db.models.base import Model

# Create your models here.

class deudores(models.Model):
    nombre = models.CharField(max_length=20)
    dni = models.IntegerField()
    expediente = models.IntegerField(help_text="Ingresar solo cantidad de expedientes que está afectado")

    def __str__(self):
        return f'El Sr./Sra. {self.nombre}, dni: {self.dni} se encuentra afectado en {self.expediente} expedienes'