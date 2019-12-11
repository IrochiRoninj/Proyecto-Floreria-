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
    path('carrito/',carrito,name='CARRITO'),
    path('carro_compras/<id>',carro_compras,name='AGREGAR_CARRO'),
    path('carro_mas/<id>/', carro_compras_mas,name='CARRO_MAS'),
    path('carro_menos/<id>/',carro_compras_menos,name='CARRO_MENOS'),
    path('grabar_carro/',grabar_carro,name="GRABAR_CARRO"),
    path('formulario2/',formulario2,name='FORMI'),
]