from django.db import forms

class Articulos_camping_FM(forms.Form):
    tipo_articulo = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)
    ano = forms.IntegerField()

class Articulos_hidratación_FM(forms.Form):
    tipo_articulo = forms.CharField(max_length=3)
    marca = forms.CharField(max_length=3)
    litros = forms.IntegerField()

class Articulos_alimentacion_FM(forms.Form):
    tipo_alimento = forms.CharField(max_length=10)
    marca = forms.CharField(max_length=4)