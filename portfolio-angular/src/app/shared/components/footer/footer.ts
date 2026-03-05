import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../../shared/services/api.service';
import { SocialNetwork } from '../../../shared/models/index';

@Component({
  selector: 'app-footer',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './footer.html',
  styleUrl: './footer.scss',
})
export class Footer implements OnInit {
  socials: SocialNetwork[] = [];

  constructor(
    private apiService: ApiService,
    private cdr: ChangeDetectorRef // Injecté pour stabiliser le rendu
  ) {}

  ngOnInit(): void {
    this.apiService.getFullProfileData().subscribe({
      next: (data) => {
        this.socials = data.socials || [];
        // On force la détection après le cycle actuel pour éviter l'erreur NG0100
        setTimeout(() => {
          this.cdr.detectChanges();
        }, 0);
      },
      error: (err) => console.error('Erreur Footer:', err)
    });
  }
}