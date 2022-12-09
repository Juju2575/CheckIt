import { Component, OnInit } from '@angular/core';
import { Snapface } from './models/snapface.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'checkit';

  mySnap! : Snapface;

  getTextBoxVal(item : any){
    console.log(item.value)
  }

  ngOnInit(){
    this.mySnap = {
      title : "Lukas Lapidus",
      description : "Daaaaaamn",
      creationDate : new Date(),
      like: 0,
      imageUrl: "https://media-exp1.licdn.com/dms/image/C5603AQGsCYZqm5BJwA/profile-displayphoto-shrink_800_800/0/1604946547057?e=2147483647&v=beta&t=7Qg1RvPNXY3lIcV-XDU84IxxC8XGsVvf3jc8fOngnn4"
    };
  }
}
