import { Component, OnInit, Input } from '@angular/core';
import { WeatherService } from '../weather.service';
@Component({
  selector: 'app-seattle',
  templateUrl: './seattle.component.html',
  styleUrls: ['./seattle.component.css']
})
export class SeattleComponent implements OnInit {
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
