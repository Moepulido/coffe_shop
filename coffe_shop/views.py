from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Product
from products.forms import ProductForm

def home(request):
    return render(request, 'base.html')  # Asegúrate de que la plantilla base.html exista 

class ListProductsView(TemplateView):
    template_name = "products/list_products.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context['add_products'] = products
        return context

class ProductFormView(TemplateView):
    template_name = "products/add_product.html"  # Asegúrate de que esta plantilla exista
    form_class = ProductForm  # Asegúrate de que esta línea esté correcta
    
    