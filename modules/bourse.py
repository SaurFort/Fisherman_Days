class Bourse:
    def __init__(self) -> None:
        self.__bourse = 1

    def recuperer(self) -> int:
        return self.__bourse

    def ajouter(self, somme: int) -> None:
        self.__bourse += somme

    def retirer(self, somme: int) -> None:
        self.__bourse -= somme

    def __str__(self) -> str:
        return f"Argent: {self.__bourse}"