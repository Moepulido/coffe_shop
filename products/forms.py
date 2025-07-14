from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label=_('Nombre'))
    description = forms.CharField(max_length=300, label=_('Descripción en español'))
    description_en = forms.CharField(max_length=300, label=_('Descripción en inglés'), required=False)
    description_fr = forms.CharField(max_length=300, label=_('Descripción en francés'), required=False)
    price = forms.DecimalField(max_digits=10, decimal_places=2, label=_('Precio'))
    available = forms.BooleanField(initial=True, label=_('Disponible'), required=False)
    photo = forms.CharField(max_length=100, label=_('Nombre de archivo de la imagen (en static/images/)'), required=False)

    def save(self):
        Product.objects.create(
            name=self.cleaned_data["name"],
            description=self.cleaned_data["description"],
            description_en=self.cleaned_data["description_en"],
            description_fr=self.cleaned_data["description_fr"],
            price=self.cleaned_data["price"],
            available=self.cleaned_data["available"],
            photo=self.cleaned_data["photo"],
        )
