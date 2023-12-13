import { CanActivate } from '@angular/router';
import { Injectable } from '@angular/core';
import { LocalStorageService } from '../services/local-storage.service';
import { Router } from '@angular/router';
import { decodeToken } from '../helper/jwt.helper';

@Injectable({
  providedIn: 'root'
})

export class TokenGuardSellerLogin implements CanActivate {
  constructor(private router: Router, private localStorageService : LocalStorageService) { }

   canActivate(): boolean {
    const token : any = this.localStorageService.getItem('token');

    if (token){
      const tokenDesencripted :any = decodeToken(token)
      if (tokenDesencripted.user.role === 'seller') {
        return true;
      }
    }
    return false;
    }
  }