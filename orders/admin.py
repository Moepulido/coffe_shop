from django.contrib import admin
from .models import Order, OrderProduct


class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderProductInline, OrderProductInlineAdmin]
    list_display = ("id", "user", "created_at", "is_active")
    list_filter = ("is_active", "created_at")
    search_fields = ("user__username",)


# Registra solo Order con su clase Admin personalizada
# Esto incluirá OrderProduct como un inline dentro de Order
admin.site.register(Order, OrderAdmin)

# Eliminamos el registro directo de OrderProduct para evitar la duplicación
# admin.site.register(OrderProduct)
