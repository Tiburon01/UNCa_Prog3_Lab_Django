# Generated by Django 5.1.2 on 2024-10-31 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0007_producto_precio_producto_stock_venta_precio_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('PANIFICACION', 'Panificación'), ('PASTELERIA', 'Pastelería')], max_length=30),
        ),
    ]
