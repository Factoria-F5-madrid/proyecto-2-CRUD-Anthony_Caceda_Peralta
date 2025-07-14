from django.db import models
from django.core.validators import MinValueValidator


class Almacen(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    almacenes = models.ManyToManyField(Almacen, through="Stock")

    def __str__(self):
        return self.nombre


class Stock(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["producto", "almacen"], name="unique_stock_producto_almacen"
            )
        ]

    def __str__(self):
        return (
            f"{self.producto.nombre} en {self.almacen.nombre}: {self.cantidad} unidades"
        )
