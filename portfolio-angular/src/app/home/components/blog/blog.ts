import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../../shared/services/api.service';
import { Article } from '../../../shared/models/index';

@Component({
  selector: 'app-blog',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './blog.html',
  styleUrl: './blog.scss',
})
export class Blog implements OnInit {

  articles: Article[] = [];

  constructor(
    private apiService: ApiService,
    private cdr: ChangeDetectorRef 
  ) {}

  ngOnInit(): void {
    this.apiService.getFullProfileData().subscribe({
      next: (data: any) => {
        this.articles = (data.articles || []).slice(0, 3);
        this.cdr.detectChanges();
      },
      error: (err: any) => console.error('Erreur Blog:', err)
    });
  }

  // Fonction pour gérer le clic sans remonter en haut
  openArticle(event: Event, article: Article): void {
    event.preventDefault(); // Bloque le comportement par défaut du '#'
    
    if (article.lien) {
      window.open(article.lien, '_blank');
    } else {
      // Si pas de lien, on affiche le contenu saisi dans Django
      alert(article.contenu || "Contenu en cours de rédaction...");
    }
  }

  getImageUrl(article: Article): string {
    return this.apiService.getMediaUrl(article.image);
  }

  formatDate(dateStr: string): string {
    if (!dateStr) return '';
    return new Date(dateStr).toLocaleDateString('fr-FR', {
      day: '2-digit', month: 'short', year: 'numeric'
    });
  }
}