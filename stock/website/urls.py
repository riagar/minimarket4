from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # URL para la página de inicio
    path('about/', views.about, name='about'), # URL para el about
    path('stock', views.stock, name='stock'),
]