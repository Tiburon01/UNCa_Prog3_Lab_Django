# Generated by Django 5.1.2 on 2024-11-11 18:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_producto_estado'),
        ('ventas', '0012_venta_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleventa',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='producto', to='productos.producto'),
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
