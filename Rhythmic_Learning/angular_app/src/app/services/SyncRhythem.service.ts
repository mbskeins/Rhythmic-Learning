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

  private sentences: string[];
  currentSentenceIndex = 0;
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

  public startTtsWithSentences(sentences: string[], voiceURI: string){
    this.sentences = sentences;
    this.currentSentenceIndex = 0;

    this.music.play();
    this.isBeatPlaying = true;
    
    const sound = new Speech();
    sound.init({
      'volume': 1,
      'lang': 'en-GB',
      'rate': 1.05,
      'pitch': 1,
      'voice':voiceURI,
      'splitSentences': true
    });
    this.playNextSentence(sound);
  }

  private playNextSentence(sound: Speech){
    if(this.currentSentenceIndex >= this.sentences.length) return;
    var currentSentence = this.sentences[this.currentSentenceIndex];

    var startTimeInMili = new Date().getTime();
    var quarterNote = 0.35;
    var quarterNoteMili = quarterNote * 1000;
    var measureTimeMili = quarterNoteMili * 4;

      sound.speak({
        text: currentSentence,
        queue: false,
        listeners: {
          onend: () => {
            var endTimeInMili = new Date().getTime();
            var differenceInMili = endTimeInMili - startTimeInMili;
            var numberOfMeasuresThatPassed = differenceInMili / measureTimeMili;
            var percentageOfMeasureToPad = Math.ceil(numberOfMeasuresThatPassed) - numberOfMeasuresThatPassed;
            var delayInMili = percentageOfMeasureToPad * measureTimeMili;
            setTimeout(() => {
              this.playNextSentence(sound);
            }, delayInMili);
          }
        }
      });

      ++this.currentSentenceIndex;
  }

  public startTts(ttsInstance: TtsInstance, voiceURI: string){
    const sound = new Speech();
    sound.init({
      'volume': 1,
      'lang': 'en-GB',
      'rate': 1.05,
      'pitch': 1,
      'voice':voiceURI,
      'splitSentences': true
    });
    var startTimeInMili = new Date().getTime();
    this.music.play();
    this.isBeatPlaying = true;
    setTimeout(() => {
      sound.speak({
        text: ttsInstance.text,
        queue: false,
        listeners: {
          onend: () => {
          }
        }
      });
    }, ttsInstance.delay);
  }
}