import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { TtsInstance } from '../models/TtsInstance'

@Injectable()
export class HttpService {
  constructor(private http: HttpClient) { }


  getData(): Observable<Object> {
    return this.http.get('https://api.github.com/users');
  }

  getTestData(): Observable<TtsInstance[]>{
    return this.http.get<TtsInstance[]>('/api/generate')
  }
      
  postTopic(topic){
    console.log(topic);
  }
}