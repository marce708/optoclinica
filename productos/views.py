from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'productos/index.html')

def imagen(request):
    return render(request, 'productos/imagen.html')

def productos(request):
    return render(request, 'productos/productos.html')
