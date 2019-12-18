#que es un serializador de DJANGO
#bbdd --> datos  --> JSON
#JSON --> datos --> bbdd

from rest_framework import serializers
from .models import Flores

class FloresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flores
        fields = ['name', 'precio', 'descripcion', 'estado', 'stock']