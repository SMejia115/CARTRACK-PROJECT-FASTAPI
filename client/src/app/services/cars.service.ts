import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CarsService {

  private urlApi = 'http://localhost:5000/cars';

  constructor(private http: HttpClient) { }

  public getCars(): Observable<any> {
    return this.http.get(this.urlApi);
  }

  public getCar(id: Number): Observable<any> {
    return this.http.get(this.urlApi + '/' + id);
  }

}
