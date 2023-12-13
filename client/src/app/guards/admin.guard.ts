import { LocalStorageService } from '../services/local-storage.service';
import { Router } from '@angular/router';
import { decodeToken } from '../helper/jwt.helper';
import jwt_decode from 'jwt-decode';
import { CanActivate } from '@angular/router';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})

export class TokenGuardAdmin implements CanActivate {
  constructor(private router: Router, private localStorageService : LocalStorageService) { }

   canActivate(): boolean {
    const token:string = this.localStorageService.getItem('token')
    const tokenDesencripted:any  = decodeToken(token)

    if (tokenDesencripted.user.role === 'admin') {
      return true;
    } else {
      this.router.navigate(['']);
      return false;
    }
  }

}

// export const adminGuard: CanActivateFn = (route, state) => {
//   return true;
// };