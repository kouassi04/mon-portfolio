import { Component, OnInit, ChangeDetectorRef } from '@angular/core'; // Ajout de ChangeDetectorRef
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { ProfileService } from '../../../shared/services/profile.service';
import { Profile } from '../../../shared/models/index';

@Component({
  selector: 'app-contact',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './contact.html',
  styleUrl: './contact.scss',
})
export class Contact implements OnInit {

  profile: Profile | null = null;
  formData = { nom_complet: '', email: '', objet: '', message: '' };
  sending = false;
  sent = false;
  hasError = false;

  constructor(
    private profileService: ProfileService, 
    private http: HttpClient,
    private cdr: ChangeDetectorRef // Injecté pour stabiliser l'affichage
  ) {}

  ngOnInit(): void {
    this.profileService.getProfile().subscribe({
      next: (data: any) => { // Ajout du type : any
        this.profile = data;
        this.cdr.detectChanges(); // ✅ Fixe l'erreur NG0100
      },
      error: (err: any) => console.error('Erreur Contact:', err)
    });
  }

  sendMessage(): void {
    if (!this.formData.nom_complet || !this.formData.email || !this.formData.message) {
      alert('Veuillez remplir tous les champs obligatoires.');
      return;
    }
    this.sending = true;
    this.hasError = false;

    // Utilisation de l'URL directe ou via service
    this.http.post('http://localhost:8000/api/contact/', this.formData).subscribe({
      next: () => {
        this.sent = true;
        this.sending = false;
        this.formData = { nom_complet: '', email: '', objet: '', message: '' };
        this.cdr.detectChanges();
      },
      error: (err: any) => {
        this.hasError = true;
        this.sending = false;
        this.cdr.detectChanges();
        console.error('Erreur envoi message:', err);
      }
    });
  }
}