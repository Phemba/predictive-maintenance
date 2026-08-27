import { Component } from '@angular/core';
import { CommonModule } from '@angular/common'; 
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

// Standalone component for the predictive maintenance form
@Component({
  imports: [CommonModule, FormsModule],
  selector: 'app-predict-form',
  styleUrl: './predict-form.css',
  templateUrl: './predict-form.html',
  standalone: true,
  
})
export class PredictForm {
  // Step1: properties matching the model backend fields
  type: number = 0;
  airTemperature: number = 298;
  processTemperature: number = 308;
  rotationalSpeed: number = 1500;
  torque: number = 40;
  toolWear: number = 0;

  // Step 2: Property to hold the prediction once we get one
  riskResult: number | null = null;

  //Dependency injection of HttpClient to make HTTP requests to the backend.
  constructor (private http: HttpClient) {}

  //Step5: Method to handle form submission and send data to the backend
  //Use snake_case for the payload keys to match the backend model
  onSubmit() {
    const payload = {
      type: this.type,
      air_temperature: this.airTemperature,
      process_temperature: this.processTemperature,
      rotational_speed: this.rotationalSpeed,
      torque: this.torque,
      tool_wear: this.toolWear
    };
    // .subscribe({next, error}) HTTP calls take time to complete,
    // use .subscribe to tell Angular "Run this code once the response comes back"
    // .next handles the successful response, .error handles any errors that occur during the request.

    this.http.post<{ risk: number }>('http://localhost:8000/predict', payload)
    .subscribe({
       next: (response) => {
      this.riskResult = response.risk;

       },
        error: (err) => {
          console.error('Prediction error:', err);
        }
    });
  }
}
