from pathlib import Path
import os

# -------------------------------------------------------------
# BASE GENERAL DEL PROYECTO
# -------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent


# -------------------------------------------------------------
# CONFIGURACIÓN BÁSICA
# -------------------------------------------------------------
SECRET_KEY = 'dev-secret-key-cámbiala-en-producción'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# -------------------------------------------------------------
# APLICACIONES INSTALADAS
# -------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Tus apps locales
    'store',
    'carrito',
    'usuarios',
    'Lupa',
]


# -------------------------------------------------------------
# MIDDLEWARE
# -------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# -------------------------------------------------------------
# URL PRINCIPAL Y WSGI
# -------------------------------------------------------------
ROOT_URLCONF = 'bunny.urls'
WSGI_APPLICATION = 'bunny.wsgi.application'


# -------------------------------------------------------------
# TEMPLATES (carpeta Templates con mayúscula)
# -------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'Templates'],  # Usa la carpeta Templates con T mayúscula
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


# -------------------------------------------------------------
# BASE DE DATOS (SQLite para desarrollo)
# -------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# -------------------------------------------------------------
# VALIDADORES DE CONTRASEÑA
# -------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# -------------------------------------------------------------
# CONFIGURACIÓN DE IDIOMA Y ZONA HORARIA
# -------------------------------------------------------------
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True


# -------------------------------------------------------------
# ARCHIVOS ESTÁTICOS Y MEDIA
# -------------------------------------------------------------
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# -------------------------------------------------------------
# LOGIN / LOGOUT
# -------------------------------------------------------------
LOGIN_URL = '/usuarios/login/'
LOGIN_REDIRECT_URL = 'catalogo'
LOGOUT_REDIRECT_URL = '/usuarios/login/'


# -------------------------------------------------------------
# CONFIGURACIÓN FINAL
# -------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
