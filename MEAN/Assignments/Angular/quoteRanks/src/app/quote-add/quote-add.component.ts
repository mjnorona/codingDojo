import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-quote-add',
  templateUrl: './quote-add.component.html',
  styleUrls: ['./quote-add.component.css']
})
export class QuoteAddComponent implements OnInit {
  @Output() myEvent = new EventEmitter();
  
  quote = {
    submission: '',
    author: '',
    votes: 0
  }  

  callParent() {
    this.myEvent.emit(this.quote);
  }
  ngOnInit() {
  }

}
