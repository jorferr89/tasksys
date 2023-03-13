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
        return self.nombre + " " + self.descripcion + " - Fecha Límite: " + " " + " - Prioridad: " + self.prioridad.nombre + " - Empleado: " + self.empleado.apellidos + " " + self.empleado.nombres


    class Meta:
        db_table = 'proyectos'
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['fecha_limite']

class Tarea(models.Model):
    nombre = models.TextField(verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripcion')
    fecha_limite = models.DateField(verbose_name='Fecha Limite')
    terminada = models.BooleanField(default=False, verbose_name='Terminada')
    proyecto = models.ForeignKey(Proyecto, models.DO_NOTHING, verbose_name='Proyecto')

    def __str__(self):
        return self.nombre + " " + self.descripcion + " - Fecha Límite: " + " " + " - Terminada: " + " "

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        db_table = 'tareas'
        ordering = ['fecha_limite']


