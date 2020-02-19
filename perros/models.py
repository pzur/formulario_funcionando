from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15,null=True)
    direccion = models.CharField(max_length=15, null=True)






# Create your models here.
