import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-window',
  templateUrl: './window.component.html',
  styleUrls: ['./window.component.css']
})
export class WindowComponent implements OnInit{
  title! : string;
  description! : string;
  creationDate!: Date;
  like! : number;

  ngOnInit() {
    this.title = "Article";
    this.description = "Fenêtre d'affichage de l'article";
    this.creationDate = new Date();
    this.like = 6;
  }
}
