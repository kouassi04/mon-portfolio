from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    

# Ce code crée l'admin automatiquement au démarrage du serveur
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'votre-email@gmail.com', 'votre_mot_de_passe_secret')
]

# servir MEDIA
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)