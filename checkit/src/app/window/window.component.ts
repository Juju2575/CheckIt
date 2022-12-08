import { Component, OnInit, Input } from '@angular/core';
import { Fenetre } from '../models/window.model';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-window',
  templateUrl: './window.component.html',
  styleUrls: ['./window.component.css']
})
export class WindowComponent implements OnInit {
  @Input() window!: Fenetre;

  creationDate!: Date;
  like!: number;
  imageUrl!: string;
  constructor(private httpClient: HttpClient) { }
  ngOnInit() {
    this.creationDate = new Date();
    this.like = 0;
    this.imageUrl = "https://media-exp1.licdn.com/dms/image/C5603AQGsCYZqm5BJwA/profile-displayphoto-shrink_800_800/0/1604946547057?e=2147483647&v=beta&t=7Qg1RvPNXY3lIcV-XDU84IxxC8XGsVvf3jc8fOngnn4"
  };

  onAddLike() {
    this.like++;
  };
  values: number[] = [];
  onRandomLike() {
    var valueList = this.httpClient.get<number[]>('http://127.0.0.1:5000/lukas');
    valueList.subscribe(x => {
      console.log(x);
      this.values = x
    })
    this.like = this.values[Math.floor(Math.random() * this.values.length)];
  }
}
