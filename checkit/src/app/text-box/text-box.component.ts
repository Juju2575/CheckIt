import { Component } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-text-box',
  templateUrl: './text-box.component.html',
  styleUrls: ['./text-box.component.css']
})
export class TextBoxComponent {
  constructor(private httpClient: HttpClient) { }
  value = '';
  captureText(text: string) {
    this.httpClient.post('http://127.0.0.1:5000/sendArticle', text).subscribe();
  }
  retrieveInfo() {
    this.httpClient.get<string>('http://127.0.0.1:5000/articleInfos').subscribe(x => {
      console.log(x);
      this.value = x;
    });
  }
}
