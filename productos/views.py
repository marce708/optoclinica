# Create your views here.

def index(request):
    return render(request, 'productos/index.html')
def producto(request):
    return render(request, 'productos/producto.html')
def productos(request):
    return render(request, 'productos/listadeproductos.html')

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *


def home(request):
	productos = Producto.objects.all()
	total_productos = productos.count()

	context = {'productos':productos, 'total_productos':total_productos}

	return render(request, 'productos/listadeproductos.html', context)

def producto(request):
	productos = Producto.objects.all()

	return render(request, 'productos/producto.html', {'productos':productos})

def listadeproductos(request):
	productos = Producto.objects.all()

	return render(request, 'productos/listadeproductos.html', {'productos':productos})
