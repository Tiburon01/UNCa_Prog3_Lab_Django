# Generated by Django 5.1.2 on 2024-10-31 23:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0008_alter_producto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='empleado',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empleado', to='ventas.empleado'),
        ),
        migrations.AddField(
            model_name='venta',
            name='mayorista',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mayorista', to='ventas.mayorista'),
        ),
        migrations.AddField(
            model_name='venta',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='ventas.producto'),
        ),
    ]
