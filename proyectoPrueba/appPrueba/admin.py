from appPrueba.models import deudores
from django.contrib import admin


# Register your models here.

class modelDeudores(admin.ModelAdmin):
    list_display = ("nombre", "dni", "expediente", "fecha_actualizacion_datos", "regularizo_situacion")
    search_fields = ("dni",)
    list_filter=("fecha_actualizacion_datos",)


    
admin.site.register(deudores, modelDeudores)