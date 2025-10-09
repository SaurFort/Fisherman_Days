class Bourse:
    def __init__(self):
        self.__bourse = 1

    def ajouter(self, somme: int):
        self.__bourse += somme

    def retirer(self, somme: int):
        self.__bourse -= somme

    def __str__(self):
        return f"Argent: {self.__bourse}"