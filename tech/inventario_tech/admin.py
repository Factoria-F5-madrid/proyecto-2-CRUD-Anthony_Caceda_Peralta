from django.contrib import admin
from .models import Producto, Almacen, Stock


class StockInline(admin.TabularInline):
    model = Stock
    extra = 0


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio")
    inlines = [StockInline]


@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
