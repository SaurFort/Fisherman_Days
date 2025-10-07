from poisson import Poisson

class Glaciere:
    def __init__(self):
        self.niveau = 1
        self.__stocke = []

    def __total_places(self) -> int:
        if self.niveau == 1:
            return 5
        elif self.niveau == 2:
            return 12
        elif self.niveau == 3:
            return 20
        else:
            return 30

    def vider(self):
        self.__stocke = []

    def place_disponible(self) -> int:
        return self.__total_places() - len(self.__stocke)

    def verifier_stock(self) -> bool:
        if len(self.__stocke) < self.__total_places():
            return True

        return False

    def relacher_poisson(self) -> None:
        if len(self.__stocke) > 0 and self.__stocke[-1].categorie != "Fugu":
            self.__stocke.pop(-1)

    def stocker_poisson(self, poisson: Poisson) -> None:
        if self.verifier_stock():
            self.__stocke.append(poisson)

    def recuperer_stock(self) -> dict:
        compte = {}
        for poisson in self.__stocke:
            if not poisson.categorie in compte.keys():
                compte[poisson.categorie] = 1
            else:
                compte[poisson.categorie] += 1

        return compte

    def __str__(self) -> str:
        compte = self.recuperer_stock()

        texte = ""
        if len(compte) > 0:
            for categorie in compte:
                texte += f"{categorie}: {str(compte[categorie])}\n"
            texte += f"Il vous restes: {self.place_disponible()} emplacement"
        else:
            texte = "Votre glacière est vide"
        
        return texte

    def __len__(self) -> int:
        return len(self.__stocke)