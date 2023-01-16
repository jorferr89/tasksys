from django.db import models

# Create your models here.

# Parámetros del empleado
class Rol(models.Model):
    nombre = models.TextField(verbose_name='Nombre', unique=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'roles'
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['nombre']

# Parámetros del proyecto
class Prioridad(models.Model):
    nombre = models.TextField(verbose_name='Nombre', unique=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'prioridades'
        verbose_name = 'Prioridad'
        verbose_name_plural = 'Prioridades'
        ordering = ['nombre']