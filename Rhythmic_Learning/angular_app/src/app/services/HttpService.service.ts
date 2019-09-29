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

  getRapLyrics(topic): Observable<TtsInstance>{
    return this.http.get<TtsInstance>(`/api/generate/${topic}`)
  }
}