import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiService } from './api.service'; // On importe le nouveau service
import { Profile, ContactForm } from '../models/index';

@Injectable({
  providedIn: 'root'
})
export class ProfileService {

  constructor(private apiService: ApiService) {}

  // Au lieu de chercher l'ID 1, on demande au nouveau service de donner le bon profil
  getProfile(): Observable<Profile> {
    return this.apiService.getFullProfileData();
  }

  sendContact(form: ContactForm): Observable<any> {
    return this.apiService.sendContact(form);
  }

  getMediaUrl(path?: string | null): string {
    return this.apiService.getMediaUrl(path);
  }
}