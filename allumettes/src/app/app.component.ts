import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  Arr = Array;
  nbAllumettes:number = 20;
  nbAllumettesHumain:number = 0;
  nbAllumettesIA:number = 0;
  fini: boolean = false;
  mauvaisJoueurHumain: boolean = false;
  mauvaisJoueurIA: boolean = false;
  gagnant: string = "";
  lastJoueur: string;
  rand: number;

  retirer(n: number) {
    this.mauvaisJoueurIA = false;
    if (this.lastJoueur != 'humain')
    {
      this.nbAllumettes -= n;
      this.nbAllumettesHumain += n;
      if(this.nbAllumettes < 0) {
        this.nbAllumettes = 0;
      }
      this.lastJoueur = "humain";
      this.assertGagnant();
      console.log(this.lastJoueur);
    } else {
      this.mauvaisJoueurHumain = true;
    }
  }

  jouerIA() {
    this.mauvaisJoueurHumain = false;
    if(this.lastJoueur != "IA")
    {
      this.rand = Math.floor(Math.random() * 3);
      this.lastJoueur = "IA";
      this.nbAllumettes -= this.rand == 0 ? 1: this.rand;
      this.nbAllumettesIA += this.rand == 0 ? 1: this.rand;
      this.assertGagnant();
    } else {
      this.mauvaisJoueurIA = true;
    }
  
  }

  assertGagnant() {
    if(this.nbAllumettes == 0){
      this.fini = true;
      switch (this.lastJoueur) {
        case "IA" :
          this.gagnant = "vous avez";
          break;
        case "humain":
          this.gagnant = "l'IA a";
          break;
      }
    }
  }

}
