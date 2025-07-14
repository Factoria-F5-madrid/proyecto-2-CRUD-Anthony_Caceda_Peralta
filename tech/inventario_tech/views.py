from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import transaction
from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .forms import StockFormSet
from .models import Producto, Almacen
from django.shortcuts import render


def bienvenida(request):
    return render(request, "inventario_tech/bienvenida.html")


# ── mixin de autorización ──────────────────────────────────────────────────────
class StaffRequiredMixin(UserPassesTestMixin):
    """Solo usuarios staff pueden acceder."""

    def test_func(self):
        return self.request.user.is_staff


# ── CRUD de ALMACÉN ────────────────────────────────────────────────────────────
class AlmacenListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = Almacen
    template_name = (
        "inventario_tech/almacen_list.html"  # tener claro el uso del los templates
    )
    context_object_name = "almacenes"
    paginate_by = 25


class AlmacenCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Almacen
    fields = ["nombre"]
    success_url = reverse_lazy("inventario_tech:almacen-list")  #


class AlmacenUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Almacen
    fields = ["nombre"]
    success_url = reverse_lazy("inventario_tech:almacen-list")  #


class AlmacenDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Almacen
    success_url = reverse_lazy("inventario_tech:almacen-list")  #


# ── CRUD de PRODUCTO + STOCK ───────────────────────────────────────────────────
class ProductoListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = Producto
    template_name = "inventario_tech/producto_list.html"  #
    context_object_name = "productos"
    paginate_by = 25

    def get_queryset(self):
        return (
            Producto.objects.prefetch_related("stock_set__almacen")
            .annotate(stock_total=Sum("stock__cantidad"))
            .order_by("nombre")
        )


class _ProductoBaseView(LoginRequiredMixin, StaffRequiredMixin):
    model = Producto
    fields = ["nombre", "precio"]  # 'almacenes' se gestiona vía StockFormSet
    template_name = "inventario_tech/producto_form.html"  #
    success_url = reverse_lazy("inventario_tech:producto-list")  #

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["stock_formset"] = StockFormSet(
                self.request.POST, instance=self.object
            )
        else:
            data["stock_formset"] = StockFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        stock_formset = context["stock_formset"]
        if not stock_formset.is_valid():
            return self.form_invalid(form)

        with transaction.atomic():
            self.object = form.save()
            stock_formset.instance = self.object
            stock_formset.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Muestra los errores del producto o del formset.
        """
        context = self.get_context_data(form=form)
        return self.render_to_response(context)


class ProductoCreateView(_ProductoBaseView, CreateView):
    pass


class ProductoUpdateView(_ProductoBaseView, UpdateView):
    pass


class ProductoDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy("inventario_tech:producto-list")  #


class ProductoStockDetailView(LoginRequiredMixin, StaffRequiredMixin, DetailView):
    model = Producto
    template_name = "inventario_tech/producto_stock_detail.html"
