
class Radar:
    def __init__ (self):
        self.niveau = 0
    
    def afficher (self,proba):
        if self.niveau == 0:
            return "|#####|"
        if self.niveau == 1 or self.niveau > 1:
            return f"|💠: {proba[0]}% |💠💠: {proba[1]}% |💠💠💠: {proba[2]}% |✨: {proba[3]}% |💀: {proba[4]}%|"









