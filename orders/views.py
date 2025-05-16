from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Order, OrderProduct
from .forms import OrderProductForm
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class MyOrderView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/my_order.html'
    context_object_name = 'orders'
    login_url = reverse_lazy('login')
    redirect_field_name = 'next'

    def handle_no_permission(self):
        messages.warning(self.request, 'Por favor, inicia sesión para ver tus órdenes.')
        return super().handle_no_permission()

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, is_active=True).order_by('-created_at')
    
class CreatOrderProductView(LoginRequiredMixin, CreateView):
    template_name = 'orders/add_product.html'
    form_class = OrderProductForm
    success_url = reverse_lazy('products:product_list')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        order, created = Order.objects.get_or_create(
            is_active=True,
            user=self.request.user
        )
        form.instance.order = order
        if not form.instance.quantity:
            form.instance.quantity = 1
        messages.success(self.request, 'Producto añadido a tu orden correctamente.')
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        # Si se está enviando desde la lista de productos
        if 'product' in request.POST and not self.request.FILES:
            order, created = Order.objects.get_or_create(
                is_active=True,
                user=self.request.user
            )
            product_id = request.POST.get('product')
            
            # Crear o actualizar el producto en la orden
            order_product, created = OrderProduct.objects.get_or_create(
                order=order,
                product_id=product_id,
                defaults={'quantity': 1}
            )
            
            # Si ya existía, aumentar la cantidad
            if not created:
                order_product.quantity += 1
                order_product.save()
                
            messages.success(request, 'Producto añadido a tu orden correctamente.')
            return redirect('products:product_list')
            
        return super().post(request, *args, **kwargs)
       
       