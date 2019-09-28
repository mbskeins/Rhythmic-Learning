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

public startTts(){
 var data = [{"text": "text", "delay": 0.5}, {"text": "text", "delay": 0.5}, {"text": "text", "delay": 0.5}, {"text": "text", "delay": 0.5}, {"text": "text", "delay": 0.5}, {"text": "text", "delay": 0.5}, {"text": "text", "delay": 0.5}, {"text": "text", "delay": 0.5}, {"text": "text", "delay": 0.5}, {"text": "text", "delay": 0.5}, {"text": "text", "delay": 0.5}, {"text": "text", "delay": 0.5}, {"text": "text", "delay": 0.5}, {"text": "text", "delay": 0.5}, {"text": "text", "delay": 0.5}, {"text": "text", "delay": 0.5}, {"text": "text", "delay": 0.5}, {"text": "text", "delay": 0.5}, {"text": "text", "delay": 0.5}];
 const sound = new Speech();
 sound.init({
  'volume': 1,
     'lang': 'en-GB',
     'rate': 1,
     'pitch': 1,
     'voice':'Google UK English Male',
     'splitSentences': true,
     'listeners': {
         'onvoiceschanged': (voices) => {
             console.log("Event voiceschanged", voices)
         }
     }
  });
  var secondTotal = 0;
  data.forEach(data => {
    secondTotal += data.delay;
    var miliTotal = secondTotal * 1000;
    setTimeout(() => {
      sound.speak({
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
      }, 3);
  }
  this.isPlaying = true;
}
}
