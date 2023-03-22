import { Component } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Article } from '../app.article';
import { ArrayType } from '@angular/compiler';
import { WindowComponent } from '../window/window.component';

@Component({
  selector: 'app-text-box',
  templateUrl: './text-box.component.html',
  styleUrls: ['./text-box.component.css']
})
export class TextBoxComponent {
  constructor(private httpClient: HttpClient) { }
  value = new Article;
  windowComp = new WindowComponent;
  infoDisplay(text: string) {
    var rep = this.httpClient.get<Article>('http://127.0.0.1:5000/articleInfos', { headers: { text } }).subscribe(x => {
      console.log(x);
      this.value = x;
      this.windowComp.isLoaded = true;
      this.windowComp.displayInfo(this.value);
    });
  }
}

