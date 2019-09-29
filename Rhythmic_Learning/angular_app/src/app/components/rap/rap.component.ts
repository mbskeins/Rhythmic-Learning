import { Component, OnInit, OnChanges, SimpleChanges, AfterViewInit } from '@angular/core';
import { SyncRhythemService } from 'src/app/services/SyncRhythem.service';
import { Observable } from 'rxjs';
import { HttpService } from '../../services/HttpService.service';
import { TtsInstance } from '../../models/TtsInstance'
import { trigger, transition, useAnimation } from '@angular/animations';
import { bounce, fadeIn, fadeOut } from 'ng-animate';
import {AudioRecordingService} from '../../services/audio-recording.service'
import { AdLib } from '../../models/AdLib';


@Component({
  selector: 'app-rap',
  templateUrl: './rap.component.html',
  styleUrls: ['./rap.component.scss'],
  providers: [HttpService, AudioRecordingService],
  animations: [
    trigger('fadeIn', [transition('* => *', useAnimation(fadeIn, {
      // Set the duration to 5seconds and delay to 2seconds
      params: { timing: 3, delay: 0 }
    }))])
  ],
})
export class RapComponent implements OnInit, AfterViewInit {
  title = 'RhythmicLearning';
  apiObject$: Observable<string[]>;
  uiText = {
    str: ""
  };
  getDataObj;
  test1 = false;
  fadeIn: any;
  topicText = "";
  private voices: SpeechSynthesisVoice[];

  private adLibs: AdLib[];
  private numberOfAdlibs: number;
  private selectedVoiceURI: string;
  
  constructor(
    private syncService: SyncRhythemService,
    private http: HttpService,
    private audioRecordingService: AudioRecordingService
    ){
      this.adLibs = [];
      this.numberOfAdlibs = 0;
      this.audioRecordingService.getRecordedBlob().subscribe((data) => {
        var url = URL.createObjectURL(data.blob);
        var adlibAudio = new Audio(url);
        ++this.numberOfAdlibs;
        this.adLibs.push(new AdLib(adlibAudio, this.numberOfAdlibs));
      });
    }

    ngOnInit(){
      var synth = window.speechSynthesis;
      setTimeout(() => {
        this.voices = synth.getVoices();
      }, 5);
      this.selectedVoiceURI = "Google UK English Male";
    }

  ngAfterViewInit(){

  }

  onKey(event: any) {
    this.topicText = event.target.value;
  }

  test(){
    // var ttsInstance = new TtsInstance("Pockets too big they sumo. Pockets too big they sumo. Pockets too big they sumo. Pockets too big they sumo. Pull a nigga card like Uno. Flip a nigga shit like Judo. You niggas act too culo. You a nerd no Chad Hugo. Pockets too big they sumo. Pockets too big they sumo. Pockets too big they sumo.", 22);
    // this.syncService.startTts(ttsInstance);
    console.log(this.selectedVoiceURI);
    var dataString;
    this.apiObject$ = this.http.getRapLyrics(this.topicText);
    this.apiObject$.subscribe(data => dataString = data);
    this.apiObject$.subscribe(data => {
      console.log(dataString);
      var dataStringTts;
      dataStringTts = new TtsInstance(dataString, 0);
      console.log(dataStringTts);
      this.syncService.startTts(dataStringTts, this.topicText);
    });
  }

  startRecording(){
    this.audioRecordingService.startRecording();
  }

  stopRecording(){
    this.audioRecordingService.stopRecording();
  }

  playAudio(numberToPlay: number){
    var index = numberToPlay - 1;
    this.adLibs[index].audio.play();
  }

  onSelectVoice(event: any){
    this.selectedVoiceURI = event.value;
    console.log(this.selectedVoiceURI);
  }
}