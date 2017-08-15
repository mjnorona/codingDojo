import { Component } from '@angular/core';
import { NgModel } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  quotes = []
  invoke(event) {
    var temp = JSON.parse(JSON.stringify(event));
    this.quotes.push(temp)
    console.log("invoked", event)
    // for (var x of this.quotes){
    //   console.log(x.submission)
    //   console.log('go')
    // }
  }

  delete(event) {
    this.quotes.splice(event, 1)
  }

  upVote(event){
    this.quotes[event].votes++
  }

  downVote(event){
    this.quotes[event].votes--
  }
}
