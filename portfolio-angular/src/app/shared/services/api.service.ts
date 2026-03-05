import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, forkJoin, of, shareReplay } from 'rxjs';
import { catchError, map, switchMap } from 'rxjs/operators';
import { Profile, Skill, SocialNetwork, Stat, Service, ContactForm } from '../models';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  // Remplace 'mon-portfolio-oxum' par ton identifiant exact vu sur Render
  private baseUrl = 'https://mon-portfolio-oxum.onrender.com/api';
  private rootUrl = 'https://mon-portfolio-oxum.onrender.com';
  
  private profileData$?: Observable<Profile>;

  constructor(private http: HttpClient) {}

  getMediaUrl(path?: string | null): string {
    if (!path) return ''; 
    if (path.startsWith('http')) return path;
    return `${this.rootUrl}${path}`;
  }

  getFullProfileData(): Observable<Profile> {
    if (!this.profileData$) {
      this.profileData$ = this.http.get<Profile[]>(`${this.baseUrl}/profiles/`).pipe(
        switchMap((profiles) => {
          if (!profiles || profiles.length === 0) throw new Error("Aucun profil");
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

  sendContact(form: ContactForm): Observable<any> {
    return this.http.post(`${this.baseUrl}/contact/`, form);
  }
}