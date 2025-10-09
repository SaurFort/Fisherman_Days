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

    def boutique (self,bourse,glaciere,filet,radar):
        prix_glaciere = 50*(self.glaciere.niveau+1)**2+50*(self.glaciere.niveau+1)-100
        if glaciere.niveau == 4:
            prix_glaciere = 'MAX'
            
            
        prix_filet = 50*(self.filet.niveau+1)**3-50*(self.filet.niveau+1)
        if filet.niveau == 3:
            prix_filet = 'MAX'
            

        prix_radar = 650
        if radar.niveau == 1:
            prix_radar = 'MAX'

        choix=int(input(f"-VOUS ÊTES DANS LA BOUTIQUE-\n1. Glacière [{prix_glaciere}]\n2. Filet [{prix_filet}]\n3. Radar [{prix_radar}]"))
        if choix == 1:
            if glaciere.niveau < 4 and bourse.recuperer >= prix_glaciere:
                bourse.retirer(prix_glaciere)
                glaciere.niveau += 1
                
        if choix == 2:
            if filet.niveau < 3 and bourse.recuperer >= prix_filet:
                bourse.retirer(prix_filet)
                filet.niveau += 1
            
        if choix == 3:
            if glaciere.niveau < 1 and bourse.recupere >= prix_radar:
                bourse.retirer(prix_radar)
                radar.niveau += 1

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
