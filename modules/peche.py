from modules.glaciere import Glaciere
from modules.poisson import Poisson
from modules.filet import Filet
from random import randint
from modules.validator2000 import Validateur

class Peche:
    def __init__(self, taux: list[int], glaciere: Glaciere):
        """ Initialise la classe Peche avec les taux d'apparition des poissons et la glacière du joueur."""
        self.taux = taux
        self.glaciere = glaciere

    def __apparition(self) -> Poisson:
        """ Détermine quel poisson apparaît en fonction des taux d'apparition."""
        poissons = ["Maquereau", "Aiglefin", "Thon", "Merlin", "Fugu"]

        x = randint(1, 100)

        proba_cumule = 0

        # Pour chaque poisson, on vérifie si la probabilité cumulée tombe dans la tranche de probabilité du poisson et
        # on crée et retourne l'objet Poisson correspondant.
        for i, p in enumerate(self.taux): # Enumerate retourne l'index et la valeur de chaque élément de la liste taux
            proba_cumule += p
            if x <= proba_cumule:
                return Poisson(poissons[i])

        # Recourt en cas de problème (ne devrait pas arriver)
        return Poisson(poissons[-1])

    def pecher(self):
        """Gère le processus de pêche : apparition du poisson, stockage ou le fait de le relacher."""
        poisson = self.__apparition()
        # On regarde à quelle catégorie appartient le poisson pour afficher un nom décoré
        if poisson.categorie == "Maquereau":
            nom_poisson = "Maquereau |💠|"
        elif poisson.categorie == "Aiglefin":
            nom_poisson = "Aiglefin |💠💠|"
        elif poisson.categorie == "Thon":
            nom_poisson = "Thon |💠💠💠|"
        elif poisson.categorie == "Merlin":
            nom_poisson = "Merlin |✨|"
        else:
            nom_poisson = "Fugu |💀|"

        if poisson.categorie == "Fugu":
            # Puisque le poisson est un Fugu, le joueur perd ses trois derniers poissons et ne peut pas le relâcher.
            input(f"Ho! Vous avez attrapé un {nom_poisson}, vos trois dernières captures ont été perdus,\n impossible de retirer le Fugu de la glacière.\n|⭕| Suivant\n\n _")
            for i in range(3):
                self.glaciere.relacher_poisson()
            self.glaciere.stocker_poisson(poisson)
            print("|✅|Vous avez stocké ce poisson.")
        else:
            # Puisque le poisson n'est pas un Fugu, le joueur peut choisir de le garder ou non.
            choix = Validateur.choix(f"Vous avez attrapé un {nom_poisson}, voulez-vous le garder ?\n1. Oui\n2. Non\n\n _", ["1","2"])
            if choix == "1":
                # Si la glacière est pleine, on relâche le dernier poisson avant de stocker le nouveau.
                if self.glaciere.place_disponible() == 0:
                    self.glaciere.relacher_poisson()
                self.glaciere.stocker_poisson(poisson)
                print("|✅|Vous avez stocké ce poisson.")
            elif choix == "2":
                print("|❌|Vous avez relâché ce poisson.")

        # On affiche le stock de la glacière.
        print("Votre stock:\n", self.glaciere)
