"""
Django settings for coffe_shop project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env file for local development
load_dotenv(os.path.join(BASE_DIR, '.env'))

# Check for the environment type
DJANGO_ENV = os.getenv('DJANGO_ENV', 'development')

# --- Basic Security Settings ---
# In production, SECRET_KEY and DEBUG must be set via environment variables.
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'True') == 'True' # Defaults to True for development

if DJANGO_ENV == 'production' and not SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable not set for production")

if DJANGO_ENV == 'production' and DEBUG:
    raise ValueError("DEBUG must be set to False in production")


# --- Host Configuration ---
if DJANGO_ENV == 'production':
    # For production, trust the domain from EB and the .elasticbeanstalk.com subdomain for health checks
    ALLOWED_HOSTS = [os.getenv('EB_HOST'), '.elasticbeanstalk.com']
else:
    # For development, allow localhost and 127.0.0.1
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "crispy_tailwind",
    "rest_framework",
    "products",
    "users",
    "orders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "coffe_shop.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "users", "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                "django.template.context_processors.csrf",
            ],
        },
    },
]

WSGI_APPLICATION = "coffe_shop.wsgi.application"


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en"  # Cambiar a inglés como idioma por defecto

LANGUAGES = [
    ("en", "English"),
    ("es", "Español"),
    ("fr", "Français"),
]

# Nombre explícito para la cookie de idioma
LANGUAGE_COOKIE_NAME = "django_language"
LANGUAGE_COOKIE_SAMESITE = "Lax"  # Recomendado para seguridad
LANGUAGE_COOKIE_PATH = "/"  # Asegura que la cookie de idioma se aplique a todo el sitio
LANGUAGE_COOKIE_DOMAIN = None  # Se aplica solo al dominio actual
LANGUAGE_COOKIE_SECURE = False  # Simplificar para que funcione en HTTP y HTTPS
LANGUAGE_COOKIE_HTTPONLY = True  # Mejora la seguridad

TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Ubicación de los archivos de traducción
LOCALE_PATHS = [
    BASE_DIR / "locale",
]

# Crispy Forms configuration
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

LOGIN_URL = "/usuarios/login/"
LOGIN_REDIRECT_URL = "products:product_list"
LOGOUT_REDIRECT_URL = "login"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configuración de archivos estáticos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Directorio para archivos estáticos personalizados
]

# Configuración de finders para archivos estáticos
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ==============================================================================
# Configuración de WhiteNoise para archivos estáticos
# ==============================================================================
# Usar WhiteNoise para servir archivos estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configuración adicional de WhiteNoise
WHITENOISE_USE_FINDERS = True
WHITENOISE_AUTOREFRESH = True if not DEBUG else False

# Configuración de compresión para archivos estáticos
WHITENOISE_SKIP_COMPRESS_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif', 'webp', 'zip', 'gz', 'tgz', 'bz2', 'tbz', 'xz', 'br']

# Configuración adicional para asegurar que los archivos del admin se sirvan correctamente
WHITENOISE_MAX_AGE = 31536000  # 1 año para archivos estáticos
WHITENOISE_STATIC_PREFIX = '/static/'

# Configuración para servir archivos de media con WhiteNoise
WHITENOISE_USE_FINDERS = True
WHITENOISE_AUTOREFRESH = True if not DEBUG else False

# Configuración específica para archivos de media en AWS
if DEBUG: # Only apply if in DEBUG mode
    # En producción, usar el mismo directorio para media que en desarrollo
    MEDIA_ROOT = '/var/app/current/media'
    MEDIA_URL = '/media/'
    
    # Configurar WhiteNoise para servir archivos de media
    WHITENOISE_STATIC_PREFIX = '/static/'
    
    # Agregar el directorio de media como un directorio estático adicional
    import os
    STATICFILES_DIRS.append(('media', MEDIA_ROOT))
    

# --- Database Configuration ---
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
if DJANGO_ENV == 'production':
    # Production database configured via DJANGO_DB_URL environment variable
    DATABASES = {
        'default': dj_database_url.parse(os.getenv('DJANGO_DB_URL'))
    }
    DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql'
else:
    # Development database (SQLite)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

