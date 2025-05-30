from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=200, verbose_name=_("nombre"))
    description = models.TextField(max_length=300, verbose_name=_("descripcion"))
    description_en = models.TextField(
        max_length=300, verbose_name=_("descripción en inglés"), blank=True, null=True
    )
    description_fr = models.TextField(
        max_length=300, verbose_name=_("descripción en francés"), blank=True, null=True
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("precio")
    )
    available = models.BooleanField(default=True, verbose_name=_("disponible"))
    photo = models.ImageField(
        upload_to="logos", null=True, blank=True, verbose_name=_("Foto")
    )
    created_at = models.DateField(default=timezone.now, verbose_name=_("creado"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Producto")
        verbose_name_plural = _("Productos")
