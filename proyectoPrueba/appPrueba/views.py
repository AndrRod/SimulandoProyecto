from django.http.response import HttpResponse

from django.shortcuts import render
from appPrueba.models import deudores



# Create your views here.

def buscar(request):
    return render(request, "busqueda_deudor.html")


def resultado_deudores(request):
    if request.GET['dato']:
        dni_dato = request.GET['dato']
        
        dni = deudores.objects.filter(nombre__icontains = dni_dato)
        return render(request, "resultado_deudores.html", {"dni_dato" : dni_dato, "dni" : dni})
    else:
        mensaje = 'No ingreso ningún dato'
    
    return HttpResponse(mensaje)