import { Component, OnInit, ChangeDetectorRef } from '@angular/core'; // Ajout de ChangeDetectorRef
import { CommonModule } from '@angular/common';
import { ApiService } from '../../../shared/services/api.service'; // Utilisation du service stable
import { Education, Experience, Skill } from '../../../shared/models/index';

@Component({
  selector: 'app-resume',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './resume.html',
  styleUrl: './resume.scss',
})
export class Resume implements OnInit {

  educations: Education[] = [];
  experiences: Experience[] = [];
  devSkills: Skill[] = [];
  networkSkills: Skill[] = [];

  constructor(
    private apiService: ApiService, // Utilise le bon service
    private cdr: ChangeDetectorRef  // Pour forcer le dessin des barres de skill
  ) {}

  ngOnInit(): void {
    this.apiService.getFullProfileData().subscribe({
      next: (data: any) => {
        this.educations = data.educations || [];
        this.experiences = data.experiences || [];
        
        // On trie les compétences par catégorie
        this.devSkills = (data.skills || []).filter((s: any) => s.categorie === 'dev' || s.categorie === 'outil');
        this.networkSkills = (data.skills || []).filter((s: any) => s.categorie === 'reseau');
        
        this.cdr.detectChanges(); // ✅ Indispensable pour l'animation des barres
      },
      error: (err: any) => console.error('Erreur Resume:', err)
    });
  }

  formatPeriod(debut: string, fin?: string): string {
    if (!debut) return '';
    const d = new Date(debut).getFullYear();
    const f = fin ? new Date(fin).getFullYear() : 'Présent';
    return `${d} — ${f}`;
  }
}