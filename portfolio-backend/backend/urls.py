from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User

# Script de création automatique sécurisé
try:
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'kouassisamuelo226@gmail.com', '12345678')
        print("Compte admin créé avec succès !")
except Exception as e:
    print(f"Erreur lors de la création de l'admin : {e}")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]