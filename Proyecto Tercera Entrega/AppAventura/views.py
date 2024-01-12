from django.shortcuts import render
from AppAventura.models import Articulos_camping
from AppAventura.models import Articulos_hidratación
from AppAventura.models import Articulos_alimentacion
from AppAventura.forms import Articulos_camping_FM
from AppAventura.forms import Articulos_hidratación_FM
from AppAventura.forms import Articulos_alimentacion_FM


# Create your views here.
def agregar_articuloscamping(request):  #vista para agregar
    if request.method=="POST":
        info_camping=Articulos_camping_FM(request.POST)
        if info_camping.is_valid():
            dic_camping = info_camping.cleaned_data
            nuevo_camping = Articulos_camping(tipo_articulo=dic_camping["tipo_articulo"], marca=dic_camping["marca"], ano=dic_camping["ano"])
            nuevo_camping.save()
            return render(request, "ver_articuloscamping.html")
    else:
        nuevo_formulario_camping = Articulos_camping_FM()
    return render(request, "crear_articuloscamping.html", {"nuevo_formulario_camping":nuevo_formulario_camping})

def ver_articuloscamping(request):  #vista para ver
    return render(request, "ver_articuloscamping.html")

#################################################################
def agregar_articuloshidratación(request):  #vista para agregar
    if request.method=="POST":
        info_hidratacion=Articulos_hidratación_FM(request.POST)
        if info_hidratacion.isvalid():
            dic_hidratacion = info_hidratacion.cleaned_data
            nuevo_hidratacion = Articulos_hidratación(tipo_articulo=dic_hidratacion["tipo_articulo"], marca=dic_hidratacion["marca"], litros=dic_hidratacion["litros"])
            nuevo_hidratacion.save()
            return render(request, "ver_articuloshidratacion.html")
        else:
            nuevo_formulario_hidratacion = Articulos_hidratación_FM()
        return render(request, "crear_articuloshidratacion.html", {"nuevo_formulario_hidratacion":nuevo_formulario_hidratacion})

def ver_articuloshidratación(request):  #vista para ver
    return render(request, "ver_articuloshidratacion.html")

##################################################################
def agregar_articulosalimentacion(request):  #vista para agregar
    if request.method=="POST":
        info_alimentacion=Articulos_alimentacion_FM(request.POST)
        if info_alimentacion.isvalid():
            dic_alimentacion =info_alimentacion.cleaned_data
            nuevo_alimentacion = Articulos_alimentacion(tipo_alimento=dic_alimentacion["tipo_alimento"], marca=dic_alimentacion["marca"])
            nuevo_alimentacion.save()
            return render(request, "ver_articulosalimentacion.html")
        else:
            nuevo_formulario_alimentacion = Articulos_alimentacion_FM()
        return render(request, "crear_articulosalimentacion.html", {"nuevo_formulario_alimentacion":nuevo_formulario_alimentacion})

def ver_articulosalimentacion(request):  #vista para ver
    return render(request, "ver_articulosalimentacion.html")

