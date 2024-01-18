from django.shortcuts import render
from paginaweb.models import cliente, producto, delivery
from paginaweb.forms import formulario_cliente
from paginaweb.forms import formulario_producto
#from paginaweb.forms import ClienteForm, CuentaBancariaForm, TransaccionForm

# Create your views here.

def mensaje_inicio(request):
    mensaje_inicio = "Bienvenido a mi paginaweb. Comienza a explorar las funciones."
    return render(request, 'mensaje_inicio.html', {'mensaje': mensaje_inicio})

###########################################################################################
def crear_cliente(request):  
    if request.method=="POST":    
        formulario=formulario_cliente(request.POST)
        if formulario.is_valid():
            #diccionario=formulario.cleaned_data
            #nuevo_cliente=cliente(nombre=diccionario["nombre"], dni=diccionario["dni"], email=diccionario["email"], edad=diccionario["edad"])
            #nuevo_cliente.save()
           return render(request, "ver_cliente.html")
    else:
        formulario = formulario_cliente()       #guardamos la info
        
    return render(request, 'crear_cliente.html', {'formulario': formulario}) 

def ver_cliente(request):
    return render(request, 'ver_cliente.html')

