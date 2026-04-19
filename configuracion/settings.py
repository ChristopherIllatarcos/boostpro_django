"""
Django settings for configuracion project.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# 1. Rutas del Proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Carga de variables de entorno (.env)
load_dotenv(os.path.join(BASE_DIR, '.env'))

# 3. Variables Básicas
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-default-cambiame')
DEBUG = os.getenv('DEBUG') == 'False' #Cambiar a False en producción

ALLOWED_HOSTS = ['boostpro.cl', '127.0.0.1', 'localhost']



# 4. Diagnóstico (solo en consola si DEBUG=True)
if DEBUG:
    print(f"--- DIAGNÓSTICO BOOSTPRO ---")
    print(f"BASE_DIR: {BASE_DIR}")
    print(f"¿Existe .env?: {os.path.exists(os.path.join(BASE_DIR, '.env'))}")
    print(f"--- -------------------- ---")

# 5. Hosts Permitidos
ALLOWED_HOSTS = [
    'boostpro.cl',
    'www.boostpro.cl',
    'bootsPro.pythonanywhere.com',
    '127.0.0.1',
    'localhost'
]

# 6. Definición de Aplicaciones
INSTALLED_APPS = [
    'web',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 7. Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'configuracion.urls'

# 8. Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'configuracion.wsgi.application'

# 9. Base de Datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / os.getenv('DB_NAME', 'db.sqlite3'),
    }
}

# 10. Validación de Passwords
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 11. Internacionalización
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True

# 12. Archivos Estáticos y Media
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'web/static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 13. Configuración de Correo (Gmail)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

# 14. Seguridad para Producción
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # Cambia a True solo cuando tengas HTTPS activo en PythonAnywhere
    SECURE_SSL_REDIRECT = False 
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'