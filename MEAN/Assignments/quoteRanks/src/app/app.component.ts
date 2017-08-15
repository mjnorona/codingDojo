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

  compare(a,b) {
    if (a['votes'] < b['votes'])
      return 1;
    if (a['votes']> b['votes'])
      return -1;
    return 0;
  }

  
  delete(event) {
    this.quotes.splice(event, 1)
  }

  upVote(event){
    this.quotes[event].votes++
    this.quotes.sort(this.compare)
    console.log("new list")
    for (var quote of this.quotes){
      console.log(quote['votes'])
    }
  }

  downVote(event){
    this.quotes[event].votes--
    this.quotes.sort(this.compare)
    console.log("new list")
    for (var quote of this.quotes){
      console.log(quote['votes'])
    }
  }
}
