import { Injectable, EventEmitter, Output } from '@angular/core';
import Speech from 'speak-tts'
import {Howl, Howler} from 'howler'
import { TtsInstance } from '../models/TtsInstance'

@Injectable({
  providedIn: 'root'
})
export class SyncRhythemService {
  private music: Howl;
  private isBeatPlaying: boolean;

constructor() { 
  console.log("SyncRhythem attached");
  this.music = new Howl({
    src: ['static/trap.mp3'],
    volume: 0.5,
    onend: () => {
      this.isBeatPlaying = false;
    }
  });
}

public startBeatAndLyrics(ttsInstance: TtsInstance){
  const sound = new Speech();
  sound.init({
    'volume': 1,
    'lang': 'en-GB',
    'rate': 1.05,
    'pitch': 1,
    'voice':'Microsoft Zira Desktop - English (United States)',
    'splitSentences': true
  });
  this.music.play();
  this.isBeatPlaying = true;
  setTimeout(() => {
    // sound.speak({
    //   text: ttsInstance.text,
    //   queue: false,
    //   listeners: {
    //     onstart: () => {
    //       //start ad libs
    //     }
    //   }
    // });
  }, ttsInstance.delay);
}

  public startTts(ttsInstance: TtsInstance){
    this.startBeatAndLyrics(ttsInstance);
  }
}