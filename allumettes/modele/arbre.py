from allumettes.modele.marque import Marque


class Arbre(object):

    def __init__(self):
        self.entree = None

    def estVide(self):
        return self.entree == None

    def contient(self, nb_allumettes):
        if self.entree == None:
            return False
        return self.entree.contient(nb_allumettes)

    def prefixe(self, nb_allumettes):
        if self.entree == None:
            return False
        return self.entree.prefixe(nb_allumettes)

    def ajout(self, nb_allumettes):
        if self.entree == None:
            self.entree = Marque(None)
            self.entree = self.entree.ajout(nb_allumettes)
            if not nb_allumettes.isEmpty():
                self.entree = self.entree.suppr("")
            return True
        self.entree = self.entree.ajout(nb_allumettes)

    def suppr(self, nb_allumettes):
        if self.entree == None:
            return False
        self.entree = self.entree.suppr(nb_allumettes)

    def toString(self):
        if self.entree == None:
            return ""
        return self.entree.toString("")
