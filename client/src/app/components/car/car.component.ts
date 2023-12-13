import { Component } from '@angular/core';
import {Router, ActivatedRoute} from '@angular/router';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { CarsService } from 'src/app/services/cars.service';
import { OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { LocalStorageService } from 'src/app/services/local-storage.service'; // Importamos el servicio de localStorage para poder usarlo
import jwt_decode from 'jwt-decode';


// Definición de la estructura con la que se mandará el cuerpo de la petición
interface Sale {
  carID: number;
  saleDate: Date;
  clientID: number;
  sellerID: number;
  totalPrice: number;
}

@Component({
  selector: 'app-car',
  templateUrl: './car.component.html',
  styleUrls: ['./car.component.css']
})
export class CarComponent implements OnInit{
  car: any = {};
  images: string[] = [];
  carID = this.route.snapshot.params['id'];
  selectedImage: string = '';
  clientInfo: any = null;
  clientDocument: string = '';
  totalPrice: number = 0;
  clientNotFound: boolean = false;
  sellerToken: any = null;
  sellerID: any = null;
  decodeSellerToken: any = null;
  fechaActual: Date;
  fechaFormateada: string = '';
  clientID: number = 0;
  
  saleData : Sale = {
    carID: 0,
    saleDate: new Date(),
    clientID: 0,
    sellerID: 0,
    totalPrice: 0
  }

  headers = new HttpHeaders({
    'Content-Type': 'application/json' // Ajusta esto según el tipo de contenido que espera tu servidor
  });

  constructor(private router: Router, private route: ActivatedRoute, private http: HttpClient, private carsService: CarsService,
     private localStorageService: LocalStorageService ) { this.fechaActual = new Date(); };

  ngOnInit(): void {
    this.obtainCar();
    this.sellerToken = this.localStorageService.getItem('token'); // Obtenemos el ID del vendedor del localStorage
    this.decodeSellerToken = jwt_decode(this.sellerToken); // Decodificamos el token para obtener el ID del vendedor
    this.sellerID = this.decodeSellerToken.user.userID; // Obtenemos el ID del vendedor
    this.fechaFormateada = this.formatDate(this.fechaActual);
  }

  formatDate(date: Date): string {
    const day = date.getDate().toString().padStart(2, '0');
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const year = date.getFullYear();
    return `${day}/${month}/${year}`;
  }

  obtainCar(){
    this.http.get(`http://localhost:5000/car/images/${this.carID}`).subscribe(
      (response: any) => {
        this.car = response.car;
        for (const image of response.carImages) {
          this.images.push(image.ImageURL); // Agregamos cada URL de imagen al array "images"
        }
        this.selectedImage = this.images[0]; // Seleccionamos la primera imagen del array
        this.totalPrice = parseInt(this.car.appraisal) * 1.1;
      },
      (error: any) => {
        console.error('Error obtaining cars:', error);
      }
    );
  }

  getClientInfo() {
    this.http.get(`http://localhost:5000/clients/identificationNumber/${this.clientDocument}`).subscribe(
      (response: any) => {
        this.clientInfo = response;
        this.clientID = response.clientID;
        this.clientNotFound = false;
      },
      (error: any) => {
        this.clientNotFound = true;
        console.error('Error obteniendo información del cliente:', error);
      }
    );}

  changeImage(imageUrl: string): void {
    this.selectedImage = imageUrl;
  }

  registerSale(){
    console.log(this.clientInfo.clientID);
    console.log(this.sellerID);
    this.saleData.carID = this.carID;
    this.saleData.saleDate = new Date();
    this.saleData.clientID = parseInt(this.clientInfo.clientID, 10);
    this.saleData.sellerID = parseInt(this.sellerID, 10);
    this.saleData.totalPrice = this.totalPrice;
    console.log(this.saleData);


    this.http.post(`http://localhost:5000/sales/add`, this.saleData, { headers: this.headers }).subscribe(
      (response: any) => {
        console.log('Venta registrada:', response);
        window.alert("Venta registrada exitosamente");
        this.router.navigate([`/home`]);
      },
      (error: any) => {
        console.error('Error registrando la venta:', error);
      }
    );}






}
