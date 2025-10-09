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