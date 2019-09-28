import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class HttpService {
  constructor(private http: HttpClient) { }


  getData(): Observable<Object> {
    return this.http.get('https://api.github.com/users');
  }
      // test query
      // https://angular-http-guide.firebaseio.com/courses.json?orderBy="$key"&limitToFirst=1
      
  postTopic(topic){
    console.log(topic);
  }
}