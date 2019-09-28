import { Injectable } from '@angular/core';
import { debug } from 'util';
import Speech from 'speak-tts'
import {Howl, Howler} from 'howler'

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

private generateTestData(){
  var number = 40;
  var delay = .5;
  var results = [];
  for(var i = 0; i < number; ++i){
    results.push({
      "text": "test",
      "delay": delay
    });
  }
  return results;
}

public startTts(){
  var data = this.generateTestData();
  var parsedData = this.buildSounds(data);
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
          },
          onboundary: event => {
            console.log(
              event.name +
                " boundary reached after " +
                event.elapsedTime +
                " milliseconds."
            );
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
    }, 4);
  }
  this.isPlaying = true;
}

  private buildSounds(data: any[]){
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
