from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from rest_framework.decorators import action

from .models import Categoria, Producto, Inventario, Proveedor # Ajusta esto según los modelos que tengas en tu aplicación
from .serializers import CategoriaSerializer, ProductoSerializer, InventarioSerializer, ProveedorSerializer

# Create your views here.

class ItemList(APIView):
    def get(self, request):
        data = {"message": "Hello, this is your API!"}
        return Response(data, status=status.HTTP_200_OK)

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    

# Vistas basadas en funciones
def api_home(request):
    categorias = Categoria.objects.all()  # Obtén todos los datos de la categoría
    productos = Producto.objects.all()    # Obtén todos los datos del producto
    inventarios = Inventario.objects.all()  # Obtén todos los datos del inventario
    proveedores = Proveedor.objects.all()  # Obtén todos los datos del proveedor
    return render(request, 'api/api_home.html', {'categorias': categorias, 'productos': productos, 'inventarios': inventarios, 'proveedores': proveedores})

def api_home(request):
    return render(request, 'api/api_home.html')

def api_docs(request):
    return render(request, 'api/api_docs.html')

def api_detalle(request):
    return render(request, 'api/api_detalle.html')

def api_endpoints(request):
    return render(request, 'api/api_endpoints.html')




