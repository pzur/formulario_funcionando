from django.db import models


class Cliente(models.Model):
    SEXO = (('V','Varon'),('M','Mujer'))
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15,null=True)
    direccion = models.CharField(max_length=15, null=True)
    sexo = models.CharField(max_length=20,choices=SEXO,null=True)
    distrito =models.CharField(max_length=200, null=True)

class Mascota(models.Model):
    SEXO = (('M','Macho'),('H','Hembra'))
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200,null=True)
    raza = models.CharField(max_length=50,null=True)
    edad = models.IntegerField(null=True)
    sexo = models.CharField(max_length=20,choices=SEXO,null=True)
    alergia =models.CharField(max_length=200,null=True)


class Paseador(models.Model):
    SEXO = (('V','Varon'),('M','Mujer'))
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    sexo = models.CharField(max_length=20,choices=SEXO,null=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=15)
    experiencia = models.CharField(max_length=15)
    distrito =models.CharField(max_length=200)




# Create your models here.
