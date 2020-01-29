import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { TtsInstance } from '../models/TtsInstance'

@Injectable()
export class HttpService {
  constructor(private http: HttpClient) { }


  getData(topic): Observable<Object> {
    return this.http.get('https://api.github.com/users');
  }

  getRapLyrics(topic): Observable<string[]>{
    //return this.http.get<string[]>(`https://rhythmic-learning.herokuapp.com/api/generate/${topic}`)
    return this.http.get<string[]>(`api/generate/${topic}`)
  }
}