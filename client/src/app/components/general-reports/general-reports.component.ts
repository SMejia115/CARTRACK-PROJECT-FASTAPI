import { select } from 'd3-selection'; // Asegúrate de importar los módulos de D3 necesarios
import { colorSets } from '@swimlane/ngx-charts';
import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-general-reports',
  templateUrl: './general-reports.component.html',
  styleUrls: ['./general-reports.component.css']
})
export class GeneralReportsComponent {

  salesData: any = [];
  sales: any = [];

  constructor (private http: HttpClient) { }

  ngOnInit() {
    this.http.get('http://localhost:5000/sales/sum').subscribe((data: any) => {
      this.salesData = data;
      console.log(this.salesData);
      console.log("Entró al get");
    });

    this.http.get('http://localhost:5000/sales').subscribe((data: any) => {
      this.sales = data;
      console.log(this.sales);
    });
  }
}
