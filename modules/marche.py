from modules.glaciere import Glaciere
from modules.validator2000 import Validateur

class Marche:
    def __init__(self):
        """Initialisation des prix initiaux du marché."""
        self.prix_maquereau = 3.0
        self.prix_aiglefin = 12.0
        self.prix_thon = 25.0
        self.prix_merlin = 120.0
        self.prix_fugu = 0.1
        self.prix_bibelot = 10000

    def __inflation(self) -> None:
        """Gère l'augmentation des prix pour les poissons ainsi que du bibelot."""
        self.prix_maquereau = round(self.prix_maquereau * 1.1, 2)
        self.prix_aiglefin = round(self.prix_aiglefin * 1.1, 2)
        self.prix_thon = round(self.prix_thon * 1.1, 2)
        self.prix_merlin = round(self.prix_merlin * 1.1, 2)
        self.prix_fugu = round(self.prix_fugu * 1.1, 2)
        self.prix_bibelot = round(self.prix_bibelot * 1.05, 0)

    def boutique (self,joueur):
        """
        Permet au joueur d'améliorer son équipement ou d'acheter le bibelot final.

        Args:
            joueur: Instance du joueur actuel.
        """
        joueur.voir_bourse()
        prix_glaciere = 50*(joueur.glaciere.niveau+1)**2+50*(joueur.glaciere.niveau+1)-100
        if joueur.glaciere.niveau == 4:
            prix_glaciere = 'MAX'

        prix_filet = 50*(joueur.filet.niveau+1)**3-50*(joueur.filet.niveau+1)
        if joueur.filet.niveau == 3:
            prix_filet = 'MAX'

        prix_radar = 650
        if joueur.radar.niveau == 1:
            prix_radar = 'MAX'
        #affiche au joueur les choix d'amélioration
        choix = Validateur.choix(f"-VOUS ÊTES DANS LE MARCHÉ-\n1|⏫| Glacière + Réservoir [{prix_glaciere}💲]\n2|⏫| Filet [{prix_filet}💲]\n3|🆕| Radar [{prix_radar}💲] !\n4|⭐| Joli bibelot [{self.prix_bibelot}💲]  \n5|⛔|Retour au port \n\n _", ["1","2","3","4","5","fugu&ships"])
        # Condition de debug (chut c'est un secret)
        if choix == "fugu&ships":
            joueur.bourse.ajouter(1000000)
            joueur.voir_bourse()
        
        if choix == "1": #améliore le capacité max de la glaciere, 
                            #comme le reservoir de fioul est basé sur le double de la capacité max de la glaciere, il s'améliore automatiquement
            if joueur.glaciere.niveau < 4 and joueur.bourse.recuperer() >= prix_glaciere:
                joueur.bourse.retirer(prix_glaciere)
                joueur.glaciere.niveau += 1
                print("✅ Votre Glacière et votre Réservoir a été amélioré avec succès ! ✅\n")
                
        if choix == "2": # augmente les probabilités de trouver de bons poissons (+0% / +3% / +10%)
            if joueur.filet.niveau < 3 and joueur.bourse.recuperer() >= prix_filet:
                joueur.bourse.retirer(prix_filet)
                joueur.filet.niveau += 1
                print("✅ Votre Filet a été amélioré avec succès ! ✅\n")
            
        if choix == "3": # permet au joueur de voir les taux d'obtention de poissons en temps réel (une fois aquis)
            if joueur.radar.niveau < 1 and joueur.bourse.recuperer() >= prix_radar:
                joueur.bourse.retirer(prix_radar)
                joueur.radar.niveau += 1
                print("✅ Votre Radar a été acquis avec succès ! ✅\n")

        if choix == "4": # lance la phase finale du jeu qui sera dans "joueur"
            if joueur.bourse.recuperer() >= self.prix_bibelot:
                joueur.fin(self.prix_bibelot)
            else:
                joueur.affichage2()
        else:
            joueur.affichage2()

    def vente(self, glaciere: Glaciere, ursaf: bool = False) -> int:
        """
        Gère la vente des poissons de la glacière du joueur et l'inflation des prix pour la prochaine vente.

        Args:
            glaciere (Glaciere): Instance de la glacière du joueur.
            ursaf (bool): Si l'URSAF est active ou non.

        Returns:
            int: Montant total gagné par le joueur lors de la vente.
        """
        argent = 0 # Montant gagné lors de la vente
        compte = glaciere.recuperer_stock() # Dictionnaire du stock de poissons dans la glacière

        # Boucle de calcul des gains et ajustement des prix.
        # Pour chaque poisson vendu dans chaque catégorie, le prix diminue de 1% par unité vendue.
        # Cette boucle aurait pu être optimisée en utilisant la propriété lambda.
        for poisson in compte:
            if poisson == "Aiglefin":
                argent += compte[poisson] * self.prix_aiglefin
                self.prix_aiglefin = round(self.prix_aiglefin * (0.99 ** compte[poisson]), 2)
            elif poisson == "Thon":
                argent += compte[poisson] * self.prix_thon
                self.prix_thon = round(self.prix_thon * (0.99 ** compte[poisson]), 2)
            elif poisson == "Merlin":
                argent += compte[poisson] * self.prix_merlin
                self.prix_merlin = round(self.prix_merlin * (0.99 ** compte[poisson]), 2)
            elif poisson == "Fugu":
                argent += compte[poisson] * self.prix_fugu
                self.prix_fugu = round(self.prix_fugu * (0.99 ** compte[poisson]), 2)
            else:
                argent += compte[poisson] * self.prix_maquereau
                self.prix_maquereau = round(self.prix_maquereau * (0.99 ** compte[poisson]), 2)

        if ursaf: # Si le joueur est endetté, la banque prélève 40% de ses gains.
            print(f"|⚖️| Vous êtes endetté, la banque vous prélève 40% de vos gains soit {argent * 0.6}💲.\n")
            argent = argent * 0.6

        glaciere.vider() # On vide la glacière.
        self.__inflation() # On applique l'inflation des prix pour la prochaine vente.
        print( # Affiche au joueur les prix des poissons pour la prochaine vente.
            f"🔍 Voila les nouveaux prix du marché |💠: {self.prix_maquereau}💲 |💠💠: {self.prix_aiglefin}💲 |\n|💠💠💠: "
            f"{self.prix_thon}💲 |✨: {self.prix_merlin}💲 |💀: {self.prix_fugu}💲 |, à bientôt .\n")
        return argent
