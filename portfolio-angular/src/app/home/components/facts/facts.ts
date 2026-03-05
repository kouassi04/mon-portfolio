import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProfileService } from '../../../shared/services/profile.service';
import { Stat } from '../../../shared/models/index';

@Component({
  selector: 'app-facts',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './facts.html',
  styleUrl: './facts.scss',
})
export class Facts implements OnInit {

  stats: Stat[] = [];

  constructor(private profileService: ProfileService) {}

  ngOnInit(): void {
    this.profileService.getProfile().subscribe({
      next: (data) => this.stats = data.stats || [],
      error: (err) => console.error('Erreur Facts:', err)
    });
  }
}