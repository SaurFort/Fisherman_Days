from modules.marche import Marche
from modules.glaciere import Glaciere
from modules.filet import Filet
from modules.radar import Radar
from modules.peche import Peche
from modules.bourse import Bourse
from modules.radar import Radar

class Joueur :
    def __init__ (self):
        self.bourse = Bourse()
        self.marche = Marche()
        self.glaciere = Glaciere()
        self.filet = Filet()
        self.radar = Radar()
        self.fioul = 10
        
    def affichage (self):
        while self.fioul > 0:
            choix = int(input(f"-VOUS ÊTES EN SESSION DE PÊCHE- ?\n 1|🎣| pêcher\n 2|💦| relâcher\n 3|💰| bourse actuelle\n 4|🪣| contenu de la glaciere\n 6|⛔| RENTRER\n\n"))
            if choix == 1:
                self.pecher_en_session()
                print(f"if vous reste {self.fioul}L |🛢️| dans le reservoir")
            if choix == 2:
                self.relacher()
            if choix == 3:
                self.voir_bourse()
            if choix == 4:
                self.voir_glaciere()
            if choix == 5:
                self.rentrer_prematurer()

        print("Vous n'avez plus de fioul |🛢️|, vous êtes obligés de rentrer.")
        self.rentrer_prematurer()

    def affichage2(self):
        choix = int(input("-VOUS ÊTES AU MARCHE- ?\n1. Boutique\n2. Retourner en session"))

        if choix == 1:
            self.marche.boutique(self)
        else:
            self.fioul = 10
            self.affichage()

    def pecher_en_session(self):
        Peche(self.filet,self.glaciere).pecher()
        self.fioul -= 1

    def relacher(self):
        self.glaciere.relacher_poisson()
        self.voir_glaciere()
        
    def voir_bourse(self):
        print(self.bourse)
        
    def voir_glaciere(self):
        print(self.glaciere)
        
    def rentrer_prematurer(self):
        self.bourse.ajouter(self.marche.vente(self.glaciere))
        self.voir_bourse()
        self.affichage2()
        
    def voir_radar(self):
        print(self.radar)







