import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})


export class AppComponent {
  email1 = {
    email: 'marcusj@gmail.com',
    importance: true,
    subject: 'computer science',
    content: 'operating systems is something i need to learn'
  }
  email2 = {
    email: 'jazz@gmail.com',
    importance: false,
    subject: 'modeling',
    content: 'nothing really special'
  }
  emails = [this.email1, this.email2]

}

class Email {
  email: string;
  importance: boolean;
  subject: string;
  content: string;

  constructor(email: string, importance: boolean, subject: string, content: string){
    this.email = name;
    this.importance = importance;
    this.subject = subject;
    this.content = content;
  }
}