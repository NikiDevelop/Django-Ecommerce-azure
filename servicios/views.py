from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.

# Cambié servicios por accesorios, más adelante retomaré los servicios
def servicios(request):

    servicios = Servicio.objects.all()
    return render(request, "servicios/servicios.html", {"servicios": servicios})


