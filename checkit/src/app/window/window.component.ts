import { Component } from '@angular/core';
import { Article } from '../app.article';

@Component({
  selector: 'app-window',
  templateUrl: './window.component.html',
  styleUrls: ['./window.component.css']
})
export class WindowComponent {

  constructor() { }
  isLoaded = false;
  displayInfo(value: Article) {
    var displayBox = document.getElementById("title");
    if (displayBox != undefined && value.title != '') {
      displayBox.textContent = 'Title : '.concat(value.title);
    }
    displayBox = document.getElementById("author");
    if (displayBox != undefined && value.author != '') {
      displayBox.textContent = 'Author : '.concat(value.author);
    }
    displayBox = document.getElementById("summary");
    if (displayBox != undefined && value.summary != '') {
      displayBox.textContent = 'Summary : '.concat(value.summary);
    }
    displayBox = document.getElementById("date");
    if (displayBox != undefined && value.creationDate != '') {
      displayBox.textContent = 'Article creation date : '.concat(value.creationDate);
    }
    var ul = document.getElementById("topicsList");
    var li;
    var topics = value.topics.substring(1, value.topics.length - 1).split(",");
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
