# Generated by Django 5.2.4 on 2025-07-14 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario_tech', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stock',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='stock',
            constraint=models.UniqueConstraint(fields=('producto', 'almacen'), name='unique_stock_producto_almacen'),
        ),
    ]
