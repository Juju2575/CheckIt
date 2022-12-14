import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { WindowComponent } from './window/window.component';
import { HeaderComponent } from './header/header.component';
import { SnapFaceTutorialComponent } from './snap-face-tutorial/snap-face-tutorial.component';
import { TextBoxComponent } from './text-box/text-box.component';

@NgModule({
  declarations: [
    AppComponent,
    WindowComponent,
    HeaderComponent,
    SnapFaceTutorialComponent,
    TextBoxComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
