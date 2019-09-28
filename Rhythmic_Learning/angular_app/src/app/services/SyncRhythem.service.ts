import { Injectable } from '@angular/core';
import Speech from 'speak-tts'
import {Howl, Howler} from 'howler'
import { TtsInstance } from '../models/TtsInstance'

@Injectable({
  providedIn: 'root'
})
export class SyncRhythemService {

  private isPlaying: boolean;
  private music: Howl;

constructor() { 
  console.log("SyncRhythem attached");
  this.music = new Howl({
    src: ['static/sound.mp3']
  })
}

public startTts(TtsInstances: TtsInstance[]){
  var parsedData = this.buildSounds(TtsInstances);
  var secondTotal = 0;
  parsedData.forEach(data => {
    secondTotal += data.delay;
    var miliTotal = secondTotal * 1000;
    setTimeout(() => {
      data.sound.speak({
        text: data.text,
        queue: false,
        listeners: {
          onstart: () => {
              this.playMusic();
          },
          onend: () => {
            //this.isPlaying = false;
            console.log("End utterance");
          },
          onresume: () => {
            console.log("Resume utterance");
          },
          onpause: () => {
            //this.isPlaying = false;
          }
        }
      });
    }, miliTotal);
 });
}

private playMusic(){
  if(!this.isPlaying) {
    setTimeout(() => {
      this.music.play();
    }, 3.5);
  }
  this.isPlaying = true;
}

  private buildSounds(data: TtsInstance[]){
    var results = [];
    data.forEach((data) => {
      const sound = new Speech();
      sound.init({
        'volume': 1,
        'lang': 'en-GB',
        'rate': 2,
        'pitch': 1,
        'voice':'Google UK English Male',
        'splitSentences': true,
        'listeners': {
          'onvoiceschanged': (voices) => {
            console.log("Event voiceschanged", voices)
          }
        }
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