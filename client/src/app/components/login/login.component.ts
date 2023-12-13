import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
import jwt_decode from 'jwt-decode';

// import { JwtHelperService } from '@auth0/angular-jwt';

// Definición de la estructura con la que se mandará el cuerpo de la petición
interface User {
  userName: string;
  password: string;
}


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent{
  respuesta: any; //Variable que almacena la respuesta de la API
  //Deinición del objeto user


  userData: User = {
    userName: '',
    password: ''
  };

  apiUrl = 'http://localhost:5000/login'; //Ruta base de la API

  headers = new HttpHeaders({
    'Content-Type': 'application/json' // Ajusta esto según el tipo de contenido que espera tu servidor
  });

  //Constructor
  constructor(private http: HttpClient, private router: Router) { }


  //Función que se ejecuta al hacer click en el botón de login
  submitLogin(){

    // const getUserName = document.querySelector("#userNameInput") as HTMLInputElement;
    // const getPassword = document.querySelector("#passwordInput") as HTMLInputElement;
    // const username = getUserName.value;
    // const password = getPassword.value;

    // // Define las cabeceras de la solicitud (pueden variar según tu API)
    

    // //Se asignan los valores de los inputs a los valores del objeto user
    // this.userData = {
    //   userName: username,
    //   password: password,

    // };

    // Se hace la petición POST a la API para verificar si el usuario existe y la contraseña es correcta y retornar el token

    this.http.post(this.apiUrl, this.userData, { headers: this.headers }).subscribe(
      (response:any) => {
        // Maneja la respuesta aquí
        const token = response.token; // Asegúrate de que el token esté en la respuesta
        const decodedToken:any = jwt_decode(token);
        if (response.token){
          window.alert("Bienvenido " + decodedToken.user.firstName + " " + decodedToken.user.lastName);
          window.localStorage.setItem("token", JSON.stringify(response.token));
          let route = '/home';
          setTimeout(() => {
            this.router.navigate([route])
          }, 1000);
        }
      },
      (error) => {
        // Maneja errores aquí
        window.alert("Usuario o contraseña incorrectos.");
        console.error('Error:', error);
      }
    );

    //Se hace la petición GET a la API para verificar si el usuario existe
    // this.http.get(this.apiUrl + 'users/username' + '/'+ this.userData.username).subscribe( (response) => {
    //   if (response != null){
    //     const user = response as User;
    //     console.log(user);
    //    if (user.password == password){
    //       window.alert("Bienvenido " + this.userData.username);
    //       window.localStorage.setItem("username", this.userData.username);
    //       window.localStorage.setItem("password", this.userData.password);
    //       let route = '/home';
    //       setTimeout(() => {
    //         this.router.navigate([route])
    //       }, 1000);
    //     }
    //     else{
    //       window.alert("Contraseña incorrecta");
    //     }
    // }},
    // (error) => {
    //   console.error('Error al realizar la petición: ', error);
    //   window.alert("El usuario NO existe");
    // });

    

    };

  }

  



