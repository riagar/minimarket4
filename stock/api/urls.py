from django.urls import path, include
from . import views
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'inventario', views.InventarioViewSet)
router.register(r'proveedores', views.ProveedorViewSet)

urlpatterns = [
    path('', views.api_home, name='api-home'),
    path('docs/', views.api_docs, name='api-docs'),
    path('endpoints/', views.api_endpoints, name='api-endpoints'),
    path('api_detalle/', views.api_detalle, name='api-detalle'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),  # Incluye las URLs de autenticación de DRF
]