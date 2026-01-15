from pathlib import Path
import os

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-auxilio-bonannata-demo-key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_distill',
    'landing',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bonannata_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Usamos plantillas dentro de las apps
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bonannata_site.wsgi.application'

# Database: usar SQLite por defecto en desarrollo, pero en entornos serverless
# (como Vercel) es preferible evitar un archivo en disco (puede ser de solo-lectura).
if os.environ.get('VERCEL') or os.environ.get('VERCEL_REGION'):
    # En Vercel usamos una DB en memoria (no persistente) para evitar errores de I/O.
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Cordoba'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
# Carpeta destino para collectstatic (producción / despliegue)
STATIC_ROOT = BASE_DIR / 'static_collected'

# WhiteNoise: almacenamiento comprimido y manifest para producción
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Django-distill: carpeta de salida para el sitio estático generado
DISTILL_DIR = BASE_DIR.parent / 'dist'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de email
# En desarrollo: consola (emails se muestran en la consola del servidor)
# En producción (Hostinger): usar SMTP de Hotmail/Outlook
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    # Para producción con Hostinger, usar SMTP de Outlook/Hotmail
    EMAIL_HOST = 'smtp-mail.outlook.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'auxiliobonannata@hotmail.com'  # ← Reemplazar con tu contraseña de app en variable de entorno
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD', '')  # usar variable de entorno en producción
