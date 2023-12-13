import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatOptionModule } from '@angular/material/core';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material/core';
import { HeaderComponent } from './components/header/header.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { HomeComponent } from './components/home/home.component';
import { UserRegistrationComponent } from './components/user-registration/user-registration.component';
import { ClientRegistrationComponent } from './components/client-registration/client-registration.component';
import { CarsViewComponent } from './components/cars-view/cars-view.component';
import { CarComponent } from './components/car/car.component';
import { CarListComponent } from './components/car-list/car-list.component';
import { BuyComponent } from './components/buy/buy.component';
import { ClientListComponent } from './components/client-list/client-list.component';
import { AdminHomeComponent } from './components/admin-home/admin-home.component';
import { PersonalReportsComponent } from './components/personal-reports/personal-reports.component';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { GeneralReportsComponent } from './components/general-reports/general-reports.component';





@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    HeaderComponent,
    HomeComponent,
    UserRegistrationComponent,
    ClientRegistrationComponent,
    CarsViewComponent,
    CarComponent,
    BuyComponent,
    AdminHomeComponent,
    CarListComponent,
    BuyComponent,
    PersonalReportsComponent,
    ClientListComponent,
    GeneralReportsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatSlideToggleModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatOptionModule,
    MatButtonModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    MatDatepickerModule,
    MatNativeDateModule,
    NgxChartsModule
  ],
  providers: [],
  bootstrap: [AppComponent]

})
export class AppModule { }
