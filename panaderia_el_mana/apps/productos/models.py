from django.db import models

# Create your models here.

class Producto(models.Model):
    CATEGORIA_PRODUCTO = [
        ('PANIFICACION', 'Panificación'),
        ('PASTELERIA', 'Pastelería'),
    ]
    ESTADO_PRODUCTO = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo')
    ]

    id_producto = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    categoria = models.CharField(max_length=30, choices=CATEGORIA_PRODUCTO)
    stock = models.PositiveIntegerField(null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    estado = models.CharField(choices=ESTADO_PRODUCTO, default='ACTIVO')
    
    def __str__(self):
        return f"id:{self.id_producto} - producto: {self.descripcion} - precio: $ {self.precio}"