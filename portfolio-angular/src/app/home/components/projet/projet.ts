import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../../shared/services/api.service';
import { Profile } from '../../../shared/models/index';

@Component({
  selector: 'app-projet',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './projet.html',
  styleUrl: './projet.scss',
})
export class Projet implements OnInit {

  profile: Profile | null = null;

  constructor(
    private apiService: ApiService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.apiService.getFullProfileData().subscribe({
      next: (data: any) => {
        this.profile = data;
        this.cdr.detectChanges();
      },
      error: (err: any) => console.error('Erreur Projet Section:', err)
    });
  }
}