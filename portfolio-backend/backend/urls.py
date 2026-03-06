from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User # Import important

# Script de création automatique (à supprimer après connexion)
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'kouassisamuelo226@gmail.com', '12345678')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
] # <--- Vérifie bien que ce crochet est présent !