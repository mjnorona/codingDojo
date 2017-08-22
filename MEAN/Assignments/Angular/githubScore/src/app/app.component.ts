import { Component } from '@angular/core';
import { TaskService } from './task.service';
import { NgModel } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  userInfo = {
    username: ''
  }

  user = {};
  score = 0;
  followers = 0;
  repos = 0;

  constructor(private _taskService: TaskService){}

  getUser() {
    console.log(this.userInfo.username)
    this._taskService.retrieveUser(this.userInfo.username)
    .then(user => 
      this.getInfo(user)
      
    )
    .catch(err => console.log(err))
    
    
  }

  getInfo(input) {
    this.user = input
    console.log(this.user['repos_url'])

    //
    this._taskService.retrieveRepos(this.user['repos_url'])
    .then(repos => this.score += repos.length)
    .catch(err => console.log(err))

    this._taskService.retrieveFollowers(this.user['followers_url'])
    .then(followers => this.score  += followers.length)
    .catch(err => console.log(err))
  }
}
