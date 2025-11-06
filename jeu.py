from modules.joueur import Joueur

# On oblige le joueur à jouer au jeu :)
print("Bienvenue dans )-Fisherman Days-(.\nDans ce petit jeu vous suivrez la vie d'un misérable pêcheur qui essaie tant bien que mal de gagner sa vie afin d'acheter un objet bizarre.")
choix = input("Êtes-vous prêt ? (Oui/oui)\n")

if choix.lower() == "oui" or choix.lower() == "o":
    print("Parfait !")
else:
    print("De toute façon vous n'avez pas le choix !")

# On initialise le joueur et on appelle aussitôt la méthode affichage qui lance le jeu.
Joueur().affichage()
