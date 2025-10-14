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
            choix = int(input(f"-VOUS ÊTES EN SESSION DE PÊCHE- \n 1|🎣| Pêcher\n 2|💦| Relâcher\n 3|💲| Bourse actuelle\n 4|🪣| Contenu de la glaciere\n 5|🛰️| Radar\n 6|⛔| RENTRER\n\n -> "))
            if choix == 1:
                self.pecher_en_session()
                print(f"Fioul restant: {self.fioul}L\n\n")
            if choix == 2:
                self.relacher()
            if choix == 3:
                self.voir_bourse()
            if choix == 4:
                self.voir_glaciere()
            if choix == 5:
                self.voir_radar()
            if choix == 6:
                self.rentrer_prematurer()

        print("Vous n'avez plus de fioul, vous êtes obligés de rentrer.")
        self.rentrer_prematurer()

    def affichage2(self):
        choix = int(input("-VOUS ÊTES AU MARCHE- ?\n1|💰| Boutique\n2|⛔| Retourner en session\n\n"))

        if choix == 1:
            self.marche.boutique(self)
        if choix == 2:
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
        self.radar.afficher(self.filet.taux(self.glaciere.place_disponible()))

    def fin(self, prix_bibelot):
        print("Vous venez d'acheter ce bibelot très joli, en l'achetant vous avez éprouver une énorme joie et êtes partie de la boutique sans demander votre reste.")
        print("En arrivant chez vous, vous vous rendez compte que sous le bibelot il y a écrit une phrase :")
        print(f"\"Vous venez de vous faire arnaquez de {prix_bibelot}, merci de m'avoir payer mon voyage au bahamas !\"")
        print("Après avoir lu tout ça vous ressentez une soudaine tristesse puisque vous avez eu beaucoup de mal pour l'acheter.")
        print("vous avvez désormais un nouvel élément de décors qui vous rappelle toute votre aventure")
        print("Fin.")
















