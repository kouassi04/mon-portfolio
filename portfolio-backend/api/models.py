from django.db import models


# 1. PROFIL PRINCIPAL
class Profile(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    description = models.TextField()
    age = models.IntegerField()
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    lien_cv = models.FileField(upload_to='cv/', blank=True, null=True)
    lien_github = models.URLField(blank=True, null=True)
    lien_video = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


# 2. LOCALISATION
class Location(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='location')
    pays = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return f"{self.ville}, {self.pays}"


# 3. RESEAUX SOCIAUX
class SocialNetwork(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='socials')
    nom_plateforme = models.CharField(max_length=50)
    lien = models.URLField()
    icone = models.CharField(max_length=50, blank=True)  # ex: 'fab fa-linkedin'

    def __str__(self):
        return self.nom_plateforme


# 4. COMPETENCES (barres de progression dans About/Resume)
class Skill(models.Model):
    CATEGORIE_CHOICES = [
        ('dev', 'Développement'),
        ('reseau', 'Réseaux'),
        ('outil', 'Outils'),
        ('autre', 'Autre'),
    ]
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')
    nom = models.CharField(max_length=100)          # ex: Python, Angular
    niveau = models.IntegerField(default=0)          # 0 à 100 (pourcentage)
    categorie = models.CharField(max_length=50, choices=CATEGORIE_CHOICES, default='dev')
    icone = models.CharField(max_length=50, blank=True)  # ex: 'fab fa-python'

    def __str__(self):
        return f"{self.nom} ({self.niveau}%)"


# 5. SERVICES
class Service(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='services')
    nom = models.CharField(max_length=100)
    detail = models.TextField()
    type_service = models.CharField(max_length=100)
    outils = models.CharField(max_length=200)       # ex: Flutter, Dart
    icone = models.CharField(max_length=50, blank=True)  # ex: 'fas fa-mobile'

    def __str__(self):
        return self.nom


# 6. PROJETS
class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects', null=True, blank=True)
    titre = models.CharField(max_length=100)
    resume = models.TextField()
    image = models.ImageField(upload_to='projects/')
    lien = models.URLField(blank=True, null=True)
    lien_github = models.URLField(blank=True, null=True)
    categorie = models.CharField(max_length=100, default='Dev')
    technologies = models.CharField(max_length=200, blank=True)  # ex: Angular, Django
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre


# 7. FORMATIONS (section Resume)
class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='educations')
    etablissement = models.CharField(max_length=150)
    diplome = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField(blank=True, null=True)   # Null si en cours

    def __str__(self):
        return f"{self.diplome} — {self.etablissement}"


# 8. EXPERIENCES PROFESSIONNELLES (section Resume)
class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiences')
    nom_entreprise = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField(blank=True, null=True)   # Null si en cours
    type_contrat = models.CharField(max_length=50)       # Stage, CDD, Freelance...

    def __str__(self):
        return f"{self.role} chez {self.nom_entreprise}"


# 9. CHIFFRES CLES (section Facts)
class Stat(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='stats')
    label = models.CharField(max_length=100)    # ex: Projets réalisés
    valeur = models.IntegerField()              # ex: 12
    icone = models.CharField(max_length=50, blank=True)  # ex: 'fas fa-project-diagram'

    def __str__(self):
        return f"{self.label}: {self.valeur}"


# 10. TEMOIGNAGES (section Testimonial)
class Testimonial(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='testimonials')
    nom_client = models.CharField(max_length=100)
    role_client = models.CharField(max_length=100)   # ex: CTO chez XYZ
    photo_client = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    message = models.TextField()
    note = models.IntegerField(default=5)            # Note sur 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Témoignage de {self.nom_client}"


# 11. ARTICLES DE BLOG
class Article(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='articles')
    titre = models.CharField(max_length=200)
    resume = models.TextField()
    contenu = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    categorie = models.CharField(max_length=100, blank=True)
    tags = models.CharField(max_length=200, blank=True)   # ex: Python, Django, API
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre


# 12. MESSAGES DE CONTACT
class ContactMessage(models.Model):
    nom_complet = models.CharField(max_length=100)
    email = models.EmailField()
    objet = models.CharField(max_length=200)
    message = models.TextField()
    lu = models.BooleanField(default=False)             # Pour savoir si tu l'as lu
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.nom_complet} — {self.objet}"