from django.utils import translation
from django.utils.deprecation import MiddlewareMixin

class LanguageMiddleware(MiddlewareMixin):
    """
    Middleware para asegurar que el idioma seleccionado por el usuario
    se mantenga en todas las páginas, incluso aquellas fuera del patrón i18n.
    """
    def process_request(self, request):
        # Intentar obtener el idioma de la cookie oficial de Django
        language = request.COOKIES.get('django_language')
        
        # Si no existe, intentar con nuestra cookie personalizada
        if not language:
            language = request.COOKIES.get('user_preferred_language')
            
        if language:
            # Activar el idioma para la solicitud actual
            translation.activate(language)
            
            # Establecer el código de idioma en la solicitud
            request.LANGUAGE_CODE = translation.get_language()
            
        return None 