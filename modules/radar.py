
class Radar:
    def __init__ (self):
        self.niveau = 0 #défini le niveau de base du radar (0)
    
    def afficher (self,proba):
        if self.niveau == 0:
            return "|#####|" # si le joueur n'a pas encore acheté le radar, on lui retourne du bruit blanc 
        if self.niveau >= 1:
            return f"|💠: {proba[0]}% |💠💠: {proba[1]}% |💠💠💠: {proba[2]}% |✨: {proba[3]}% |💀: {proba[4]}%|" 
            # si le joueur a bien acheté le radar (niveau 1), on lui retourne les probabilités en temps réel avec les améliorations du filet
