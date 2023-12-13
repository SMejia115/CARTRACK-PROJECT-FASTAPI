import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ClientService {
  constructor(private http: HttpClient) {}

  obtainClientIDbyIdentificationNumber(identificationNumber: string): Observable<number> {
    return this.http.get(`http://localhost:5000/clients/identificationNumber/${identificationNumber}`)
      .pipe(map((response: any) => {
        if (response.clientID) {
          return response.clientID;
        } else {
          throw new Error('No se encontró el cliente.');
        }
      }));
  }
}