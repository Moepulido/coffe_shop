from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Product
from products.forms import ProductForm
import os
from django.http import HttpResponse, Http404
from django.conf import settings
from django.views.decorators.http import require_GET
from django.views.decorators.cache import cache_control
import mimetypes
from django.shortcuts import redirect
from django.utils.translation import get_language_from_request


def home(request):
    return render(
        request, "base.html"
    )  # Asegúrate de que la plantilla base.html exista


class ListProductsView(TemplateView):
    template_name = "products/list_products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context["add_products"] = products
        return context


class ProductFormView(TemplateView):
    template_name = (
        "products/add_product.html"  # Asegúrate de que esta plantilla exista
    )
    form_class = ProductForm  # Asegúrate de que esta línea esté correcta


@require_GET
@cache_control(max_age=3600)  # Cache por 1 hora
def serve_media(request, path):
    """
    Sirve archivos de media en producción
    """
    # Construir la ruta completa del archivo
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    
    # Verificar seguridad y existencia
    if not os.path.exists(file_path) or not os.path.commonpath([settings.MEDIA_ROOT, file_path]) == settings.MEDIA_ROOT:
        raise Http404("Archivo no encontrado")
    
    # Obtener el tipo MIME del archivo
    content_type, _ = mimetypes.guess_type(file_path)
    if content_type is None:
        content_type = 'application/octet-stream'
    
    # Leer y servir el archivo
    try:
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type=content_type)
            response['Content-Length'] = os.path.getsize(file_path)
            return response
    except IOError:
        raise Http404("Error al leer el archivo")


def diagnostico_archivos(request):
    base_path = settings.BASE_DIR
    resultado = []
    for root, dirs, files in os.walk(base_path):
        nivel = root.replace(str(base_path), '').count(os.sep)
        indent = '&nbsp;&nbsp;' * nivel
        resultado.append(f"{indent}<b>{os.path.basename(root)}/</b>")
        subindent = '&nbsp;&nbsp;' * (nivel + 1)
        for f in files:
            resultado.append(f"{subindent}{f}")
    html = '<h2>Estructura de archivos en producción</h2><pre>' + '<br>'.join(resultado) + '</pre>'
    return HttpResponse(html)


def root_redirect(request):
    lang = get_language_from_request(request)
    if lang not in ['en', 'es', 'fr']:
        lang = 'en'
    return redirect(f'/{lang}/')
