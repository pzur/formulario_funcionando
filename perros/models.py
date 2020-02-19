from django.db import models


class Cliente(models.Model):
    SEXO = (('V','Varon'),('M','Mujer'))
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15,null=True)
    direccion = models.CharField(max_length=15, null=True)
    sexo = models.CharField(max_length=20,choices=SEXO,null=True)
    distrito =models.CharField(max_length=200, null=True)






# Create your models here.
