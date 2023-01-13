import { Component } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Article } from '../app.article';
import { ArrayType } from '@angular/compiler';

@Component({
  selector: 'app-text-box',
  templateUrl: './text-box.component.html',
  styleUrls: ['./text-box.component.css']
})
export class TextBoxComponent {
  constructor(private httpClient: HttpClient) { }
  value = new Article;
  captureText(text: string) {
    this.httpClient.post('http://127.0.0.1:5000/sendArticle', text).subscribe();
  }
  retrieveInfo() {
    this.httpClient.get<Article>('http://127.0.0.1:5000/articleInfos').subscribe(x => {
      console.log(x);
      this.value = x;
    });
    var displayBox = document.getElementById("title");
    if (displayBox != undefined) {
      displayBox.textContent = this.value.title;
    }
    displayBox = document.getElementById("author");
    if (displayBox != undefined) {
      displayBox.textContent = this.value.author;
    }
    displayBox = document.getElementById("summary");
    if (displayBox != undefined) {
      displayBox.textContent = this.value.summary;
    }
    displayBox = document.getElementById("date");
    if (displayBox != undefined) {
      displayBox.textContent = this.value.creationDate;
    }
  }
}
