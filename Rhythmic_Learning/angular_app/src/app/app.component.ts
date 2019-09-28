import { Component, OnInit, OnChanges, SimpleChanges, AfterViewInit } from '@angular/core';
import {SyncRhythemService} from 'src/app/services/SyncRhythem.service';
import { Observable } from 'rxjs';
import { HttpService } from './services/HttpService.service';
import { TtsInstance } from './models/TtsInstance'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  providers: [HttpService]
})
export class AppComponent implements OnInit, AfterViewInit{
  title = 'RhythmicLearning';
  apiObject$: Observable<TtsInstance[]>;
  userInput = '';
  getDataObj;
  
  constructor(
    private syncService: SyncRhythemService,
    private http: HttpService,
    ){}

  ngOnInit(){
    this.apiObject$ =this.http.getTestData();
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
    this.userInput = event.target.value;
  }

  test(){
    this.http.postTopic(this.userInput);
    this.apiObject$.subscribe(data => {
      this.syncService.startTts(data);
    });
  }
}
