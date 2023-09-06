from django.shortcuts import render, HttpResponse
from carro.carro import Carro
from servicios.models import Servicio

# Create your views here.

def home(request):

    carro = Carro(request)
    return render(request, "ProyectoWebApp/home.html")

   
         
def privacidad(request):
    return render(request, "ProyectoWebApp/privacidad.html")


         
def aviso(request):
    return render(request, "ProyectoWebApp/aviso.html")
   

   














