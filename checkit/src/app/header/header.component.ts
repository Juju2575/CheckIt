import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { TextBoxComponent } from '../text-box/text-box.component';
import { AppModule, articleList } from '../app.module';
import { Article } from '../app.article';



@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {



  constructor() {
  }

}
