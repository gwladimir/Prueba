from django.db import models

# Create your models here.


class Direccion(models.Model):
    direccionId = models.AutoField(primary_key=True)
    direccionPais = models.CharField(max_length=300)
    direccionProvincia = models.CharField(max_length=300)
    direccionCiudad = models.CharField(max_length=300)
    direccionCallle = models.CharField(max_length=300)



class Empleado(models.Model):
    empleadoId = models.AutoField(primary_key=True)
    direccion = models.ForeignKey(
        Direccion, on_delete=models.CASCADE, related_name='dirección')
    empleadoNombre = models.CharField(max_length=500)
    empleadoApellido = models.CharField(max_length=500)
    empleadoEdad = models.CharField(max_length=3)


