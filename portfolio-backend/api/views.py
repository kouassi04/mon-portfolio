from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from django.core.mail import send_mail # Import pour l'envoi d'email
from django.conf import settings

from .models import (
    Profile, Project, Education, Experience,
    Service, Skill, SocialNetwork, Stat,
    Testimonial, Article, ContactMessage
)
from .serializers import (
    ProfileSerializer, ProjectSerializer, EducationSerializer,
    ExperienceSerializer, ServiceSerializer, SkillSerializer,
    SocialNetworkSerializer, StatSerializer, TestimonialSerializer,
    ArticleSerializer, ContactMessageSerializer
)


# Profil — lecture seule publiquement, écriture admin uniquement
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # GET /api/profiles/1/full/ → tout le profil en un seul appel
    @action(detail=True, methods=['get'], url_path='full')
    def full(self, request, pk=None):
        profile = self.get_object()
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        categorie = self.request.query_params.get('categorie')
        if categorie:
            queryset = queryset.filter(categorie__icontains=categorie)
        return queryset


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all().order_by('-date_debut')
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all().order_by('-date_debut')
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all().order_by('categorie', '-niveau')
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SocialNetworkViewSet(viewsets.ModelViewSet):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class StatViewSet(viewsets.ModelViewSet):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all().order_by('-created_at')
    serializer_class = TestimonialSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Contact — Envoi d'email automatique après enregistrement
class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by('-created_at')
    serializer_class = ContactMessageSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        # On enregistre d'abord le message dans la base de données
        instance = serializer.save()
        
        # On prépare et on envoie l'email
        try:
            sujet = f"Portfolio : {instance.objet} de {instance.nom_complet}"
            message_corps = f"Nouveau message reçu !\n\nNom: {instance.nom_complet}\nEmail: {instance.email}\n\nMessage:\n{instance.message}"
            
            send_mail(
                sujet,
                message_corps,
                settings.EMAIL_HOST_USER, # Expéditeur (ton gmail)
                [settings.EMAIL_HOST_USER], # Destinataire (toi-même)
                fail_silently=False,
            )
        except Exception as e:
            print(f"Erreur d'envoi d'email: {e}")