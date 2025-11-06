class Filet:
    def __init__ (self): #défini le niveau de base du filet à 1, donc un boost de chances de 0%
        self.niveau = 1
        
    def taux (self, places_dispo_glaciere, session_or: bool = False):
        if session_or and places_dispo_glaciere == 0:
            return [0,0,0,0,100] #en mer dorée, si la glaciere est pleine, le fugu aura 100% de chances d'apparaitre
        elif session_or:
            return [2,12,55,30,1] # si la glaciere n'est pas pleine, le chances d'obtenir de bons poissons (SANS PRENDRE EN COMPTE LE FILET)

        if places_dispo_glaciere == 0:
            return [35,10,10,10,35] # plus de chances d'obtenir des merlins et des fugus lorsque la glaciere est pleine 
        elif self.niveau == 1:
            return [55,25,12,1,7] # statistiques avec le filet niveau 1 (0%)
        elif self.niveau == 2:
            return [47,28,15,4,6] # statistiques avec le filet niveau 2 (3%)
        elif self.niveau == 3:
            return [35,30,20,10,5] # statistiques avec le filet niveau 3 (10%)
            # dans l'ordre : maquereau, aiglefin, thon, merlin, fugu
        


