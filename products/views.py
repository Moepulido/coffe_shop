from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ProductForm
from .models import Product
from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


# Create your views here.
class ProductFormView(generic.FormView):
    form_class = ProductForm
    template_name = "products/add_product.html"
    success_url = "/products/"  # Cambiar a una URL absoluta

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductListView(generic.ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"

    def form_valid(self, form):
        # Crear un nuevo producto con los datos del formulario
        form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def is_superuser(user):
    return user.is_superuser

# Vista de edición protegida para administradores
@login_required
@user_passes_test(is_superuser)
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        # El formulario ya no maneja archivos, solo datos de POST
        form = ProductForm(request.POST)
        if form.is_valid():
            # Actualizamos manualmente el producto existente
            product.name = form.cleaned_data["name"]
            product.description = form.cleaned_data["description"]
            product.description_en = form.cleaned_data["description_en"]
            product.description_fr = form.cleaned_data["description_fr"]
            product.price = form.cleaned_data["price"]
            product.available = form.cleaned_data["available"]
            product.photo = form.cleaned_data["photo"] # Asigna el nuevo nombre de archivo
            
            product.save()
            return redirect("products:product_detail", product_id=product.id)
    else:
        # Para GET, creamos un formulario con los valores iniciales del producto
        initial_data = {
            "name": product.name,
            "description": product.description,
            "description_en": product.description_en,
            "description_fr": product.description_fr,
            "price": product.price,
            "available": product.available,
            "photo": product.photo, # Pasamos el nombre del archivo actual
        }
        form = ProductForm(initial=initial_data)

    # Pasamos tanto el formulario como el producto al template
    return render(
        request, "products/edit_product.html", {"form": form, "product": product}
    )


# Vista alternativa basada en función para añadir productos
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST) # No se manejan archivos
        if form.is_valid():
            form.save()
            return redirect("products:product_list")
    else:
        form = ProductForm()
    return render(request, "products/add_product.html", {"form": form})


def index(request):
    return render(request, "products/index.html")


def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "products/product_detail.html", {"product": product})


# ==============================================================================
# API Views
# ==============================================================================
class ProductAPIView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
