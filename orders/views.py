from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Order, OrderProduct
from products.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def add_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product')
        product = get_object_or_404(Product, id=product_id)
        
        # Obtener o crear una orden activa para el usuario
        order, _ = Order.objects.get_or_create(user=request.user, is_active=True)
        
        # Obtener o crear el producto en la orden
        order_product, created = OrderProduct.objects.get_or_create(
            order=order,
            product=product,
            defaults={'quantity': 1}
        )
        
        # Si el producto ya estaba en la orden, aumenta la cantidad
        if not created:
            order_product.quantity += 1
            order_product.save()
            messages.info(request, f'Se ha incrementado la cantidad de {product.name} en tu pedido.')
        else:
            messages.success(request, f'{product.name} ha sido añadido a tu pedido.')
            
        return redirect('products:product_list')
    
    # Si no es POST, redirigir a la lista de productos
    return redirect('products:product_list')


# Create your views here.
class MyOrderView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "orders"
    login_url = reverse_lazy("login")

    def handle_no_permission(self):
        messages.warning(self.request, "Por favor, inicia sesión para ver tus órdenes.")
        return super().handle_no_permission()

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, is_active=True).order_by(
            "-created_at"
        )
