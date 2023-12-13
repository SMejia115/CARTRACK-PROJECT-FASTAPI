import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-car-list',
  templateUrl: './car-list.component.html',
  styleUrls: ['./car-list.component.css']
})
export class CarListComponent implements OnInit {
  cars?: any[];  // Esta variable almacenará la lista de coches disponibles.
  selectedCar: any;  // Esta variable se utilizará para almacenar el coche seleccionado para su modificación.

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.loadCars();
  }

  loadCars() {
    this.http.get('http://localhost:5000/available/cars/images')
      .subscribe((data: any) => {
        this.cars = data;
      });
  }

  openModificationForm(car: any) {
    this.selectedCar = car;
  }

  updateCar() {
    // Realiza la solicitud HTTP para actualizar el coche seleccionado en this.selectedCar.
    this.http.put(`http://localhost:5000/modify/cars/${this.selectedCar.carID}`, this.selectedCar)
      .subscribe(() => {
        // Actualización exitosa, puedes mostrar un mensaje de éxito.
        console.log('Car updated successfully');
        this.selectedCar = null;  // Cierra el formulario de modificación.
        this.loadCars();  // Vuelve a cargar la lista de coches.
      });
  }
}
