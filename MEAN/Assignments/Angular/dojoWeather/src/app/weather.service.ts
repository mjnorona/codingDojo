import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/toPromise';
@Injectable()
export class WeatherService {

  constructor(private _http: Http) { }

  retrieveWeather(input) {
    var url = 'http://api.openweathermap.org/data/2.5/weather?q=' + input + '&&appid=fb9e2f474d95e73d1915d5b97fcf1e84'
    console.log(url)
    return this._http.get(url).map(data=>data.json()).toPromise()
  }
}
