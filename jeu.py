from modules.joueur import Joueur

print("Bienvenue dans )-Fisherman Days-(.\nDans ce petit jeu vous suivrez la vie d'un misérable pêcheur qui essaie tant bien que mal de gagner sa vie afin d'acheter un objet bizarre.")
choix = input("Êtes-vous prêt ? (Oui/oui)\n")

if choix.lower() == "oui" or choix.lower() == "o":
    print("Parfait !")
else:
    print("De toute façon vous n'avez pas le choix !")

joueur = Joueur()
joueur.affichage()
