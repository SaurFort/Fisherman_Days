class Bourse:
    def __init__(self) -> None:
        self.__bourse = 1.0

    def recuperer(self) -> float:
        return self.__bourse

    def ajouter(self, somme: float) -> None:
        self.__bourse += round(somme, 2)

    def retirer(self, somme: float) -> None:
        self.__bourse -= round(somme, 2)

    def __str__(self) -> str:
        return f"Argent: {self.__bourse}💲"
