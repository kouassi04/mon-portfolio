from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Inclus les routes de ton application 'api'
]

# On force le service des fichiers MEDIA même en production (DEBUG=False)
# C'est ce qui permettra à tes images de projets de s'afficher sur Render
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# On ajoute aussi le service des fichiers STATIC au cas où
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)