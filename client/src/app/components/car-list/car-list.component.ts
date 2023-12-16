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
  inEditModeIndex: number = -1;

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

  updateCar(car: any) {
    this.inEditModeIndex = -1;
    console.log(car);
    const carData = {...car};
    delete carData.carImages;
    if (typeof carData.soatDate !== 'string') {
      carData.soatDate = carData.soatDate.toISOString().split('T')[0];
    }
    if (typeof carData.tecnoDate !== 'string') {
      carData.tecnoDate = carData.tecnoDate.toISOString().split('T')[0];
    }
    console.log(carData);
    // Realiza la solicitud HTTP para actualizar el coche seleccionado en this.selectedCar.
    this.http.put(`http://localhost:5000/modify/cars/${carData.carID}`, carData)
      .subscribe(() => {
        // Actualización exitosa, puedes mostrar un mensaje de éxito.
        console.log('Car updated successfully');
        this.selectedCar = null;  // Cierra el formulario de modificación.
        this.loadCars();  // Vuelve a cargar la lista de coches.
      });
    
  }

  enterEditMode(index: number) {
    this.inEditModeIndex = index;
  }
}
