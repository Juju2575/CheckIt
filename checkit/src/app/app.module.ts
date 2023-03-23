import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { Routes, RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { WindowComponent } from './window/window.component';
import { HeaderComponent } from './header/header.component';
import { SnapFaceTutorialComponent } from './snap-face-tutorial/snap-face-tutorial.component';
import { TextBoxComponent } from './text-box/text-box.component';
import { SimilarListComponent } from './similar-list/similar-list.component';
import { HomePageComponent } from './home-page/home-page.component';
import { Article } from './app.article';

export const articleList: Article[] = [new Article()];

export const routes: Routes = [
  { path: '', component: HomePageComponent },
  { path: 'similar-articles', component: SimilarListComponent, data: { articleList: articleList[0] } },
];

@NgModule({
  declarations: [
    AppComponent,
    WindowComponent,
    HeaderComponent,
    SnapFaceTutorialComponent,
    TextBoxComponent,
    SimilarListComponent,
    HomePageComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    RouterModule.forRoot(
      routes
    ),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
