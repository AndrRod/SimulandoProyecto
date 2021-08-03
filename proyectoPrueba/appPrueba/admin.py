from appPrueba.models import deudores
from django.contrib import admin


# Register your models here.

class modelDeudores(admin.ModelAdmin):
    list_display = ("nombre", "dni", "expediente")
    
admin.site.register(deudores, modelDeudores)