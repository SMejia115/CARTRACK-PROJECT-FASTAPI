import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { FormGroup, FormControl } from '@angular/forms'; 
import { Router } from '@angular/router';

// Definición de la estructura con la que se mandará el cuerpo de la petición
interface User {
  userName: string;
  password: string;
  identificationNumber: string;
  firstName: string;
  secondName: string;
  lastName: string;
  address: string;
  phone: string;
  role: string;
}


@Component({
  selector: 'app-user-registration',
  templateUrl: './user-registration.component.html',
  styleUrls: ['./user-registration.component.css']
})
export class UserRegistrationComponent {
  apiUrl = 'http://localhost:5000/users'; 
  headers = new HttpHeaders({ 'Content-Type': 'application/json' });

  userData: User = {
    userName: '',
    password: '',
    identificationNumber: '',
    firstName: '',
    secondName: '',
    lastName: '',
    address: '',
    phone: '',
    role: '',
  };

  constructor(private http: HttpClient, private router: Router) {

  };

  submitLogin() {
    this.http.post(this.apiUrl, this.userData, { headers: this.headers }).subscribe(
      (response: any) => {
        // Maneja la respuesta aquí
        window.alert("Usuario registrado exitosamente");
        console.log('Usuario registrado:', response);
        let route = '/home';
          setTimeout(() => {
            this.router.navigate([route])
          }, 1000);

        // Puedes redirigir al usuario a una página de éxito o realizar otras acciones necesarias.
      },
      (error: any) => {
        // Maneja errores aquÍ
        if (error.status == 409) {
          window.alert("Ya existe un usuario con el username '" + this.userData.userName + "'.");
        }else{
        window.alert("Error al registrar el usuario" + error);
      }
      }
    );
  }
}
