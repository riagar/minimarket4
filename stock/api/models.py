from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    fecha_ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_en_stock = models.IntegerField()
    ubicacion_en_tienda = models.CharField(max_length=100)
    fecha_ultima_reposicion = models.DateField()
    nivel_de_reorden = models.IntegerField()

    def __str__(self):
        return f"Inventario de {self.producto.nombre}"

class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=255)
    informacion_contacto = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_proveedor
    
    
