from marche import Marche
from glaciere import Glaciere
from peche import Peche

class Joueur :
    def __init__ (self):
        self.bourse = 1
        self.marche = Marche()
        self.glaciere = Glaciere()
        self.fioul = 0
        
    def affichage (self):
        choix = int(input(f"-VOUS ETES EN SESSION DE PECHE- ?\n.pêcher .relâcher\n.bourse actuelle\n.contenu de la glaciere\n.RENTRER\n\n"))
        if choix == 1:
            self.pêcher_en_session()
        if choix == 2:
            self.relâcher()
        if choix == 3:
            self.voir_bourse()
        if choix == 4:
            self.voir_glaciere()
        if choix == 5:
            self.rentrer_prematurer()
        
    def pêcher_en_session(self):
        if self.fioul <= 10:
            Peche(self.glaciere).pecher()
            self.fioul += 1
        else:
            self.rentrer_prematurer()

    def relâcher(self):
        self.glaciere.relacher_poisson()
        self.voir_glaciere()
        
    def voir_bourse(self):
        print(self.bourse)
        
    def voir_glaciere(self):
        print(self.glaciere)
        
    def rentrer_prematurer(self):
        self.bourse += self.marche.vente()
        self.voir_bourse()
        self.fioul = 0

