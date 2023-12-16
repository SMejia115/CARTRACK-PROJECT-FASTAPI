import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms'; 
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { ClientService } from '../../services/client.service';
import { Router } from '@angular/router';

interface Car {
  brand: string;
  model: string;
  year: string;
  color: string;
  fuelType: string;
  chassisNumber: string;
  engineNumber: string;
  licensePlate: string;
  city: string;
  appraisal: number;
  cylinderCapacity: string;
  transitLicenseNumber: string;
  soatDate: Date;
  tecnoDate: Date;
  previousOwner: number;
  type: string;
  status: string;
}


@Component({
  selector: 'app-buy',
  templateUrl: './buy.component.html',
  styleUrls: ['./buy.component.css']
})
export class BuyComponent {
  nuevoAutoForm: FormGroup; 
  uploadedFiles: File[] = [];
  errorMessage: string = '';
  clientID: number = 0;
  status: string = 'available';

  carData: Car = {
    brand: '',
    model: '',
    year: '',
    color: '',
    fuelType: '',
    chassisNumber: '',
    engineNumber: '',
    licensePlate: '',
    city: '',
    appraisal: 0,
    cylinderCapacity: '',
    transitLicenseNumber: '',
    soatDate: new Date(),
    tecnoDate: new Date(),
    previousOwner: 0,
    type: '',
    status: ''
  };
  

  constructor(private formBuilder: FormBuilder, private http: HttpClient, private clientService: ClientService, private router: Router) {
    this.nuevoAutoForm = this.formBuilder.group({
      brand: ['', Validators.required],
      model: ['', Validators.required],
      year: ['', [Validators.required, Validators.pattern('^[0-9]{4}$')]],
      color: ['', Validators.required],
      fuelType: ['', Validators.required],
      chassisNumber: ['', [Validators.required, Validators.minLength(10), Validators.maxLength(17)]],
      engineNumber: ['', [Validators.required, Validators.minLength(10), Validators.maxLength(17)]],
      licensePlate: ['', [Validators.required, Validators.minLength(6), Validators.maxLength(7)]],
      city: ['', Validators.required],
      appraisal: [0, [Validators.required, Validators.min(1)]],
      cylinderCapacity: ['', Validators.required],
      transitLicenseNumber: ['', [Validators.required, Validators.minLength(10), Validators.maxLength(17)]],
      soatDate: [''],
      tecnoDate: [''],
      previousOwner: ['', [Validators.pattern('[0-9-]+')]],
      type: ['', Validators.required],
      status: [''],
    });
  }

  isSubmitButtonDisabled(): boolean {
    const requiredFields = [
      'brand',
      'model',
      'year',
      'color', 
      'fuelType',
      'chassisNumber',
      'engineNumber',
      'licensePlate',
      'city',
      'appraisal',
      'cylinderCapacity',
      'transitLicenseNumber',
      'type'
    ];

    for (const fieldName of requiredFields) {
      if (!this.nuevoAutoForm.get(fieldName)?.value) {
        return true; // Desactivar el botón si algún campo requerido está vacío
      }
    }

    return false; // Habilitar el botón si todos los campos requeridos están completos
  }

  onFileChange(event: Event) {
    const inputElement = event.target as HTMLInputElement;
    if (inputElement.files && inputElement.files.length > 0) {
      const files = inputElement.files;
      for (let i = 0; i < files.length; i++) {
        const file = files[i];
        if (this.isImageFile(file)) {
          this.uploadedFiles.push(file);
        } else {
          this.errorMessage = 'Error: solo se pueden agregar imágenes.';
        }
      }
    }
  }

  isImageFile(file: File): boolean {
    // Verifica si la extensión del archivo corresponde a una imagen (puedes personalizar esta lógica)
    const allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;
    return allowedExtensions.test(file.name);
  }

  onSubmit() {
    // Realiza la solicitud para obtener el clientID y luego procesa el formulario
    this.getClientID().subscribe((clientId: number) => {
      // En este punto, la solicitud HTTP ha completado y has obtenido el clientID
  
      this.carData.brand = this.nuevoAutoForm.value.brand;
      this.carData.model = this.nuevoAutoForm.value.model;
      this.carData.year = this.nuevoAutoForm.value.year;
      this.carData.color = this.nuevoAutoForm.value.color;
      this.carData.fuelType = this.nuevoAutoForm.value.fuelType;
      this.carData.chassisNumber = this.nuevoAutoForm.value.chassisNumber;
      this.carData.engineNumber = this.nuevoAutoForm.value.engineNumber;
      this.carData.licensePlate = this.nuevoAutoForm.value.licensePlate;
      this.carData.city = this.nuevoAutoForm.value.city;
      this.carData.appraisal = this.nuevoAutoForm.value.appraisal;
      this.carData.cylinderCapacity = this.nuevoAutoForm.value.cylinderCapacity;
      this.carData.transitLicenseNumber = this.nuevoAutoForm.value.transitLicenseNumber;
      this.carData.soatDate = this.nuevoAutoForm.value.soatDate;
      this.carData.tecnoDate = this.nuevoAutoForm.value.tecnoDate;
      this.carData.previousOwner = clientId;
      this.carData.type = this.nuevoAutoForm.value.type;
      this.carData.status = this.status;


      // Define las cabeceras de la solicitud
      const headers = new HttpHeaders({
        'Content-Type': 'application/json' // Ajusta esto según el tipo de contenido que espera tu servidor
      });
      


      // Realiza una solicitud POST para guardar el auto con los datos actualizados
      this.http.post('http://localhost:5000/cars', this.carData, { headers }).subscribe(
        (response: any) => {
          // Maneja la respuesta del servidor, por ejemplo, muestra un mensaje de éxito
          console.log('Auto guardado exitosamente:', response);
          // Ahora, envía las imágenes
          this.uploadImagesSequentially(this.carData.licensePlate, this.uploadedFiles).then(
            () => {
              console.log('Imágenes cargadas exitosamente.');
              window.alert('Auto registrado exitosamente.');
              let route = '/home';
              setTimeout(() => {
                this.router.navigate([route])
              }, 1000);
            },
            (error: any) => {
              console.error('Error al cargar las imágenes:', error);
            }
          );
        },
        (error: any) => {
          // Maneja errores, muestra un mensaje de error, etc.
          console.error('Error al guardar el auto:', error);
        }
      );
    });

  }
  
  getClientID() {
    // Realiza la solicitud HTTP para obtener el clientID
    return this.clientService.obtainClientIDbyIdentificationNumber(this.nuevoAutoForm.value.previousOwner);
  }

  uploadImage(licensePlate: string, file: File): Promise<void> {
    return new Promise<void>((resolve, reject) => {
      const formData = new FormData();
      formData.append('image', file);

      const headers = new HttpHeaders();

      this.http.post(`http://localhost:5000/image/add/licensePlate/${licensePlate}`, formData, { headers })
        .subscribe(
          () => {
            console.log(`Imagen ${file.name} cargada exitosamente.`);
            resolve();
          },
          (error: any) => {
            console.error(`Error al cargar la imagen ${file.name}:`, error);
            reject(error);
          }
        );
    });
  }

  uploadImagesSequentially(licensePlate: string, files: File[]): Promise<void> {
    let promise = Promise.resolve();

    for (const file of files) {
      promise = promise.then(() => this.uploadImage(licensePlate, file));
    }

    return promise;
  }
}