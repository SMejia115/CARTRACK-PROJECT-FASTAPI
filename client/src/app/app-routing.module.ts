import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { HeaderComponent } from './components/header/header.component';
import { HomeComponent } from './components/home/home.component';
import { UserRegistrationComponent } from './components/user-registration/user-registration.component';
import { ClientRegistrationComponent } from './components/client-registration/client-registration.component';
import { CarsViewComponent } from './components/cars-view/cars-view.component';
import { CarComponent } from './components/car/car.component';
import { CarListComponent } from './components/car-list/car-list.component';
import { TokenGuardAdmin } from './guards/admin.guard';
import { TokenGuardAdminLogin } from './guards/adminLogin.guard';
import { TokenGuardSeller } from './guards/seller.guard';
import { TokenGuardSellerLogin } from './guards/sellerLogin.guard';
import { CombinedTokenGuard } from './guards/combinedLogin.guard';
import { BuyComponent } from './components/buy/buy.component';
import { ClientListComponent } from './components/client-list/client-list.component';
import { AdminHomeComponent } from './components/admin-home/admin-home.component';
import { PersonalReportsComponent } from './components/personal-reports/personal-reports.component';
import { GeneralReportsComponent } from './components/general-reports/general-reports.component';


const routes: Routes = [
  {path : '', component : LoginComponent},
  {path : 'header', component : HeaderComponent},
  {path : 'home', component : HomeComponent, canActivate: [CombinedTokenGuard]},
  {path: 'clients', component: ClientListComponent},
  {path : 'user/registration', component : UserRegistrationComponent, canActivate: [TokenGuardAdmin]},
  {path : 'client/registration', component : ClientRegistrationComponent, canActivate: [CombinedTokenGuard]},
  {path: 'cars', component: CarsViewComponent, canActivate:[CombinedTokenGuard]},
  {path: 'car/:id', component: CarComponent, canActivate:[CombinedTokenGuard] },
  {path: 'list', component: CarListComponent , canActivate:[TokenGuardAdmin]},
  {path: 'buy', component: BuyComponent, canActivate:[CombinedTokenGuard]},
  {path: 'admin', component: AdminHomeComponent, canActivate:[TokenGuardAdmin]},
  {path: 'general/report', component: GeneralReportsComponent, canActivate:[TokenGuardAdmin]},
  {path: 'personal/report', component: PersonalReportsComponent, canActivate:[CombinedTokenGuard]},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
