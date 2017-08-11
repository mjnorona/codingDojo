import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  switches = ['on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on', 'on']
  
  pressed(index){
    console.log(index)
    console.log(this.switches[index])
    if (this.switches[index] == 'on'){
      this.switches[index] = 'off'
      console.log(index)
      console.log(this.switches[index])
    } else {
      this.switches[index] = 'on'
      console.log(index)
      console.log(this.switches[index])
    }
  }
}
