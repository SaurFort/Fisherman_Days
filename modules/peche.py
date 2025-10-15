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
        if poisson.categorie == "Maquereau":
            nom_poisson = "Maquereau |💠|"
        elif poisson.categorie == "Aiglefin":
            nom_poisson = "Aiglefin |💠💠|"
        elif poisson.categorie == "Thon":
            nom_poisson = "Thon |💠💠💠|"
        elif poisson.categorie == "Merlin":
            nom_poisson = "Merlin |✨|"
        elif poisson.categorie == "Fugu":
            nom_poisson = "Fugu |💀|"
        
            choix = 0
            if poisson.categorie == "Fugu":
                choix = input(f"Ho! Vous avez attrapé un {nom_poisson}, vos trois dernières captures ont été perdus,\n impossible de retirer le Fugu de la glacière.\n1|⭕| Suivant")
                if choix == 1 or choix != 1:
                    for i in range(3):
                        self.glaciere.relacher_poisson()
                self.glaciere.stocker_poisson(poisson)
                print("|✅|Vous avez stocké ce poisson.")
                print("Votre stock:\n", self.glaciere)
            
            if poisson.categorie == "Maquereau" or "Aiglefin" or "Thon" or "Merlin": #ou bien (elif p.c != "Fugu")
                choix = input(f"Vous avez attrapé un {nom_poisson}, voulez-vous le garder ?\n1. Oui\n2. Non\n\n -> ")
                if choix == 1:
                    if self.glaciere.place_disponible() == 0:
                        self.glaciere.relacher_poisson()

                self.glaciere.stocker_poisson(poisson)
                print("|✅|Vous avez stocké ce poisson.")
                else:
                    print("|❌|Vous avez relâché ce poisson.")

        print("Votre stock:\n", self.glaciere)
