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
  async plotInfo(text: string) {
    await this.retrieveInfo(text);
    await this.displayInfo();
  }
  async retrieveInfo(text: string) {
    this.httpClient.get<Article>('http://127.0.0.1:5000/articleInfos', { headers: { text } }).subscribe(x => {
      console.log(x);
      this.value = x;
    });
  }
  async displayInfo() {
    console.log('Hello');
    var displayBox = document.getElementById("title");
    if (displayBox != undefined && this.value.title != '') {
      displayBox.textContent = 'Title : '.concat(this.value.title);
    }
    displayBox = document.getElementById("author");
    if (displayBox != undefined && this.value.author != '') {
      displayBox.textContent = 'Author : '.concat(this.value.author);
    }
    displayBox = document.getElementById("summary");
    if (displayBox != undefined && this.value.summary != '') {
      displayBox.textContent = 'Summary : '.concat(this.value.summary);
    }
    displayBox = document.getElementById("date");
    if (displayBox != undefined && this.value.creationDate != '') {
      displayBox.textContent = 'Article creation date : '.concat(this.value.creationDate);
    }
  }
}

