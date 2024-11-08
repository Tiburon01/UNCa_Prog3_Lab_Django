# Generated by Django 5.1.2 on 2024-10-31 23:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0009_venta_empleado_venta_mayorista_venta_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(null=True)),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='producto', to='ventas.producto')),
                ('venta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='venta', to='ventas.venta')),
            ],
        ),
    ]