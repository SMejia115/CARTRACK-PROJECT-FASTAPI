import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { LocalStorageService } from 'src/app/services/local-storage.service';
import jwt_decode from 'jwt-decode';

@Component({
  selector: 'app-personal-reports',
  templateUrl: './personal-reports.component.html',
  styleUrls: ['./personal-reports.component.css']
})
export class PersonalReportsComponent implements OnInit{

  sales: any = [];
  decodedToken: any = [];
  userID: any;

  constructor (private http: HttpClient, private localStorageService : LocalStorageService) { } 

  ngOnInit() {
    const token = this.localStorageService.getItem('token');
    this.decodedToken = jwt_decode(token);
    this.userID = this.decodedToken.user.userID;
    console.log(this.userID);


    this.http.get(`http://localhost:5000/sales/seller/${this.userID}`).subscribe((data: any) => {
      this.sales = data;
      console.log(this.sales);
      console.log("Entró al get");
    });
  }
}
