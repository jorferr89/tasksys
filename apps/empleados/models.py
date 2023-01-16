from django.db import models
from apps.parametros.models import Rol

# Create your models here.

class Empleado(models.Model):
    apellidos = models.TextField(verbose_name='Apellidos')
    nombres = models.TextField(verbose_name='Nombres')
    dni = models.PositiveIntegerField(verbose_name='DNI', unique=True)
    rol = models.ForeignKey(Rol, models.DO_NOTHING, verbose_name='Rol')

    def __str__(self):
        return self.apellidos, self.nombres, self.dni

    class Meta:
        db_table = 'empleados'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['apellidos']