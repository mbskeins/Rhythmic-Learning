import { Component, OnInit } from '@angular/core';
import {SyncRhythemService} from 'src/app/services/SyncRhythem.service'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{
  title = 'RhythmicLearning';

  constructor(
    private syncService: SyncRhythemService,
    ){}

  ngOnInit(){
  }

  test(){
    this.syncService.startTts();
  }
}
