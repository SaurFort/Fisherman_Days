from glaciere import Glaciere
from poisson import Poisson
from random import randint

class Peche:
    def __init__(self, glaciere: Glaciere):
        self.glaciere = glaciere

    def __apparition(self) -> Poisson:
        i = randint(1, 5)

        if i == 2:
            return Poisson("Fugu", 0)
        elif i == 3:
            return Poisson("Aiglefin", 0)
        elif i == 4:
            return Poisson("Thon", 0)
        else:
            return Poisson("Maquereau", 0)

    def pecher(self):
        if self.glaciere.verifier_stock():
            poisson = self.__apparition()
            choix = int(input(f"Vous avez attraper un {poisson.categorie}, voulez-vous le garder ?\n1. Oui\n2. Non\n\n"))
            if choix == 1:
                self.glaciere.stocker_poisson(poisson)
                print("Vous avez stocker ce poisson.")
            else:
                print("Vous avez relâcher ce poisson.")

            print("Votre stock:\n", self.glaciere)
