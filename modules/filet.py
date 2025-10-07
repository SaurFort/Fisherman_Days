class Filet:
    def __init__ (self):
        self.niveau = 1
        
    def taux (self, places_dispo_glaciere):
        if places_dispo_glaciere == 0:
            return [35,10,10,10,35]
        elif self.niveau == 1:
            return [55,25,12,1,7]
        elif self.niveau == 2:
            return [47,28,15,4,6]
        elif self.niveau == 3:
            return [35,30,20,10,5]
        
        

