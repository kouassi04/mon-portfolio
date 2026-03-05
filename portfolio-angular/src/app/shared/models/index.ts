export interface Location {
  id: number;
  pays: string;
  ville: string;
  quartier: string;
  latitude?: number;
  longitude?: number;
}

export interface SocialNetwork {
  id: number;
  nom_plateforme: string;
  lien: string;
  icone: string;
}

export interface Skill {
  id: number;
  nom: string;
  niveau: number;
  categorie: 'dev' | 'reseau' | 'outil' | 'autre';
  icone: string;
}

export interface Service {
  id: number;
  nom: string;
  detail: string;
  type_service: string;
  outils: string;
  icone: string;
}

export interface Project {
  id: number;
  titre: string;
  resume: string;
  image: string;
  lien?: string;
  lien_github?: string;
  categorie: string;
  technologies: string;
  created_at: string;
}

export interface Education {
  id: number;
  etablissement: string;
  diplome: string;
  domaine: string;
  description: string;
  date_debut: string;
  date_fin?: string;
}

export interface Experience {
  id: number;
  nom_entreprise: string;
  role: string;
  description: string;
  date_debut: string;
  date_fin?: string;
  type_contrat: string;
}

export interface Stat {
  id: number;
  label: string;
  valer: number;
  icone: string;
}

export interface Testimonial {
  id: number;
  nom_client: string;
  role_client: string;
  photo_client?: string;
  message: string;
  note: number;
  created_at: string;
}

export interface Article {
  id: number;
  titre: string;
  resume: string;
  contenu: string;
  image?: string;
  categorie: string;
  tags: string;
  created_at: string;
  updated_at: string;
  lien?: string; // <--- CORRECTION : Ajout de la propriété lien
}

export interface Profile {
  id: number;
  nom: string;
  prenom: string;
  photo?: string;
  description: string;
  age: number;
  email: string;
  telephone: string;
  lien_cv?: string;
  lien_github?: string;
  lien_video?: string;
  
  location?: Location;
  socials?: SocialNetwork[];
  skills?: Skill[];
  services?: Service[];
  projects?: Project[];
  educations?: Education[];
  experiences?: Experience[];
  stats?: Stat[];
  testimonials?: Testimonial[];
  articles?: Article[];
}

export interface ContactForm {
  nom_complet: string;
  email: string;
  objet: string;
  message: string;
}