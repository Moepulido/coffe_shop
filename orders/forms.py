from django import forms
from .models import OrderProduct


class OrderProductForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = ("product", "quantity")
