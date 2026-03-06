import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, forkJoin, of, shareReplay } from 'rxjs';
import { catchError, map, switchMap } from 'rxjs/operators';
import { environment } from '../../../environments/environment';
import { Profile, Skill, SocialNetwork, Stat, Service, ContactForm, Project } from '../models';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  // Utilisation de l'URL définie dans environment.ts
  private baseUrl = environment.apiUrl; 
  private rootUrl = 'https://mon-portfolio-oxum.onrender.com';
  
  private profileData$?: Observable<Profile>;

  constructor(private http: HttpClient) {}

  // Gère les URLs d'images provenant du backend Render
  getMediaUrl(path?: string | null): string {
    if (!path) return ''; 
    if (path.startsWith('http')) return path; // Si l'URL est déjà complète (HTTPS)
    return `${this.rootUrl}${path}`;
  }

  // Récupère l'ensemble des données du profil (Skills, Socials, Stats, Services)
  getFullProfileData(): Observable<Profile> {
    if (!this.profileData$) {
      this.profileData$ = this.http.get<Profile[]>(`${this.baseUrl}/profiles/`).pipe(
        switchMap((profiles) => {
          if (!profiles || profiles.length === 0) throw new Error("Aucun profil trouvé");
          const mainProfile = profiles[0];
          
          return forkJoin({
            skills: this.http.get<Skill[]>(`${this.baseUrl}/skills/`).pipe(catchError(() => of([]))),
            socials: this.http.get<SocialNetwork[]>(`${this.baseUrl}/socials/`).pipe(catchError(() => of([]))),
            stats: this.http.get<Stat[]>(`${this.baseUrl}/stats/`).pipe(catchError(() => of([]))),
            services: this.http.get<Service[]>(`${this.baseUrl}/services/`).pipe(catchError(() => of([]))),
          }).pipe(
            map((res) => {
              mainProfile.skills = res.skills;
              mainProfile.socials = res.socials;
              mainProfile.stats = res.stats;
              mainProfile.services = res.services;
              return mainProfile;
            })
          );
        }),
        shareReplay(1) 
      );
    }
    return this.profileData$;
  }

  // RÉCUPÉRATION DES PROJETS (Pouletshop, OSPF, MoneyGuide, etc.)
  getProjects(): Observable<Project[]> {
    return this.http.get<Project[]>(`${this.baseUrl}/projects/`).pipe(
      catchError((error) => {
        console.error('Erreur lors de la récupération des projets', error);
        return of([]);
      })
    );
  }

  // Envoi du formulaire de contact
  sendContact(form: ContactForm): Observable<any> {
    return this.http.post(`${this.baseUrl}/contact/`, form);
  }
}