import { Component, OnInit, OnChanges, SimpleChanges, AfterViewInit } from '@angular/core';
import { SyncRhythemService } from 'src/app/services/SyncRhythem.service';
import { Observable } from 'rxjs';
import { HttpService } from './services/HttpService.service';
import { TtsInstance } from './models/TtsInstance'
import { trigger, transition, useAnimation } from '@angular/animations';
import { bounce, fadeIn, fadeOut } from 'ng-animate';
import {AudioRecordingService} from './services/audio-recording.service'
import { AdLib } from './models/AdLib';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  providers: [HttpService, AudioRecordingService],
  animations: [
    trigger('fadeIn', [transition('* => *', useAnimation(fadeIn))]),
  ],
})
export class AppComponent implements OnInit, AfterViewInit {
  title = 'RhythmicLearning';
  apiObject$: Observable<string[]>;
  uiText = {
    str: ""
  };
  getDataObj;
  test1 = false;
  fadeIn: any;
  topicText = "";

  private adLibs: AdLib[];
  private numberOfAdlibs: number;
  private voices: SpeechSynthesisVoice[];
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
        ++this.numberOfAdlibs;
        this.adLibs.push(new AdLib(new Audio(url), this.numberOfAdlibs));
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

  onSelectVoice(event: any){
    this.selectedVoiceURI = event.value;
    console.log(this.selectedVoiceURI);
  }

  onKey(event: any) {
    this.topicText = event.target.value;
  }

  playBeatAndRapForTopic(){
    this.apiObject$ = this.http.getRapLyrics(this.topicText);
    this.apiObject$.subscribe((data) => {
      console.log(data);
      var test = ["Twinkle, twinkle, little, star", "How, I, wonder, what, you, are", "Up, above, the, world, so, high,", "Like, a, diamond, in, the, sky", "Twinkle, twinkle, little, star", "How, I, wonder, what, you, are", "When the blazing sun is gone", "When there's nothing he shines upon", "Then you show your little light", "Twinkle twinkle through the night", "Twinkle twinkle little star", "How I wonder what you are!", "In the dark blue sky so deep", "Through my curtains often peep", "For you never close your eyes", "Til the morning sun does rise", "Twinkle, twinkle, little star", "How I wonder what you are"];
      this.syncService.startTtsWithSentences(test, this.selectedVoiceURI);
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
}