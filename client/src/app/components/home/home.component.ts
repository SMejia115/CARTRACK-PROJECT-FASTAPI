import { Component } from '@angular/core';
import { Router } from '@angular/router';
import jwt_decode from 'jwt-decode';
import { LocalStorageService } from 'src/app/services/local-storage.service';

 

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {  
  token: any = this.localStorageService.getItem('token');

  tokenDesencripted(): any {
    return jwt_decode(this.token);
  }

  getRole(): boolean {
    return this.tokenDesencripted().user.role === 'admin';
  }


 constructor(private router: Router, private localStorageService: LocalStorageService  ) { }

  navigateTo(route: string) {
    this.router.navigate([route]);
  }
  

}
