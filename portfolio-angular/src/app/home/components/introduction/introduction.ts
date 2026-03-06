import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../../shared/services/api.service';
import { Profile } from '../../../shared/models/index';

@Component({
  selector: 'app-introduction',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './introduction.html',
  styleUrl: './introduction.scss',
})
export class Introduction implements OnInit {
  // Valeurs par défaut pour éviter les erreurs d'affichage initiales
  profile: Profile = {
    nom: 'KOUASSI',
    prenom: 'SAMUEL',
    photo: '',
    socials: [],
    skills: [],
    stats: [],
    services: []
  } as any;

  constructor(
    private apiService: ApiService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.apiService.getFullProfileData().subscribe({
      next: (data: Profile) => {
        this.profile = data;
        this.cdr.detectChanges(); // Force la mise à jour de la vue pour la photo
        console.log('Photo Intro synchronisée !');
      },
      error: (err: any) => {
        console.error('Erreur Intro:', err);
      }
    });
  }

  /**
   * Récupère l'URL de la photo.
   * Si la photo est présente sur le backend Render, on l'utilise.
   * Sinon, on utilise l'image locale stockée dans assets.
   */
  getPhotoUrl(): string {
    if (this.profile && this.profile.photo) {
      return this.apiService.getMediaUrl(this.profile.photo);
    }
    // Chemin vers ton image locale sur Vercel
    return 'assets/img/samuel.jpg'; 
  }
}