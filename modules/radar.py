
class Radar:
    def __init__ (self):
        self.niveau = 1
    
    def modif_taux (self):
        if self.niveau == 1:
            return "#####"
        else:
            return "💠: 55% /💠💠: 25% /💠💠💠: 12% /✨: 1% /💀: 7%"


