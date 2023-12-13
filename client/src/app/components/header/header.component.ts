import { Component, OnInit } from '@angular/core';
import { LocalStorageService } from 'src/app/services/local-storage.service';
import { Router } from '@angular/router';
import jwt_decode from 'jwt-decode';



@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})


export class HeaderComponent implements OnInit{
  token: any;
  tokenData: any;
  firstName: any;
  lastName: any;

  role: any;


  constructor(private localStorageService: LocalStorageService, private router : Router) {}

  ngOnInit(): void {
    this.token = this.localStorageService.getItem('token');
    this.tokenData = jwt_decode(this.token);
    this.firstName = this.tokenData ? this.tokenData.user.firstName : null;
    this.lastName = this.tokenData ? this.tokenData.user.lastName : null;
    this.role = this.tokenData ? this.tokenData.user.role : null;
  }

  logout() {
    // Elimina el token del localStorage
    localStorage.removeItem('token');

    // Redirige al usuario a la página principal
    this.router.navigate(['/']);
  }

  navigateTo(route: string) {
    this.router.navigate([route]);
  }

}
