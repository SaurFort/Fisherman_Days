class Filet:
    def __init__ (self):
        self.niveau = 1
    
    def modif_taux (self):
        if self.niveau == 1:
            return 0.0
        elif self.niveau == 2:
            return 0.03
        else:
            return 0.10

