from django.db import models
from django.db.models.base import Model

# Create your models here.

class deudores(models.Model):
    nombre = models.CharField(max_length=20)
    dni = models.CharField(max_length= 8)
    expediente = models.IntegerField(help_text="Ingresar solo cantidad de expedientes que está afectado")
    fecha_actualizacion_datos = models.DateField(blank=True, null=True)
    regularizo_situacion = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f'El Sr./Sra. {self.nombre}, dni: {self.dni} se encuentra afectado en {self.expediente} expedienes, ultima fecha de actualización de datos: {self.fecha_actualizacion_datos}, regularizo situación: {"SI" if self.regularizo_situacion else "NO"}'