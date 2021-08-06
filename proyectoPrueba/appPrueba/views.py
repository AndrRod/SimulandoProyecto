from django.http.response import HttpResponse

from django.shortcuts import render
from appPrueba.models import deudores



# Create your views here.

def buscar(request):
    return render(request, 'busqueda_deudor.html')



def resultado_deudores(request):
  
   if request.GET['dato']:
       
        deudor = request.GET['dato']

        if not deudor.isdigit():
            mensaje = 'La busqueda tiene que contener solo numeros'
            
        elif len(deudor) > 8 or len(deudor) < 7:
            mensaje = 'La busqueda tiene que contener menos de 8 caracteres y más de 6 caracteres'
        
        else: 
            deudor_nombre = deudores.objects.filter(dni__icontains = deudor)
        
            return render(request, "resultado_deudores.html", {"dni" : deudor_nombre, "dni_dato": deudor})
    
   else:
       mensaje = 'NO SE INTRODUJO NINGUN DATO'
    
   return HttpResponse(mensaje)