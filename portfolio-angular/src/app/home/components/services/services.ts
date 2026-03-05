import { Component, OnInit, ChangeDetectorRef } from '@angular/core'; // Ajouté
import { CommonModule } from '@angular/common';
import { ApiService } from '../../../shared/services/api.service'; // Utilise ApiService directement
import { Service } from '../../../shared/models/index';

@Component({
  selector: 'app-services',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './services.html',
  styleUrl: './services.scss',
})
export class Services implements OnInit {

  services: Service[] = [];

  constructor(
    private apiService: ApiService, // On utilise ApiService pour avoir l'ID 2
    private cdr: ChangeDetectorRef  // Injecté pour forcer l'affichage
  ) {}

  ngOnInit(): void {
    this.apiService.getFullProfileData().subscribe({
      next: (data: any) => {
        // On récupère la liste des services assemblée par ton service
        this.services = data.services || [];
        this.cdr.detectChanges(); // ✅ Force Angular à dessiner les cartes de services
        console.log('Services chargés depuis Django:', this.services);
      },
      error: (err: any) => console.error('Erreur Services:', err)
    });
  }
}