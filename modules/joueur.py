from modules.marche import Marche
from modules.glaciere import Glaciere
from modules.filet import Filet
from modules.peche import Peche
from modules.bourse import Bourse
from modules.radar import Radar
from modules.validator2000 import Validateur
from modules.aide import Aide
from random import randint
import sys


class Joueur :
    def __init__ (self):
        self.bourse = Bourse()
        self.marche = Marche()
        self.glaciere = Glaciere()
        self.filet = Filet()
        self.radar = Radar()
        self.fioul = 10 #défini la reverse de fioul au départ, celle ci augmentera avec l'achat d'une meilleur glacière
        self.compteur_de_merlin = 0
        self.session_or = False
        self.aide = Aide()
        self.compteur_de_mers = 0 #compte le nombre de mers dorées trouvées par le joueur
        self.ursaf_active = False
        self.ursaf_compteur = 0

    # -> un selecteur qui affiche tout d'abord les propositions possibles au joueur puis ce dernier 
    # écrit le numéro correspondnt a l'action qu'il veut effectuer dans la console
    # cette partie permet au joueur de faire la plus grosse partie du jeu en pêchant, regardant la glaciere, la bourse... 
    # temps que la variable "fioul" n'est pas égale a 0
    # c'est aussi la que la chance d'obtenir une mer dorée est choisie (environ 5%)
    # si le fioul tombe a 0, le joueur rentre automatiquement au port et tous les poissons sont vendus
    def affichage (self):
        if self.session_or:
            self.compteur_de_mers += 1
            print("✨| SESSION EN MER DOREE |✨\nVous avez une occasion en or de pêcher des poissons rares ! Bonne chance !\n")

        while self.fioul > 0:
            choix = Validateur.choix("-VOUS ÊTES EN SESSION DE PÊCHE- \n 1|🎣| Pêcher\n 2|💦| Relâcher\n 3|💲| Bourse "
                                     "actuelle\n 4|🪣| Contenu de la glaciere\n 5|🛰️| Radar\n 6|❔| Aide \n 7|⛔| RENTRER AU PORT\n\n _", ["1","2","3","4","5","6","7"])
            if choix == "1":
                self.pecher_en_session()
                print(f"Fioul restant: {self.fioul}L\n\n")
                if self.glaciere.sommet().categorie == "Merlin":
                    self.compteur_de_merlin += 1
            if choix == "2":
                self.relacher()
            if choix == "3":
                self.voir_bourse()
            if choix == "4":
                self.voir_glaciere()
            if choix == "5":
                self.voir_radar()
            if choix == "6": 
                self.aide.afficher_aide_joueur(self.marche)
            if choix == "7":
                self.rentrer()

        print("Vous n'avez plus de fioul, vous êtes obligé de rentrer.")
        self.rentrer()

    # -> un selecteur qui affiche tout d'abord les propositions possibles au joueur puis ce dernier 
    # écrit le numéro correspondnt a l'action qu'il veut effectuer dans la console
    # cette partie ci fait une transition entre la pêche et le marché
    def affichage2(self):
        choix = Validateur.choix("-VOUS ÊTES AU PORT-\n 1|💰| Marché\n 2|🎣| Retourner en session\n\n _", ["1","2","3"])

        if choix == "1":
            self.marche.boutique(self)
        
        if choix == "2":
            self.fioul = self.glaciere.total_places() * 2
            self.affichage()

            i = randint(1, 20)
            if i == 1:
                self.session_or = True
            else:
                self.session_or = False

        

    def pecher_en_session(self):
        Peche(self.filet.taux(self.glaciere.place_disponible(), self.session_or),self.glaciere).pecher()
        self.fioul -= 1
        i = randint(1, 200)

        if i == 1: # 0,5% de chance que des pirates attaquent le joueur a chaque fois qu'il pêche
            self.pirate()

    def pirate(self):
        """Gère l'attaque de pirates qui volent la moitié des poissons et une partie de l'argent du joueur."""
        perte = 0
        if self.bourse.recuperer() > 300:
            perte = (self.bourse.recuperer() - 300) * 0.8
        perte += 300

        print(f"🏴‍☠️| Des pirates sont apparus et vous ont volé la moitié de vos poissons et {perte} ! |🏴‍☠️\n")
        for i in range(len(self.glaciere) // 2):
            self.glaciere.relacher_poisson()

        if self.bourse.recuperer() < 0:
            self.ursaf()

    def ursaf(self):
        """Gère la situation où le joueur est endetté et doit rembourser sa dette sous peine de fin de partie."""
        print("Vous êtes endetté et l'URSAF est à vos trousses, vous avez 2 sessions pour rembourser votre dette, "
              "de plus la banque va vous prélevez 40% de vos gains à chaque vente.")
        self.ursaf_active = True

    def relacher(self):
        self.glaciere.relacher_poisson()
        self.voir_glaciere()
        
    def voir_bourse(self):
        print(self.bourse)
        
    def voir_glaciere(self):
        print(self.glaciere)
        
    def rentrer(self): #gère le retour du joueur
        self.bourse.ajouter(self.marche.vente(self.glaciere, self.ursaf_active)) # vend et ajoute l'argent a la bourse
        if self.bourse.recuperer() >= 0:
            self.ursaf_active = False # si le joueur a remboursé sa dette, l'ursaf est désactivée
        elif self.ursaf_active:
            self.ursaf_compteur += 1
            if self.ursaf_compteur >= 2:
                print("L'URSAF est venue vous arrêter pour ne pas avoir remboursé votre dette et découvre aussi que "
                      "vous avez fait du détournement de fond.\nVous avez perdu.")
                sys.exit()
        self.voir_bourse() # affiche la bourse au joueur
        self.affichage2() # bascule directement sur le menu du port
        
    def voir_radar(self):
        print(self.radar.afficher(self.filet.taux(self.glaciere.place_disponible())))


    #gestionnaire de fin de partie, nous affiche dans un premier temps un message de fin global suivit par un afficheur de succès.
    #il y a un total de 6 succès, tous réalisables en une seule partie qui prendra en compte plusieurs éléments.
    
    def fin(self, prix_bibelot):
        compteur_fins = 0
        print("Vous venez d'acheter ce très joli bibelot, en l'achetant vous ressentez une vague de bonheur et d'accomplissement.")
        print("En arrivant chez vous, vous vous apercevez qu'une phrase est écrite sous l'objet.")
        print(f"\"Vous venez de vous faire arnaquez {prix_bibelot}💲, merci de m'avoir payer mon voyage au Bahamas !\"")
        print("A la lecture de ce mot vous ressentez une violente redescente et repenssez au mal que vous avez eu pour l'obtenir.")
        print("Fin.\n")
        print("Merci d'avoir joué")
        print("MoonCore Studio©\n\n")
        
    #-> le nombre d'aides que nous avons lu (pour un total de 12)
        if len(self.aide.vu) == 12:
            print("nouveau prix; |🎋| -Sur le bout des doigts-")
            print("finir le jeu en ayant lu toutes les aides.\n")
            print("Niveau de difficulté: 🟦")
            compteur_fins += 1
        else:
            print("|❌| -Sur le bout des doigts-") #si le joueur n'a pas réussi le succès, seul le nom de celui ci lui est retourné (sans le niveau de difficulté)
                                                    # cela peut lui permettre de trouver ce qu'il doit faire simplement avec le nom du succès
        
    #-> regarde le nombre d'améliorations achetés au marché, il faudra acheter tous les niveaux 
        #d'amélioration de la Glacière, le Filet et le Radar
        if self.glaciere.niveau == 4 and self.filet.niveau == 3 and self.radar.niveau == 1:
            print("nouveau prix; |🔖| -Addict à la consommation-")
            print("finir le jeu en achetant toutes les améliorations.\n")
            print("Niveau de difficulté: 🟩")
            compteur_fins += 1
        else:
            print("|❌| -Addict à la consommation-")
            
    #-> ici on regarde le prix actuel du bibelot, si il n'a pas encore dépassé le palier des 30K dollards, 
        #le succès est débloqué. Ce qui represente environ une vingtaines de sessions de pêche
        if prix_bibelot <= 30000:
            print("nouveau prix; |🏷️| -Rapide comme l'éclair-")
            print("finir le jeu en achetant le bibelot à moins de 30000💲.\n")
            print("Niveau de difficulté: 🟨")
            compteur_fins += 1
        else:
            print("|❌| -Rapide comme l'éclair-")
            
    # -> le joueur doit simplement finir le jeu en ayant au moins 1 million de dollerd dans sa bours LORSQU'il achete le bibelot
        # cela ne prend pas en compte l'achat du bibelot  (bourse_actuelle - prix_bibelot) != bourse finale
        if self.bourse.recuperer() >= 1000000 :
            print("nouveau prix; |📜| -Avide d'argent-")
            print("finir le jeu en étant richissime.\n")
            print("Niveau de difficulté: 🟧")
            compteur_fins += 1
        else:
            print("|❌| -Avide d'argent-")
            
    # -> le joueur doit avoir pêché au moins 100 Merlins.
        if self.compteur_de_merlin >= 100:
            print("nouveau prix; |🎖️| -Le pêcheur devenu Légende-")
            print("finir le jeu en ayant capturés plus de 100 merlins.\n")
            print("Niveau de difficulté: 🟥")
            compteur_fins += 1
        else:
            print("|❌| -Le pêcheur devenu Légende-")
            
    # -> ici la console récupere le nombre de fois ou le joueur a eu une mer dorée
        if self.compteur_de_mers >= 2:
            print("nouveau prix; |🎫| -La ruée vers l'or-")
            print("finir le jeu en ayant découvert 2 mers dorées.\n")
            print("Niveau de difficulté: 🟪")
            compteur_fins += 1
        else:
            print("|❌| -La ruée vers l'or-")
        
        
        print("")
        print(f"fins débloquées: {compteur_fins}/6\n")

        # -> permet de donner le dernier prix si tous les autres ont été rempli
        if compteur_fins == 6:
            print("toutes nos félicitations, vous avez complétez le jeu à 100% ! ")
            print("nouveau prix; |👑| -Roi des mers-")
            print("finir le jeu en ayant débloqué tous les succès.\n")

        # force l'arrêt du programme
        sys.exit()







