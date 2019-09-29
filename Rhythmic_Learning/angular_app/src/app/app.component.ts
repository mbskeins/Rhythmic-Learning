import { Component, OnInit, OnChanges, SimpleChanges, AfterViewInit } from '@angular/core';
import {SyncRhythemService} from 'src/app/services/SyncRhythem.service';
import { Observable } from 'rxjs';
import { HttpService } from './services/HttpService.service';
import { TtsInstance } from './models/TtsInstance'
import { trigger, transition, useAnimation } from '@angular/animations';
import { bounce, fadeIn, fadeOut } from 'ng-animate';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  providers: [HttpService],
  animations: [
    trigger('fadeIn', [transition('* => *', useAnimation(fadeIn))]),
  ],
})
export class AppComponent implements OnInit, AfterViewInit{
  title = 'RhythmicLearning';
  apiObject$: Observable<TtsInstance[]>;
  uiText = {str: ""};
  getDataObj;
  test1 = false;
  fadeIn: any;
  
  constructor(
    private syncService: SyncRhythemService,
    private http: HttpService,
    ){}

  ngOnInit(){
    //this.apiObject$ =this.http.getTestData();
  }

  ngAfterViewInit(){
    // console.log(this.apiObject$.subscribe(data => {
    //   //console.log(data);
    //   this.getDataObj = data;
    //   console.log("printing data object");
    //   console.log(this.getDataObj);
    // }))
  }

  onKey(event: any) {
    this.uiText = event.target.value;
  }

  test(){
    var list = [];
    list.push(new TtsInstance("Pockets too big they sumo. Pockets too big they sumo. Pockets too big they sumo. Pockets too big they sumo. Pull a nigga card like Uno. Flip a nigga shit like Judo. You niggas act too culo. You a nerd no Chad Hugo. Pockets too big they sumo. Pockets too big they sumo. Pockets too big they sumo.", 22));
    this.syncService.startTts(list, this.uiText);
    // this.apiObject$ = this.http.getTestData("this.uiText");
    // this.apiObject$.subscribe(data => {
    //   var list = [];
    //   list.push(new TtsInstance("Twinkle, twinkle, little star, How I wonder what you are. Up above the world so high, Like a diamond in the sky. When the blazing sun is gone, When he nothing shines upon, Then you show your little light, Twinkle, twinkle, all the night.", 22));
    //   this.syncService.startTts(list, this.uiText);
    // });
  }
}
