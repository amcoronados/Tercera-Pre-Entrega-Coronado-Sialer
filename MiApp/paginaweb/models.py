from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class cliente(models.Model):
    nombre = models.CharField(max_length=70)
    dni = models.CharField(max_length=8)
    email = models.EmailField()
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class producto(models.Model):
    tipo_producto = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Producto seleccionado: {self.producto.tipo_producto}"
    
class delivery(models.Model):
    direccion = models.CharField(max_length=200)


