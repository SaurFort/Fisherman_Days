from modules.validator2000 import Validateur

class Aide:
    def afficher_aide_joueur(self):
        choix = Validateur.choix("QU'EST CE QUI VOUS TRACASSE ? \n 1|❔|Le but du jeu ? \n 2|❓|La Pêche ? \n 3|❓|Relâcher ? \n 4|❓|La Bourse ?\n 5|❓|La Glacière ? \n 6|❓|Le Radar ? \n 7|❓|Le Port ? \n8|❔|Si ma Glacière est pleine ? \n9|❔|Les prix des poissons ? \n10|❔|Le prix du Bibelot ? \n11|⛔|RETOUR", ["1","2","3","4","5","6","7","8","9","10","11"]\n\n ->)
        if choix == "1" :
            print("🟡 Vous devez pêcher et vendre des poissons, pour acheter un joli bibelot.")
        elif choix == "2" :
            print("🟡 En pêchant, vous collecter un poisson, plus ou moins rare \nque vous pourrez revendre en rentrant au port.")
        elif choix == "3" :
            print("🟡 L'acion de relâcher renvoie directement le dernier poisson collecté à l'eau.")
        elif choix == "4" :
            print("🟡 La Bourse ? Bah, c'est ton argent quoi, on peut pas être plus explicite")
        elif choix == "5" :
            print("🟡La Glacière, c'est votre zone de stockage de poissons.")
        elif choix == "6" :
            print("🟡 Le radar est un objet qui vous donne les chances d'obtenir tel ou tel poisson,")
            print("Mais pour l'utiliser, il est préférable d'en avoir un...")
        elif choix == "7" :
            print("🟡 Le port est là où le poisson sera vendu. Et vous pourrez aller au marché acheter des nouveaux équipements.")
        elif choix == "8" :
            print("🟡 Si vous pêcher avec une Glacière pleine et que vous pêchez et gardez un poisson,")
            print("c'est le dernier poisson enregistré qui laissera sa place au nouveau. ")
        elif choix == "9" :
            print(f"🟡 Voila le prix actuel des poissons; |💠: {self.marche.prix_maquereau} |💠💠: {self.marche.prix_aiglefin} |\n|💠💠💠: {self.marche.prix_thon} |✨: {self.marche.prix_merlin} |💀: {self.marche.prix_fugu} |.")
        elif choix == "10" : 
            print("🟡 À chaques fois que vous rentrez au port, le prix du Bibelot augmente, ne tardez donc pas à en faire l'acquisition ! ")
        elif choix == "11" :  
            return
        choix = Validateur.choix("VOULEZ VOUS RETOURNER EN PÊCHE ? \n1. Oui \n2. Non", ["1", "2"])
        if choix == "1" : 
            return
        if choix == "2" : 
            self.afficher_aide_joueur()






