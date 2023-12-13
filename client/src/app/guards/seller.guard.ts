import { CanActivate } from '@angular/router';
import { Injectable } from '@angular/core';
import { LocalStorageService } from '../services/local-storage.service';
import { Router } from '@angular/router';
import { decodeToken } from '../helper/jwt.helper';

@Injectable({
  providedIn: 'root'
})

export class TokenGuardSeller implements CanActivate {
  constructor(private router: Router, private localStorageService : LocalStorageService) { }

   canActivate(): boolean {
    const token : any = decodeToken(this.localStorageService.getItem('token'));
    if (token.user.role === 'seller') {
      return true;
    } else {
      this.router.navigate(['']);
      return false;
    }
  }

}