import { Component, OnInit } from '@angular/core';
import {SyncRhythemService} from 'src/app/services/SyncRhythem.service'
import {Howl, Howler} from 'howler'

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
    console.log("fuck");
    var sound = new Howl({
      src: ['sound.mp3'],
      onend: function() {
          console.log('Finished!');
      },
      onloaderror: function() {
          console.log('Error!');
      },
  }).play();
  }
}
