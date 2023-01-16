from django.db import models
from datetime import datetime
from apps.parametros.models import Prioridad
from apps.empleados.models import Empleado

# Create your models here.

class Proyecto(models.Model):
    nombre = models.TextField(verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripcion')
    fecha_limite = models.DateField(verbose_name='Fecha Limite')
    prioridad = models.ForeignKey(Prioridad, models.DO_NOTHING, verbose_name='Prioridad')
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING, verbose_name='Empleado')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'proyectos'
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['fecha_limite']

