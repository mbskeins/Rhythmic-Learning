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
    src: ['static/trap.mp3']
  });
}

public startTts(TtsInstances: TtsInstance[], uiText){
  var parsedData = this.buildSounds(TtsInstances);
  var secondTotal = 0;
  // parsedData.forEach(data => {
    var data = parsedData[0]
    this.playMusic();
    secondTotal += data.delay;
    var miliTotal = secondTotal * 1000;
    setTimeout(() => {
      console.log(data);
      uiText.str = data.text;
      console.log(uiText.str);
      data.sound.speak({
        text: data.text,
        queue: false,
        listeners: {
          onstart: () => {
              //this.playMusic();
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
//  });
}

private playMusic(){
  if(!this.isPlaying) {
    setTimeout(() => {
      this.music.play();
    }, 0);
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