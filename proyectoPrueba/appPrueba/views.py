from django.http.response import HttpResponse

from django.shortcuts import render
from appPrueba.models import deudores



# Create your views here.

def buscar(request):
    return render(request, 'busqueda_deudor.html')



# def resultado_deudores(request):
#     if request.GET['dato']:
#         dni_dato = request.GET['dato']
        
#         dni = deudores.objects.filter(nombre__icontains = dni_dato)
#         return render(request, "resultado_deudores.html", {"dni_dato" : dni_dato, "dni" : dni})
#     else:
#         mensaje = 'No ingreso ningún dato'
    
#     return HttpResponse(mensaje)


def resultado_deudores(request):
  
   if request.GET['dato']:
       
        deudor = request.GET['dato']

        if len(deudor) > 8:
            mensaje = 'La busqueda tiene que contener menos de 8 caracteres'
            
        # incontains sustituye o es como like, nombre es lo que haya en deudor
        else: 
            deudor_nombre = deudores.objects.filter(dni__icontains = deudor)
            #    redirigir Art a otro archivo html
            return render(request, "resultado_deudores.html", {"dni" : deudor_nombre, "dni_dato": deudor})
    
   else:
       mensaje = 'No has introducido nada'
    
   return HttpResponse(mensaje)