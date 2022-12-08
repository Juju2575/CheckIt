import { Component, OnInit } from '@angular/core';
import { Snapface } from './models/snapface.model';
import { Fenetre } from './models/window.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'checkit';

  mySnap! : Snapface;
  articleWindow! : Fenetre;
  themeWindow! : Fenetre;

  ngOnInit(){
    this.articleWindow = {
      title : "Article",
      description : "Fenêtre d'aperçu de l'article"
    };
    this.themeWindow = {
      title : "Thematiques",
      description : "Fenêtre d'apeçu des thématiques"
    };
  }
}
