from django.db import models

# Create your models here.

class Empleado(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]

    id_empleado = models.AutoField(primary_key=True)
    cuit = models.CharField(max_length=8, unique=True)
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    telefonos = models.CharField(max_length=15)
    domicilio = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='activo')

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['apellido', 'nombre']