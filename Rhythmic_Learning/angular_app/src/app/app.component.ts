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
    this.apiObject$ = this.http.getTestData(this.uiText);


    this.apiObject$.subscribe(data => {
      this.syncService.startTts(data, this.uiText);
    });
  }
}
