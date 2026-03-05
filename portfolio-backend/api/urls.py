from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProfileViewSet, ProjectViewSet, EducationViewSet,
    ExperienceViewSet, ServiceViewSet, SkillViewSet,
    SocialNetworkViewSet, StatViewSet, TestimonialViewSet,
    ArticleViewSet, ContactMessageViewSet
)

router = DefaultRouter()
router.register(r'profiles',     ProfileViewSet)       # /api/profiles/
router.register(r'projects',     ProjectViewSet)       # /api/projects/
router.register(r'educations',   EducationViewSet)     # /api/educations/
router.register(r'experiences',  ExperienceViewSet)    # /api/experiences/
router.register(r'services',     ServiceViewSet)       # /api/services/
router.register(r'skills',       SkillViewSet)         # /api/skills/
router.register(r'socials',      SocialNetworkViewSet) # /api/socials/
router.register(r'stats',        StatViewSet)          # /api/stats/
router.register(r'testimonials', TestimonialViewSet)   # /api/testimonials/
router.register(r'articles',     ArticleViewSet)       # /api/articles/
router.register(r'contact',      ContactMessageViewSet)# /api/contact/

urlpatterns = [
    path('', include(router.urls)),
]