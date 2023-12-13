import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-client-list',
  templateUrl: './client-list.component.html',
  styleUrls: ['./client-list.component.css']
})
export class ClientListComponent implements OnInit {
  clients: any[] = [];  // Inicializa la lista de clientes como un array vacío.
  selectedClient: any;  // Almacena el cliente seleccionado para mostrar información detallada.

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.loadClients();
  }

  loadClients() {
    this.http.get('http://localhost:5000/clients')
      .subscribe((data: any) => {
        this.clients = data;
      });
  }

  showClientDetails(client: any) {
    this.selectedClient = client;
  }
}
