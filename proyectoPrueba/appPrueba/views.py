from django.shortcuts import render

# Create your views here.

def buscar(request):
    return render(request, "busqueda_deudor.html")