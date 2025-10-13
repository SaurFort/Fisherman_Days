from modules.glaciere import Glaciere

class Marche:
    def __init__(self):
        self.prix_maquereau = 3.0
        self.prix_aiglefin = 12.0
        self.prix_thon = 25.0
        self.prix_merlin = 120.0
        self.prix_fugu = 0.1

    def __inflation(self) -> None:
        self.prix_maquereau = round(self.prix_maquereau * 1.1, 2)
        self.prix_aiglefin = round(self.prix_aiglefin * 1.1, 2)
        self.prix_thon = round(self.prix_thon * 1.1, 2)
        self.prix_merlin = round(self.prix_merlin * 1.1, 2)
        self.prix_fugu = round(self.prix_fugu * 1.1, 2)

    def boutique (self,joueur):
        prix_glaciere = 50*(joueur.glaciere.niveau+1)**2+50*(joueur.glaciere.niveau+1)-100
        if joueur.glaciere.niveau == 4:
            prix_glaciere = 'MAX'
            
            
        prix_filet = 50*(joueur.filet.niveau+1)**3-50*(joueur.filet.niveau+1)
        if joueur.filet.niveau == 3:
            prix_filet = 'MAX'
            

        prix_radar = 650
        if joueur.radar.niveau == 1:
            prix_radar = 'MAX'

        choix=int(input(f"-VOUS ÊTES DANS LA BOUTIQUE-\n1. Glacière [{prix_glaciere}]\n2. Filet [{prix_filet}]\n3. Radar [{prix_radar}]\n4. Retour au marché\n\n"))
        if choix == 1:
            if joueur.glaciere.niveau < 4 and joueur.bourse.recuperer() >= prix_glaciere:
                joueur.bourse.retirer(prix_glaciere)
                joueur.glaciere.niveau += 1
                
        if choix == 2:
            if joueur.filet.niveau < 3 and joueur.bourse.recuperer() >= prix_filet:
                joueur.bourse.retirer(prix_filet)
                joueur.filet.niveau += 1
            
        if choix == 3:
            if joueur.glaciere.niveau < 1 and joueur.bourse.recuperer() >= prix_radar:
                joueur.bourse.retirer(prix_radar)
                joueur.radar.niveau += 1

        joueur.affichage2()

    def vente(self, glaciere: Glaciere) -> int:
        self.__inflation()
        argent = 0
        compte = glaciere.recuperer_stock()

        for poisson in compte:
            if poisson == "Aiglefin":
                argent += compte[poisson] * self.prix_aiglefin
                self.prix_aiglefin = round((self.prix_aiglefin * 0.99) * compte[poisson], 2)
            elif poisson == "Thon":
                argent += compte[poisson] * self.prix_thon
                self.prix_thon = round((self.prix_thon * 0.99) * compte[poisson], 2)
            elif poisson == "Merlin":
                argent += compte[poisson] * self.prix_merlin
                self.prix_merlin = round((self.prix_merlin * 0.99) * compte[poisson], 2)
            elif poisson == "Fugu":
                argent += compte[poisson] * self.prix_fugu
                self.prix_fugu = round((self.prix_fugu * 0.99) * compte[poisson], 2)
            else:
                argent += compte[poisson] * self.prix_maquereau
                self.prix_maquereau = round((self.prix_maquereau * 0.99) * compte[poisson], 2)

        return argent
