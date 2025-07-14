from django.forms import inlineformset_factory, BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Producto, Stock


class BaseStockFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        seen = set()
        for form in self.forms:
            if form.cleaned_data.get("DELETE"):
                continue  # omitimos los que el usuario marca para borrar

            almacen = form.cleaned_data.get("almacen")
            cantidad = form.cleaned_data.get("cantidad")

            # Ignorar completamente filas vacías (almacén vacío Y cantidad vacía)
            if not almacen and (cantidad in (None, "", 0)):
                continue

            # Evitar duplicados de almacén
            if almacen in seen:
                raise ValidationError("No puedes repetir el mismo almacén dos veces.")
            seen.add(almacen)


StockFormSet = inlineformset_factory(
    parent_model=Producto,
    model=Stock,
    formset=BaseStockFormSet,  # formset personalizado
    fields=["almacen", "cantidad"],
    extra=1,
    can_delete=True,
)
