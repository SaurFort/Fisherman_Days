from modules.marche import Marche
from modules.glaciere import Glaciere
from modules.filet import Filet
from modules.peche import Peche
from modules.bourse import Bourse
from modules.radar import Radar
from modules.validator2000 import Validateur
import sys

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
            choix = Validateur.choix("-VOUS ÊTES EN SESSION DE PÊCHE- \n 1|🎣| Pêcher\n 2|💦| Relâcher\n 3|💲| Bourse "
                                     "actuelle\n 4|🪣| Contenu de la glaciere\n 5|🛰️| Radar\n 6|⛔| RENTRER AU PORT\n\n -> ", ["1","2","3","4","5","6"])
            if choix == "1":
                self.pecher_en_session()
                print(f"Fioul restant: {self.fioul}L\n\n")
            if choix == "2":
                self.relacher()
            if choix == "3":
                self.voir_bourse()
            if choix == "4":
                self.voir_glaciere()
            if choix == "5":
                self.voir_radar()
            if choix == "6":
                self.rentrer_prematurer()

        print("Vous n'avez plus de fioul, vous êtes obligé de rentrer.")
        self.rentrer_prematurer()

    def affichage2(self):
        choix = Validateur.choix("-VOUS ÊTES AU PORT-\n1|💰| Marché\n2|❔| Prix des poissons \n3|🎣| Retourner en session\n\n", ["1","2","3"])

        if choix == "1":
            self.marche.boutique(self)
        if choix == "2":
            print(f"|💠: {self.marche.prix_maquereau} |💠💠: {self.marche.prix_aiglefin} |💠💠💠: {self.marche.prix_thon} |✨: {self.marche.prix_merlin} |💀: {self.marche.prix_fugu} |")
        if choix == "3":
            self.fioul = self.glaciere.total_places() * 2
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
        print(self.radar.afficher(self.filet.taux(self.glaciere.place_disponible())))

    def fin(self, prix_bibelot):
        print("Vous venez d'acheter ce très joli bibelot, en l'achetant vous ressentez une vague de bonheur et d'accomplissement.")
        print("En arrivant chez vous, vous vous apercevez qu'une phrase est écrite sous l'objet.")
        print(f"\"Vous venez de vous faire arnaquez {prix_bibelot}💲, merci de m'avoir payer mon voyage au Bahamas !\"")
        print("A la lecture de ce mot vous ressentez une violente redescente et repenssez au mal que vous avez eu pour l'obtenir.")
        print("Fin.\n")
        print("Merci d'avoir joué")
        print("MoonCore Studio\n\n")
        
        if self.glaciere.niveau == 4 and self.filet.niveau == 3 and self.radar.niveau == 1:
            print("nouveau prix; |🔖| -Addict à la consommation-")
            print("finir le jeu en achetant toutes les améliorations, félicitations !\n")
        if self.glaciere.niveau == 0 and self.filet.niveau == 0 and self.radar.niveau == 0:
            print("nouveau prix; |🏷️| -Ne perd pas le Nord-")
            print("finir le jeu en achetant seulement le bibelot, splendide !\n")
        if self.bourse.recuperer() >= 1000000:
            print("nouveau prix; |📜| -Avide d'argent-")
            print("finir le jeu en étant richissime, magistral !\n")
        if self.compteur_de_merlin >= 100:
            print("nouveau prix; |🎖️| -Le paria devenu légende-")
            print("finir le jeu avec plus de 100 merlins capturés, extraordinaire !\n")
        
        sys.exit()
































