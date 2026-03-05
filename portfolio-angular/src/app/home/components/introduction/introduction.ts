import { Component, OnInit, ChangeDetectorRef } from '@angular/core'; // Ajoute ChangeDetectorRef
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
  // Garde tes valeurs par défaut pour custom.js
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
    private cdr: ChangeDetectorRef // Injecte-le
  ) {}

  ngOnInit(): void {
    this.apiService.getFullProfileData().subscribe({
      next: (data: Profile) => {
        this.profile = data;
        this.cdr.detectChanges(); // Force l'affichage de la photo
        console.log('Photo Intro synchronisée !');
      },
      error: (err: any) => console.error('Erreur Intro:', err)
    });
  }

  getPhotoUrl(): string {
    return this.apiService.getMediaUrl(this.profile?.photo);
  }
}