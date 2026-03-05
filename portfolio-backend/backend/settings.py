from pathlib import Path
import os

# Construction des chemins à l'intérieur du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# Clé de sécurité (ne pas partager en production)
SECRET_KEY = 'django-insecure-e6i1y_6a*dve1vg5o!rnm=(5@*hh$c^jsxk)i2dj181yu$57vt'

# Mode debug (True pour le développement)
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# ─── APPLICATIONS INSTALLÉES ──────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Tes applications tierces
    'rest_framework',  # Pour créer les API
    'corsheaders',     # Pour autoriser Angular
    
    # Ton application
    'api',
]

# ─── MIDDLEWARE ───────────────────────────────────────────────────────────────
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',         # ⚠️ DOIT ÊTRE EN PREMIER !
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
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

# Validation des mots de passe
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ─── INTERNATIONALISATION ─────────────────────────────────────────────────────
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Abidjan'
USE_I18N = True
USE_TZ = True

# ─── FICHIERS STATIQUES (CSS, JS de l'admin) ──────────────────────────────────
STATIC_URL = 'static/'

# ─── MEDIA (Tes photos de profil, projets, CV...) ─────────────────────────────
# C'est ici que Django va stocker les images uploadées
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configuration par défaut des IDs
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ─── CORS CONFIGURATION (Lien avec Angular) ───────────────────────────────────
# Autorise ton frontend Angular (port 4200) à discuter avec Django
CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",
]
CORS_ALLOW_CREDENTIALS = True

# ─── REST FRAMEWORK CONFIGURATION ─────────────────────────────────────────────
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',  # Important pour l'upload d'images
        'rest_framework.parsers.FormParser',
    ],
}


# ─── CONFIGURATION EMAIL (SMTP GMAIL) ─────────────────────────────────────────
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'kouassisamuelo226@gmail.com' 
EMAIL_HOST_PASSWORD = 'gofi ghbf dbkr xfkq' # <--- À REMPLACER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER