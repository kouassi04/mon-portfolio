from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import os # Correction de l'erreur "os is not defined"

# On définit BASE_DIR ici aussi pour résoudre l'erreur Pylance
BASE_DIR = settings.BASE_DIR 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

# Service des fichiers MEDIA (Photos de projets, profil, blog)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Service des fichiers STATIC (CSS, JS)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)