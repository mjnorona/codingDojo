import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/toPromise';
@Injectable()
export class TaskService {

  constructor(private _http: Http) {}

  
  retrieveUser(user) {
    var url = 'https://api.github.com/users/' + user
    console.log(url)
    return this._http.get(url).map(data=>data.json()).toPromise()
  }

  retrieveRepos(url){
    return this._http.get(url).map(data=>data.json()).toPromise()
  }

  retrieveFollowers(url){
    return this._http.get(url).map(data=>data.json()).toPromise()
  }


}
