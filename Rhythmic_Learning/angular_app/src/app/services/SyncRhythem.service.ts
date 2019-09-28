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
  //.75 = 1/4 triplet notes; .5 = 1/4 notes; 1 = 1/2 notes;
  var delay = .75;
  var results = [];
  var generator = new RhythemPatternGenerator();
  var delays = generator.generateTestDelays();
  delays.forEach((delay1) => {
    results.push({
      "text": "test",
      "delay": delay1
    });
  });
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

class RhythemPatternGenerator{
  private quarterNote: number;
  private quarterTripletNote: number;
  private halfNote: number;

  //at 120 BPM
  constructor(){
    this.quarterNote = .5;
    this.halfNote = 1;
    this.quarterTripletNote = .75;
  }

  public generateTestDelays(){
    var results = [];
    for(var i = 0; i < 10; ++i){
      results.push(this.quarterNote);
      results.push(this.quarterNote);
      results.push(this.quarterNote);
      results.push(this.quarterNote);
      results.push(this.quarterTripletNote);
      results.push(this.quarterTripletNote);
      results.push(this.halfNote);
    }
    return results;
  }
}