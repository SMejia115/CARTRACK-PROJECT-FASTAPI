import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { switchMap } from 'rxjs/operators';
import { of } from 'rxjs';
import { Router } from '@angular/router';

declare const pdfjsLib: any; // Declaración de la biblioteca PDF.js

@Component({
  selector: 'app-client-registration',
  templateUrl: './client-registration.component.html',
  styleUrls: ['./client-registration.component.css']
})
export class ClientRegistrationComponent {
  selectedFile: File | null = null;
  selectedFileURL: string |null = null;
  selectedFileName: string = ''; // Variable para almacenar el nombre del archivo
  clientForm: FormGroup;

  apiUrl = 'http://localhost:5000/clients'; // Reemplaza con la URL de tu API
  headers = new HttpHeaders({ 'Content-Type': 'application/json' });

  constructor(private http: HttpClient, private formBuilder: FormBuilder, private router: Router) {
    this.clientForm = this.formBuilder.group({
      identificationNumber: ['', [Validators.required, Validators.maxLength(30), Validators.minLength(10), Validators.pattern('[0-9-]+')]],
      firstName: ['', [Validators.required, Validators.maxLength(20), Validators.pattern('[a-zA-Z]+')]],
      secondName: ['', [Validators.maxLength(20),  Validators.pattern('[a-zA-Z]+')]],
      lastName: ['', [Validators.required, Validators.maxLength(20), Validators.pattern('[a-zA-Z]+')]],
      address: ['', [Validators.required]],
      phone: ['', [Validators.required, Validators.maxLength(15), Validators.pattern('[0-9-]+')]],
      boolReports: [false, Validators.required],
      });
  }

  isSubmitButtonDisabled(): boolean {
    const requiredFields = ['identificationNumber', 'firstName', 'lastName', 'address', 'phone'];
  
    for (const fieldName of requiredFields) {
      if (!this.clientForm.get(fieldName)?.value) {
        return true; // Desactivar el botón si algún campo requerido está vacío
      }
    }
  
    return false; // Habilitar el botón si todos los campos requeridos están completos
  }

  onSubmit() {
    const clientData = this.clientForm.value;
    
    if (!this.selectedFile && clientData.boolReports) {
      window.alert('Por favor, seleccione un archivo PDF.');
      return;
    }

    const fileData = new FormData();
    // Agrega el archivo al FormData

    // Realiza una solicitud POST para guardar el cliente y el archivo
    this.http.post(this.apiUrl, clientData, { headers: this.headers }).subscribe(
      (clientResponse) => {
        console.log('Cliente registrado:', clientResponse);
        // Ahora, envía el archivo
        if (this.selectedFile && clientData.boolReports) {
          fileData.append('report', this.selectedFile, this.selectedFileName);
          this.uploadFile(fileData);
          window.alert('Cliente registrado con éxito.');
        } else{
          window.alert('Cliente registrado con éxito.');
        }
        
        let route = '/home';
          setTimeout(() => {
            this.router.navigate([route])
          }, 1000);
      },
      (error) => {
        console.error('Error al registrar el cliente:', error);
        window.alert('Error al registrar el cliente: ' + error.message);
      }
    );
  }

  // Función para cargar el archivo al servidor
  uploadFile(fileData: FormData): void {
    this.http.post(this.apiUrl + `/report/add/${this.clientForm.get('identificationNumber')?.value}`, fileData).subscribe(
      (fileUploadResponse) => {
        console.log('Archivo PDF cargado:', fileUploadResponse);
        // Puedes redirigir al usuario a una página de éxito o realizar otras acciones necesarias.
      },
      (error) => {
        console.error('Error al cargar el archivo PDF:', error);
      }
    );
  }

// Función para abrir el explorador de archivos al hacer clic en el botón "Seleccionar Archivo"
selectFile(): void {
  const fileInput = document.getElementById('fileInput');
  if (fileInput) {
    fileInput.click(); // Simula hacer clic en el elemento de entrada de archivo
  }
}


onFileSelected(event: any): void {
  const files: FileList = event.target.files;
  if (files.length > 0) {
    this.selectedFile = files[0];
    this.selectedFileName = this.selectedFile.name; // Almacena el nombre del archivo seleccionado

    if (this.selectedFile.type === 'application/pdf') {
      // Cargar y mostrar el PDF
      this.loadAndDisplayPdf(this.selectedFile);
    } else {
      // Manejar errores si el archivo no es un PDF
      window.alert('El archivo seleccionado no es un PDF.');
    }
  }
}

loadAndDisplayPdf(pdfFile: File): void {
  const fileReader = new FileReader();
  fileReader.onload = (e: any) => { // Agrega anotación de tipo any aquí
    const arrayBuffer = e.target.result;

    pdfjsLib.getDocument(arrayBuffer).promise.then((pdf: any) => { // Agrega anotación de tipo any aquí
      pdf.getPage(1).then((page: any) => { // Agrega anotación de tipo any aquí
        const canvas: HTMLCanvasElement = document.getElementById('pdf-canvas') as HTMLCanvasElement;
        const context = canvas.getContext('2d');

        const viewport = page.getViewport({ scale: 1 });
        canvas.width = viewport.width;
        canvas.height = viewport.height;

        const renderContext = {
          canvasContext: context,
          viewport: viewport,
        };

        page.render(renderContext);
      });
    });
  };

  fileReader.readAsArrayBuffer(pdfFile);
}


}