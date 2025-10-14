from modules.glaciere import Glaciere
from modules.poisson import Poisson
from modules.filet import Filet
from random import randint

class Peche:
    def __init__(self, filet: Filet, glaciere: Glaciere):
        self.filet = filet
        self.glaciere = glaciere

    def __apparition(self) -> Poisson:
        proba = self.filet.taux(self.glaciere.place_disponible())
        poissons = ["Maquereau", "Aiglefin", "Thon", "Merlin", "Fugu"]

        x = randint(1, 100)

        proba_cumule = 0
        # Enumerate -> retourne index + valeur (foreach PHP)
        for i, p in enumerate(proba):
            proba_cumule += p
            if x <= proba_cumule:
                return Poisson(poissons[i])

        # Fallback
        return Poisson(poissons[-1])

    def pecher(self):
        poisson = self.__apparition()
        if poisson.categorie != "Fugu":
            if poisson.categorie == "Maquereau":
                nom_poisson = "Maquereau |💠|"
            elif poisson.categorie == "Aiglefin":
                nom_poisson = "Aiglefin |💠💠|"
            elif poisson.categorie == "Thon":
                nom_poisson = "Thon |💠💠💠|"
            elif poisson.categorie == "Merlin":
                nom_poisson = "Merlin |✨|"

            choix = int(
                input(f"Vous avez attraper un {nom_poisson}, voulez-vous le garder ?\n1. Oui\n2. Non\n\n"))
            if choix == 1:
                if self.glaciere.place_disponible() == 0:
                    self.glaciere.relacher_poisson()

                self.glaciere.stocker_poisson(poisson)
                print("|✅|Vous avez stocker ce poisson.")
            else:
                print("|❌|Vous avez relâcher ce poisson.")
        else:
            print("Vous êtes tombé sur un Fugu |💀|, vous perdez les trois derniers poissons que vous avez capturé, et vous ne pouvez pas relâcher le Fugu.")
            for _ in range(3):
                self.glaciere.relacher_poisson()
            self.glaciere.stocker_poisson(poisson)

        print("Votre stock:\n", self.glaciere)
