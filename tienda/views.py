from django.shortcuts import render, get_object_or_404
from .models import Producto, Accesorio
from django.db.models import Q
#from carro.carro import Carro


# Create your views here.

def tienda(request):   
    accesorios = Accesorio.objects.all()
    productos = Producto.objects.all()
    if "buscar" in request.GET:
        queryset = request.GET.get("buscar")
        #carro=Carro(request)
       
        
        
        if queryset:                        
            productos = Producto.objects.filter(
                Q(nombre__icontains = queryset) | 
              # Q(accesorios__icontains = queryset) |
                Q(precio__icontains = queryset) 
                
                
            ).distinct()
            # if queryset:
            #     request.GET.get("buscar") == "?buscar=accesorios"
            #     accesorios = Accesorio.objects.all()
                

            

    return render(request, "tienda/tienda.html", {"productos":productos})


def accesorios(request):   
    accesorios = Accesorio.objects.all()
    if "buscar" in request.GET:
        queryset = request.GET.get("buscar")
        #carro=Carro(request)
        
        
        
        if queryset:             
            accesorios = Accesorio.objects.filter(
                Q(nombre__icontains = queryset) | 
            # Q(categoria__icontains = queryset) |
                Q(precio__icontains = queryset)
            ).distinct()
        
        

            

    return render(request, "tienda/accesorio.html", {"accesorios":accesorios})