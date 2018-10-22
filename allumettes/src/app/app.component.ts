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
      this.nbAllumettesHumain = this.removeAllumettes(n, this.nbAllumettesHumain);
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
      this.rand = Math.floor(Math.random() * 3) + 1;
      console.log(this.rand);
      this.lastJoueur = "IA";

      this.nbAllumettesIA = this.removeAllumettes(this.rand, this.nbAllumettesIA);
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

  removeAllumettes(nbAllumettesRemove: number, nbAllumettesWin : number){
    var w = this.nbAllumettes;

    if((w - nbAllumettesRemove) <= 0){
      this.nbAllumettes = 0;
      nbAllumettesWin = nbAllumettesWin + w;
    }else {
      this.nbAllumettes = this.nbAllumettes - nbAllumettesRemove;
      nbAllumettesWin = nbAllumettesWin + nbAllumettesRemove;
    }

    return nbAllumettesWin;
  }

}
