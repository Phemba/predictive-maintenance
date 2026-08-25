import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { PredictForm } from "./predict-form/predict-form";

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, PredictForm],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('frontend');
}
