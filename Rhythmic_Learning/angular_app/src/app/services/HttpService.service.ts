import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class HttpService {
  constructor(private http: HttpClient) { }


  getData() {
    this.http.get('https://api.github.com/users')
        .subscribe(data => console.log(data))
  }
      // test query
      // https://angular-http-guide.firebaseio.com/courses.json?orderBy="$key"&limitToFirst=1
      
  postTopic(topic){
    console.log(topic);
  }
}