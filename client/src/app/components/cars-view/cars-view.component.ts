import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-cars-view',
  templateUrl: './cars-view.component.html',
  styleUrls: ['./cars-view.component.css']
})
export class CarsViewComponent {
  constructor(private http: HttpClient, private router:Router) {}


  cars: any[] = [];

  ngOnInit(): void {
    this.obtainCars();
  }

  obtainCars(){
    this.http.get('http://localhost:5000/available/cars/images').subscribe(
      (response: any) => {
        this.cars = response;
      },
      (error: any) => {
        console.error('Error obtaining cars:', error);
      }
    );
  }

  viewProductPage(id: number){
    this.router.navigate([`/car/${id}`]);
  }
}
