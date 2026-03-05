import { Component, OnInit, ChangeDetectorRef } from '@angular/core'; // Ajouté
import { CommonModule } from '@angular/common';
import { ApiService } from '../../../shared/services/api.service'; // Utilise ApiService
import { Project } from '../../../shared/models/index';

@Component({
  selector: 'app-portfolio',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './portfolio.html',
  styleUrl: './portfolio.scss',
})
export class Portfolio implements OnInit {

  allProjects: Project[] = [];
  filteredProjects: Project[] = [];
  categories: string[] = [];
  activeCategory = 'Tous';

  constructor(
    private apiService: ApiService,
    private cdr: ChangeDetectorRef // Injecté pour forcer l'affichage
  ) {}

  ngOnInit(): void {
    this.apiService.getFullProfileData().subscribe({
      next: (data: any) => {
        this.allProjects = data.projects || [];
        this.filteredProjects = this.allProjects;
        
        // Extraire les catégories uniques
        const cats = new Set(this.allProjects.map(p => p.categorie));
        this.categories = ['Tous', ...Array.from(cats)];
        
        this.cdr.detectChanges(); // ✅ TRÈS IMPORTANT : Force l'affichage des projets
        console.log('Projets chargés :', this.allProjects.length);
      },
      error: (err: any) => console.error('Erreur Portfolio:', err)
    });
  }

  filterBy(category: string): void {
    this.activeCategory = category;
    this.filteredProjects = category === 'Tous'
      ? this.allProjects
      : this.allProjects.filter(p => p.categorie === category);
    this.cdr.detectChanges(); // Force la mise à jour après filtrage
  }

  getImageUrl(project: Project): string {
    return this.apiService.getMediaUrl(project.image);
  }
}