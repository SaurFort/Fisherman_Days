from glaciere import Glaciere
from poisson import Poisson
from filet import Filet
from random import randint

class Peche:
    def __init__(self, filet: Filet, glaciere: Glaciere):
        self.filet = filet
        self.glaciere = glaciere

    def __apparition(self) -> Poisson:
        proba = self.filet.taux(self.glaciere.place_disponible())
        i = randint(1, 100)

        if i < proba[0] + proba[1]:
            return Poisson("Maquereau")
        elif (i >= proba[0] + proba[1]) and (i < proba[0] + proba[1] + proba[2]):
            return Poisson("Aiglefin")
        elif (i >= proba[0] + proba[1] + proba[2]) and (i < proba[0] + proba[1] + proba[2] + proba[3]):
            return Poisson("Thon")
        elif (i >= proba[0] + proba[1] + proba[2] + proba[3]) and (i < proba[0] + proba[1] + proba[2] + proba[3] + proba[4]):
            return Poisson("Merlin")
        else:
            return Poisson("Fugu")

    def pecher(self):
        if self.glaciere.verifier_stock():
            poisson = self.__apparition()
            if poisson.categorie != "Fugu":
                choix = int(
                    input(f"Vous avez attraper un {poisson.categorie}, voulez-vous le garder ?\n1. Oui\n2. Non\n\n"))
                if choix == 1:
                    self.glaciere.stocker_poisson(poisson)
                    print("|⤵️|Vous avez stocker ce poisson.")
                else:
                    print("|↩️|Vous avez relâcher ce poisson.")
            else:
                print("Vous êtes tombé sur un Fugu, vous perdez les trois derniers poissons que vous avez capturé, et vous ne pouvez pas relâcher le Fugu.")
                for _ in range(3):
                    self.glaciere.relacher_poisson()

            print("Votre stock:\n", self.glaciere)
