import { Component, OnInit } from '@angular/core';
import {SyncRhythemService} from 'src/app/services/SyncRhythem.service';
import { Observable } from 'rxjs';
import { HttpService } from './services/HttpService.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  providers: [HttpService]
})
export class AppComponent implements OnInit{
  title = 'RhythmicLearning';
  apiObject$: Observable<object>[];
  userInput = '';
  
  constructor(
    private syncService: SyncRhythemService,
    private http: HttpService,
    ){}

  ngOnInit(){
    this.http.getData();
  }

  onKey(event: any) {
    this.userInput = event.target.value;
  }

  test(){
    this.http.postTopic(this.userInput);
    //this.syncService.startTts();
  }
}
