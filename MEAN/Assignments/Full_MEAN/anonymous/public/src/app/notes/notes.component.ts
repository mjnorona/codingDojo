import { Component, OnInit } from '@angular/core';
import { NoteService } from '../note.service';
@Component({
  selector: 'app-notes',
  templateUrl: './notes.component.html',
  styleUrls: ['./notes.component.css']
})
export class NotesComponent implements OnInit {
  notes = {}
  constructor(private _noteService: NoteService) { }

  ngOnInit() {
    this._noteService.retrieveNotes()
    .then(notes => {
      return this.notes = notes
    })
    .catch(err => console.log(err))
  }

  getAll() {
    
  }
}
