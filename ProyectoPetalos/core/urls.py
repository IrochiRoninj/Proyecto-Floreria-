from django.contrib import admin
from django.urls import path,include #agregar libreria "include"
from .views import *

urlpatterns = [
    path('',index,name='HOME'), #renderizar pag index
    path('galeria/',galeria,name='GALE'),
    path('formulario/',formulario,name='FORMU'),
    path('quien_somos/',quienes_somos,name='QUIEN'),
    path('categoria/',categoria,name='CATE'),
    path('caja/',caja,name='CAJA'),
    path('florero/',florero,name='FLOR'),
    path('novia_y_eventos/',novia_y_eventos,name='NYE'),
    path('cerrar_sesion',cerrar_sesion,name='CERRAR'),
]