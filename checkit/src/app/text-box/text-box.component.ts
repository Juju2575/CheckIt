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
  isLoaded = false;
  infoPromise(text: string) {
    return new Promise((resolve, reject) => {
      var rep = this.httpClient.get<Article>('http://127.0.0.1:5000/articleInfos', { headers: { text } }).subscribe(x => {
        console.log(x);
        this.value = x;
        this.isLoaded = true;
      });
      console.log(this.value)
      if (rep) {
        resolve('')
        return
      }
      reject('');
    });
  }

  retrievePromise(text: string) {
    let promise = this.infoPromise(text);
    promise.then(
      (n) => {
        console.log('Hello');
        this.displayInfo();
      },
      (t) => console.log('no info registred'))
  };

  displayInfo() {
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
    var ul = document.getElementById("topicsList");
    var li;
    var topics = this.value.topics.substring(1, this.value.topics.length - 1).split(",");
    // console.log(topics);
    // console.log(typeof topics);
    // console.log(typeof this.value.topics);
    if (ul != undefined) {
      while (ul.firstChild) {
        ul.removeChild(ul.firstChild)
      }
      for (let i = 0; i < topics.length; i++) {
        li = document.createElement("li");
        li.appendChild(document.createTextNode(topics[i]));
        ul.appendChild(li);
      }
    }
    ;


  }
}

