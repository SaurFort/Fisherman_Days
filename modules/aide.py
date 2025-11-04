from modules.marche import Marche
from modules.validator2000 import Validateur

class Aide:
    def __init__ (self):
        self.vu = {}
        
    def afficher_aide_joueur(self, marche: Marche):
        choix = Validateur.choix("QU'EST CE QUI VOUS TRACASSE ? \n 1|❔|Le but du jeu ? \n 2|❓|La Pêche ? \n 3|❓|Relâcher ? \n 4|❓|La Bourse ?\n 5|❓|La Glacière ? \n 6|❓|Le Radar ? \n 7|❓|Le Port ? \n 8|❔|Si ma Glacière est pleine ? \n 9|❔|Les prix des poissons ? \n10|❔|Le prix du Bibelot ? \n11|❓| Les améliorations ?\n12|❓| Le fioul ? \n13|⛔|RETOUR\n\n _", ["1","2","3","4","5","6","7","8","9","10","11","12","13"])
        if choix == "1" :
            print("🔍 Vous devez pêcher et vendre des poissons, pour acheter un joli bibelot.\n")
            self.vu["1"] = True
            
        elif choix == "2" :
            print("🔍 En pêchant, vous collectez un poisson, plus ou moins rare que vous pourrez revendre en rentrant au port.")
            print("Une rumeur raconte que les poissons les plus rares nageraient en abondance dans une 'mer dorée'...")
            self.vu["2"] = True
            
        elif choix == "3" :
            print("🔍 L'acion de relâcher renvoie directement le dernier poisson collecté à l'eau.\n")
            self.vu["3"] = True
            
        elif choix == "4" :
            print("🔍 La Bourse ? Bah, c'est ton argent quoi, on peut pas être plus explicite...\n")
            self.vu["4"] = True
            
        elif choix == "5" :
            print("🔍 La Glacière, c'est votre zone de stockage de poissons.\n")
            self.vu["5"] = True
            
        elif choix == "6" :
            print("🔍 Le radar est un objet qui vous affiche les chances d'obtenir tel ou tel poisson,")
            print("Mais pour l'utiliser, il est préférable d'en avoir un...\n")
            self.vu["6"] = True
            
        elif choix == "7" :
            print("🔍 Le port est là où le poisson sera vendu. Et vous pourrez aller au marché acheter des nouveaux équipements.\n")
            self.vu["7"] = True
            
        elif choix == "8" :
            print("🔍 Si vous pêcher avec une Glacière pleine et que vous pêchez et gardez un poisson, c'est le dernier poisson enregistré qui laissera sa place au nouveau.\n ")
            self.vu["8"] = True
            
        elif choix == "9" :
            print(f"🔍 Voila le prix actuel des poissons; |💠: {marche.prix_maquereau} |💠💠: {marche.prix_aiglefin} |\n|💠💠💠: {marche.prix_thon} |✨: {marche.prix_merlin} |💀: {marche.prix_fugu} |.\n")
            self.vu["9"] = True
            
        elif choix == "10" : 
            print("🔍 À chaques fois que vous rentrez au port, le prix du Bibelot augmente, ne tardez donc pas à en faire l'acquisition !\n ")
            self.vu["10"] = True
            
        elif choix == "11" :
            print("🔍 Le Filet augmentera les chances de tomber sur de gros poissons, la Glacière vous permet de pêcher plus et plus longtemps en augmentant la réserve de fioul.\n")
            self.vu["11"] = True
            
        elif choix == "12":
            print("🔍 Le fioul représenté en Litres (L), vous annonce le nombre de fois que vous pouvez pêcher avant de rentrer au port. Une fois le réservoir vide, vous serez directement redirigé vers le port.")
            self.vu["12"] = True
            
        elif choix == "13" :  
            return
        choix = Validateur.choix("VOULEZ VOUS RETOURNER AU JEU ? \n1. Oui \n2. Non\n\n _", ["1", "2"])
        if choix == "1" : 
            return
        if choix == "2" : 
            self.afficher_aide_joueur(marche)















