from django.shortcuts import render
from api.models import Categoria, Producto, Inventario, Proveedor  # Importa los modelos desde la aplicación API


# Create your views here.

def home(request):
    return render(request, 'website/home.html')

def stock(request):
    return render(request, 'website/stock.html')

def about(request):
    return render(request, 'website/about.html')


def stock_view(request):
    return render(request, 'stock.html')

def stock_view2(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    inventarios = Inventario.objects.all()
    proveedores = Proveedor.objects.all()
    return render(request, 'website/stock.html', {
        'categorias': categorias,
        'productos': productos,
        'inventarios': inventarios,
        'proveedores': proveedores
    })
    
    
