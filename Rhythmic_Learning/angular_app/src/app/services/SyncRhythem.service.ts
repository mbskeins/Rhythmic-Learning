import { Injectable, EventEmitter, Output } from '@angular/core';
import Speech from 'speak-tts'
import {Howl, Howler} from 'howler'
import { TtsInstance } from '../models/TtsInstance'

@Injectable({
  providedIn: 'root'
})
export class SyncRhythemService {
  @Output() playAudio: EventEmitter<any> = new EventEmitter();

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

public getPlayAudioEmitter(){
  return this.playAudio;
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
    sound.speak({
      text: ttsInstance.text,
      queue: false,
      listeners: {
        onstart: () => {
          //start ad libs
        }
      }
    });
  }, ttsInstance.delay);
}

  public startTts(ttsInstance: TtsInstance){
    this.startBeatAndLyrics(ttsInstance);
    this.startAdlibs();
  }

  public startAdlibs(){
    var secondTotal = 0;
    var quarterNoteInSec = .58;
    for(var i = 0; i < 999; ++i){
      var milisecondTotal = secondTotal * 1000;
      setTimeout(() => {
        this.playAudio.emit();
      }, milisecondTotal);
      secondTotal += quarterNoteInSec;
    };
  }

  private buildSounds(data: TtsInstance[]){
    var results = [];
    data.forEach((data) => {
      const sound = new Speech();
      sound.init({
        'volume': 1,
        'lang': 'en-GB',
        'rate': 1.05,
        'pitch': 1,
        'voice':'Microsoft Zira Desktop - English (United States)',
        'splitSentences': true
      });
      results.push({
        "sound": sound,
        "text": data.text,
        "delay": data.delay
      });
    });
    return results;
  }
}