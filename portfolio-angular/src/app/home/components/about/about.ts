import { Component, OnInit, ChangeDetectorRef } from '@angular/core'; // Import ChangeDetectorRef
import { CommonModule } from '@angular/common';
import { ApiService } from '../../../shared/services/api.service';
import { Profile } from '../../../shared/models/index';

@Component({
  selector: 'app-about',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './about.html',
  styleUrl: './about.scss',
})
export class About implements OnInit {
  profile: Profile | null = null;

  constructor(
    private apiService: ApiService,
    private cdr: ChangeDetectorRef // Injecte le détecteur de changements
  ) {}

  ngOnInit(): void {
    this.apiService.getFullProfileData().subscribe({
      next: (data: Profile) => {
        this.profile = data;
        // On force Angular à mettre à jour la vue immédiatement
        this.cdr.detectChanges(); 
        console.log('Données About chargées avec succès');
      },
      error: (err: any) => console.error('Erreur About:', err)
    });
  }

  getCvUrl(): string {
    return this.apiService.getMediaUrl(this.profile?.lien_cv);
  }

  getPhotoUrl(): string {
    return this.apiService.getMediaUrl(this.profile?.photo);
  }
}