import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-quote-list',
  templateUrl: './quote-list.component.html',
  styleUrls: ['./quote-list.component.css']
})
export class QuoteListComponent implements OnInit {
  @Input() myQuotes
  @Output() upVoteEvent = new EventEmitter();
  @Output() downVoteEvent = new EventEmitter();
  @Output() deleteEvent = new EventEmitter();
  

  constructor() { }

  delete(index) {
    console.log(index)
    this.deleteEvent.emit(index)
  }

  upVote(index){
    this.upVoteEvent.emit(index)
  }

  downVote(index){
    this.downVoteEvent.emit(index)
  }

  ngOnInit() {

  }

}
