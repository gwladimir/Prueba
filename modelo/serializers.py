from rest_framework import serializers
from modelo.models import Empleado, Direccion

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Direccion
        fields=('direccionId','direccionPais', 'direccionProvincia', 'direccionCiudad', 'direccionCallle')


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empleado
        fields=('empleadoId', 'empleadoNombre', 'empleadoApellido', 'empleadoEdad','direccion')