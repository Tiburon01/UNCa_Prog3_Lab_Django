# Generated by Django 5.1.2 on 2024-10-31 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_itemproducto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='telefonos',
            new_name='telefono',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='precio',
        ),
        migrations.DeleteModel(
            name='ItemProducto',
        ),
    ]
