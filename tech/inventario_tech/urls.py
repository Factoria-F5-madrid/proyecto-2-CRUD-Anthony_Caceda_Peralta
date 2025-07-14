from django.urls import path

from .views import (
    AlmacenListView,
    AlmacenCreateView,
    AlmacenUpdateView,
    AlmacenDeleteView,
    ProductoListView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
    ProductoStockDetailView,
)

app_name = "inventario_tech"  #  IMPORTANTE

urlpatterns = [
    # ── Almacenes ─────────────────────────────────────────────────────────────
    path("almacenes/", AlmacenListView.as_view(), name="almacen-list"),
    path("almacenes/nuevo/", AlmacenCreateView.as_view(), name="almacen-create"),
    path(
        "almacenes/<int:pk>/editar/", AlmacenUpdateView.as_view(), name="almacen-update"
    ),
    path(
        "almacenes/<int:pk>/borrar/", AlmacenDeleteView.as_view(), name="almacen-delete"
    ),
    # ── Productos ─────────────────────────────────────────────────────────────
    path("productos/", ProductoListView.as_view(), name="producto-list"),
    path("productos/nuevo/", ProductoCreateView.as_view(), name="producto-create"),
    path(
        "productos/<int:pk>/editar/",
        ProductoUpdateView.as_view(),
        name="producto-update",
    ),
    path(
        "productos/<int:pk>/borrar/",
        ProductoDeleteView.as_view(),
        name="producto-delete",
    ),
    path(
        "productos/<int:pk>/stock/",
        ProductoStockDetailView.as_view(),
        name="producto-stock",
    ),
]
