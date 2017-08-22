import { Component, OnInit, Input } from '@angular/core';
import { WeatherService } from '../weather.service';
@Component({
  selector: 'app-burbank',
  templateUrl: './burbank.component.html',
  styleUrls: ['./burbank.component.css']
})
export class BurbankComponent implements OnInit {
  @Input() currentWeather;

  ngOnInit() {
  }
  weather = {}
  constructor(private _weatherService: WeatherService){}
  getWeather(city) {
    this._weatherService.retrieveWeather(city)
    .then(weather => this.weather = weather)
    .catch(err => console.log(err))
  }
}
