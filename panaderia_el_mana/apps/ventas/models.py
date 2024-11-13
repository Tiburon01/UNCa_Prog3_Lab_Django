from django.db import models
from apps.productos.models import Producto 

# Create your models here.

class Empleado(models.Model):
    ESTADO_EMPLEADO = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    ]

    id_empleado = models.AutoField(primary_key=True)
    cuit = models.CharField(max_length=11, unique=True)
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    domicilio = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()
    estado = models.CharField(choices=ESTADO_EMPLEADO, default='Activo')

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['apellido', 'nombre']

class Mayorista(models.Model):
    ESTADO_MAYORISTA = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    ]

    id_mayorista = models.AutoField(primary_key=True)
    cuit = models.CharField(max_length=11, unique=True)
    razon_social = models.CharField(max_length=30)
    direccion= models.CharField(max_length=50)
    telefono= models.CharField(max_length=20)
    email= models.CharField(max_length=50)
    estado=models.CharField(choices=ESTADO_MAYORISTA, default='Activo')

    def __str__(self):
        return self.razon_social
    
# class Producto(models.Model):
#     CATEGORIA_PRODUCTO = [
#         ('PANIFICACION', 'Panificación'),
#         ('PASTELERIA', 'Pastelería'),
#     ]
#     ESTADO_PRODUCTO = [
#         ('ACTIVO', 'Activo'),
#         ('INACTIVO', 'Inactivo')
#     ]

#     id_producto = models.AutoField(primary_key=True)
#     descripcion = models.CharField(max_length=50)
#     categoria = models.CharField(max_length=30, choices=CATEGORIA_PRODUCTO)
#     stock = models.PositiveIntegerField(null=True)
#     precio = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    
#     def __str__(self):
#         return f"{self.descripcion} - precio: $ {self.precio}"

class Venta(models.Model):
    TIPO_VENTA = [
        ('MAYORISTA', 'Mayorista'),
        ('MINORISTA', 'Minorista')
    ]
    FORMA_PAGO = [
        ('CONTADO', 'Contado'),
        ('TRANSFERENCIA', 'Transferencia'),
        ('CREDITO', 'Credito'),
        ('OTRO', 'Otro')
    ]
    TIPO_COMPROBANTE = [
        ('RECIBO', 'Recibo'),
        ('FACTURA', 'Factura'),
        ('OTRO', 'Otro')
    ]
    ESTADO_VENTA = [
        ('REGISTRADA', 'Registrada'),
        ('CANCELADA', 'Cancelada'),
    ]

    id_venta = models.AutoField(primary_key=True)
    fecha_venta = models.DateField(auto_now_add=True)
    tipo_venta = models.CharField(max_length=30, choices=TIPO_VENTA, default='Mayorista')
    forma_pago = models.CharField(max_length=30, choices=FORMA_PAGO)
    tipo_comprobante = models.CharField(max_length=30, choices=TIPO_COMPROBANTE)
    numero_comprobante = models.IntegerField(unique=True)
    observaciones = models.TextField(blank=True, null=True)
    estado = models.CharField(choices=ESTADO_VENTA, default='REGISTRADA')
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True,null=True) 
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='empleado', null=True)
    mayorista = models.ForeignKey(Mayorista, on_delete=models.CASCADE, related_name='mayorista', null=True)
    # producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='productos', null=True)

    def __str__(self):
        return f'Id venta: {self.id_venta} - fecha: {self.fecha_venta}'
    
class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='venta', null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='producto', null=True)
    cantidad = models.IntegerField(null=True)
    # precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Id detalle: {self.pk} - id venta: {self.venta.id_venta} - producto: {self.producto.descripcion}'
    
class Caja(models.Model):
    id_caja = models.AutoField(primary_key=True)
    fecha_hora_apertura = models.DateTimeField(auto_now_add=True)
    fecha_hora_cierre = models.DateTimeField(blank=True, null=True)
    saldo_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_final = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_ventas = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    # empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def __str__(self):
        return f'caja: {self.id_caja} - fecha de apertura: {self.fecha_hora_apertura}'