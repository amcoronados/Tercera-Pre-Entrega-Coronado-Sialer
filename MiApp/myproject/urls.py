"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from paginaweb.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("crear_cliente/", crear_cliente),
    path("mensaje_inicio/", mensaje_inicio),
    path("ver_cliente/", ver_cliente),
    path("ver_producto/", ver_cliente),
    #path("crear_producto/", crear_producto),
    #path("ver_producto/", ver_producto),
   # path("crear_delivery/", crear_delivery),
   # path("ver _delivery/", ver_delivery),
]