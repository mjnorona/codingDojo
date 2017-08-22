import { Component } from '@angular/core';
import { NoteService } from './note.service';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  note = {
    content: ''
  }
  notes = {}
  constructor(private _noteService: NoteService) {}


  onSubmit() {
    console.log("in the correct function")
    console.log('line 15', this.note.content)
    this._noteService.create(this.note.content)
    .then(notes => console.log(notes))
    .catch(err => console.log(err))
  }
}
