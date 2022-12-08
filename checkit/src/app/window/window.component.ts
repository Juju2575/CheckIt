import { Component, OnInit, Input } from '@angular/core';
import { Fenetre } from '../models/window.model';

@Component({
  selector: 'app-window',
  templateUrl: './window.component.html',
  styleUrls: ['./window.component.css']
})
export class WindowComponent implements OnInit{
  @Input() window! : Fenetre;

  creationDate!: Date;
  like! : number;
  imageUrl!: string;

  ngOnInit() {
    this.creationDate = new Date();
    this.like = 0;
    this.imageUrl = "https://media-exp1.licdn.com/dms/image/C5603AQGsCYZqm5BJwA/profile-displayphoto-shrink_800_800/0/1604946547057?e=2147483647&v=beta&t=7Qg1RvPNXY3lIcV-XDU84IxxC8XGsVvf3jc8fOngnn4"
  }

  onAddLike() {
    this.like++;
  }
}
