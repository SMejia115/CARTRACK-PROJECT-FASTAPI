import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree, Router } from '@angular/router';
import { Observable } from 'rxjs';
import { TokenGuardSellerLogin } from './sellerLogin.guard';
import { TokenGuardAdminLogin } from './adminLogin.guard';

@Injectable({
  providedIn: 'root'
})
export class CombinedTokenGuard implements CanActivate {
  constructor(private router: Router, private tokenGuard: TokenGuardSellerLogin, private tokenGuardAdmin: TokenGuardAdminLogin) {}

  canActivate(
    next: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {

    // Lógica para verificar si ambos TokenGuard y TokenGuardAdmin retornan falso
    const isTokenValid = this.tokenGuard.canActivate();
    const isAdminTokenValid = this.tokenGuardAdmin.canActivate();


    if (!isTokenValid && !isAdminTokenValid){
      this.router.navigate(['']);
      return !isTokenValid && !isAdminTokenValid;

    }else{
      return isTokenValid || isAdminTokenValid;
    }
  }
}