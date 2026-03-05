from django.contrib import admin
from .models import (
    Profile, Location, Project, Experience, 
    Service, SocialNetwork, ContactMessage, 
    Education, Article, Skill  # <--- AJOUTE 'Skill' ICI
)

# Permet d'éditer la localisation directement dans la page Profil
class LocationInline(admin.StackedInline):
    model = Location
    can_delete = False

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [LocationInline]
    list_display = ('nom', 'prenom', 'email')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('diplome', 'etablissement', 'date_debut')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'nom_entreprise', 'date_debut')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type_service')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'created_at')

# AJOUTE CETTE CLASSE POUR LES SKILLS
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('nom', 'niveau', 'categorie')

admin.site.register(SocialNetwork)
admin.site.register(ContactMessage)