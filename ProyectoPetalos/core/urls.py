from django.contrib import admin
from django.urls import path,include #agregar libreria "include"
from .views import *

urlpatterns = [
    path('',index,name='HOME'), #renderizar pag index
    path('galeria/',galeria,name='GALE'),
    path('formulario/',formulario,name='FORMU'),
    path('quien_somos/',quienes_somos,name='QUIEN'),
    path('cerrar_sesion',cerrar_sesion,name='CERRAR'),
    path('eliminar_flor/<id>/',eliminar_flor,name='ELIMINAR'),
    path('login/',login,name='LOGIN'),
    path('login_iniciar/',login_iniciar,name='LOGIN_INICIAR'),
    path('cerrar_sesion/',cerrar_sesion,name='CERRAR_SESION'),
]