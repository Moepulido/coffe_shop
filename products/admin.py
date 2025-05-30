from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["name", "price", "available"]
    search_fields = ["name", "description", "description_en", "description_fr"]
    list_filter = ["available"]
    fieldsets = (
        (None, {"fields": ("name", "price", "available", "photo")}),
        (
            "Descripciones",
            {"fields": ("description", "description_en", "description_fr")},
        ),
    )


admin.site.register(Product, ProductAdmin)
