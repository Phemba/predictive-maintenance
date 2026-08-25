import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  imports: [CommonModule, FormsModule],
  selector: 'app-predict-form',
  styleUrl: './predict-form.css',
  templateUrl: './predict-form.html',
  standalone: true,
  
})
export class PredictForm {
  //Matching backend fields
  type: number = 0;
  airTemperature: number = 298;
  processTemperature: number = 308;
  rotationalSpeed: number = 1500;
  torque: number = 40;
  toolWear: number = 0;

  riskResult: number | null = null;

  //FastAPI request from frontend to backend
  constructor (private http: HttpClient) {}

  onSubmit() {
    const payload = {
      type: this.type,
      airTemperature: this.airTemperature,
      processTemperature: this.processTemperature,
      rotationalSpeed: this.rotationalSpeed,
      torque: this.torque,
      toolWear: this.toolWear
    };
    // Send the payload to the FastAPI backend
    // use .subscribe to handle the response
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
