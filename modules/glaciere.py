from poisson import Poisson

class Glaciere:
    def __init__(self):
        self.niveau = 1
        self.__stocke = []

    def __place_disponible(self) -> int:
        if self.niveau == 1:
            return 5
        elif self.niveau == 2:
            return 12
        elif self.niveau == 3:
            return 20
        else:
            return 30

    def verifier_stock(self) -> bool:
        if len(self.__stocke) < self.__place_disponible():
            return True

        return False

    def relacher_poisson(self) -> None:
        if len(self.__stocke) > 0 and self.__stocke[-1].categorie != "Fugu":
            self.__stocke.pop(-1)

    def stocker_poisson(self, poisson: Poisson) -> None:
        if self.verifier_stock():
            self.__stocke.append(poisson)

    def __str__(self) -> str:
        compte = {}
        for poisson in self.__stocke:
            if not compte[poisson.categorie]:
                compte[poisson.categorie] = 1
            else:
                compte[poisson.categorie] += 1

        texte = ""
        for categorie in compte:
            texte += categorie + ": " + compte[categorie] + "\n"
        
        return texte

    def __len__(self) -> int:
        return len(self.__stocke)