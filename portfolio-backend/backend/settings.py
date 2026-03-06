from pathlib import Path
import os

# Construction des chemins à l'intérieur du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# SÉCURITÉ : Récupérer la clé secrète depuis l'environnement
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-default-key-for-dev')

# Mode debug : False en production pour la cybersécurité
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

# Autoriser ton domaine Render
ALLOWED_HOSTS = [
    'localhost', 
    '127.0.0.1', 
    '.onrender.com', 
    'mon-portfolio-oxum.onrender.com'
]

# ─── APPLICATIONS INSTALLÉES ──────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'api',
]

# ─── MIDDLEWARE ───────────────────────────────────────────────────────────────
# L'ordre est CRITIQUE ici pour résoudre l'erreur CORS
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',        # Doit impérativement être en premier
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # Pour les fichiers statiques en prod
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',    # Doit être après CorsMiddleware
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'backend.wsgi.application'

# ─── BASE DE DONNÉES ──────────────────────────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ─── INTERNATIONALISATION ─────────────────────────────────────────────────────
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Abidjan'
USE_I18N = True
USE_TZ = True

# ─── FICHIERS STATIQUES ───────────────────────────────────────────────────────
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configuration WhiteNoise pour indexer les fichiers
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ─── MEDIA ────────────────────────────────────────────────────────────────────
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ─── CONFIGURATION CORS DYNAMIQUE ─────────────────────────────────────────────
# Cette section lit tes réglages directement depuis l'interface Render
CORS_ALLOWED_ORIGINS = [
    origin.strip() for origin in os.environ.get(
        'CORS_ALLOWED_ORIGINS', 
        'http://localhost:4200,https://mon-portfolio-rho-three.vercel.app'
    ).split(',') if origin.strip()
]
CORS_ALLOW_CREDENTIALS = True

# ─── CONFIGURATION EMAIL (SÉCURISÉE) ──────────────────────────────────────────
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'kouassisamuelo226@gmail.com' 
# Récupérer le mot de passe d'application via variable d'environnement
EMAIL_HOST_PASSWORD = os.environ.get('GMAIL_APP_PASSWORD', 'gofi ghbf dbkr xfkq')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER