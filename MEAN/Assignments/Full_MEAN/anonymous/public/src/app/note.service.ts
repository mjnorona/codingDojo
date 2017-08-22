import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class NoteService {

  constructor(private _http: Http) { }
  retrieveNotes(){
    return this._http.get('/notes')
    .map(data => data.json())
    .toPromise()
  }

  create(note){
    console.log('going in create method '+ typeof(note))
    return this._http.post('/notes', {data: note})
    .map( data => data.json())
    .toPromise();
  }
}
