import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  scrollTo(number: number){
    window.scrollTo({
      top: (((window.outerHeight + window.innerHeight)/2) + 8) * number,
      behavior: 'smooth',
    });
  }
}
