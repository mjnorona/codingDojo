import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  date;
  clicked = ""
  timeZone = 0

  changedZone(input){
    this.clicked = input
    this.date = new Date()
    if (this.clicked === "PST"){
      this.date = new Date()
    } else if (this.clicked == "MST"){
      this.date.setHours(this.date.getHours() + 1)
    } else if (this.clicked == "CST"){
      this.date.setHours(this.date.getHours() + 2)
    } else if (this.clicked == "EST"){
      this.date.setHours(this.date.getHours() + 3)
    } else if (this.clicked == null) {
      this.date = null
    }
    
  }

}
