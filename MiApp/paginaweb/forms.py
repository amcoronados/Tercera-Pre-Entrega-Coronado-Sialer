from django import forms
from paginaweb.models import cliente, producto, delivery

class formulario_cliente(forms.Form):
  nombre = forms.CharField(max_length=70)
  dni = forms.CharField(max_length=8)
  email = forms.EmailField()
  edad = forms.IntegerField()

class formulario_producto(forms.Form):
    tipo_producto = forms.CharField(max_length=100)
    marca = forms.CharField(max_length=100)
    cantidad = forms.IntegerField()

class formulario_delivery(forms.Form):
    direccion = forms.CharField(max_length=200)


