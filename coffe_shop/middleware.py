from django.utils import translation
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings


class LanguageMiddleware(MiddlewareMixin):
    """
    Middleware para asegurar que el idioma seleccionado por el usuario
    se mantenga en todas las páginas, incluso aquellas fuera del patrón i18n.
    """

    def process_request(self, request):
        # Intentar obtener el idioma de la cookie oficial de Django
        language = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME)

        # Verificar que el idioma sea válido
        if language and language in [lang[0] for lang in settings.LANGUAGES]:
            # Activar el idioma para la solicitud actual
            translation.activate(language)
            # Establecer el código de idioma en la solicitud
            request.LANGUAGE_CODE = translation.get_language()
        else:
            # Usar idioma por defecto
            translation.activate(settings.LANGUAGE_CODE)
            request.LANGUAGE_CODE = settings.LANGUAGE_CODE

        return None

    def process_response(self, request, response):
        # Asegurar que el idioma se mantenga en la respuesta
        language = getattr(request, 'LANGUAGE_CODE', settings.LANGUAGE_CODE)
        translation.activate(language)
        return response
