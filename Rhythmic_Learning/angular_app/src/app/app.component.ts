import { Component, OnInit, OnChanges, SimpleChanges, AfterViewInit } from '@angular/core';
import {SyncRhythemService} from 'src/app/services/SyncRhythem.service';
import { Observable } from 'rxjs';
import { HttpService } from './services/HttpService.service';
import { TtsInstance } from './models/TtsInstance'
import { trigger, transition, useAnimation } from '@angular/animations';
import { bounce, fadeIn, fadeOut } from 'ng-animate';
import {AudioRecordingService} from './services/audio-recording.service'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  providers: [HttpService, AudioRecordingService],
  animations: [
    trigger('fadeIn', [transition('* => *', useAnimation(fadeIn))]),
  ],
})
export class AppComponent implements OnInit, AfterViewInit{
  title = 'RhythmicLearning';
  apiObject$: Observable<TtsInstance[]>;
  uiText = {
    str: ""
  };
  getDataObj;
  test1 = false;
  fadeIn: any;
  topicText = "";

  private adlibAudio: any;
  private isAdLibButtonDown: boolean;
  
  constructor(
    private syncService: SyncRhythemService,
    private http: HttpService,
    private audioRecordingService: AudioRecordingService
    ){
      this.audioRecordingService.getRecordedBlob().subscribe((data) => {
        var url = URL.createObjectURL(data.blob);
        this.adlibAudio = new Audio(url);
      });
      syncService.playAudio.subscribe({
        next: () => this.playAudio()
      })
    }

  ngOnInit(){

  }

  ngAfterViewInit(){

  }

  onKey(event: any) {
    this.topicText = event.target.value;
  }

  test(){
    var list = [];
    this.syncService.startTts(new TtsInstance("Pockets too big they sumo. Pockets too big they sumo. Pockets too big they sumo. Pockets too big they sumo. Pull a nigga card like Uno. Flip a nigga shit like Judo. You niggas act too culo. You a nerd no Chad Hugo. Pockets too big they sumo. Pockets too big they sumo. Pockets too big they sumo.", 22));
    //this.syncService.startTts(list, this.uiText);
    // this.apiObject$ = this.http.getTestData("this.uiText");
    // this.apiObject$.subscribe(data => {
    //   var list = [];
    //   list.push(new TtsInstance("Twinkle, twinkle, little star, How I wonder what you are. Up above the world so high, Like a diamond in the sky. When the blazing sun is gone, When he nothing shines upon, Then you show your little light, Twinkle, twinkle, all the night.", 22));
    //   this.syncService.startTts(list, this.uiText);
    // });
  }

  startRecording(){
    this.audioRecordingService.startRecording();
  }

  stopRecording(){
    this.audioRecordingService.stopRecording();
  }

  playAudio(){
    if(this.isAdLibButtonDown){
      this.adlibAudio.play();
    }
  }

  preview(){
    this.adlibAudio.play();
  }

  toggleAdlib(){
    this.isAdLibButtonDown = !this.isAdLibButtonDown;
  }
}
