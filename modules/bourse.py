class Bourse:
    def __init__(self) -> None:
        """Initialise la bourse avec une somme de départ de 1.0."""
        self.__bourse = 1.0

    def recuperer(self) -> float:
        """
        Retourne la somme actuelle dans la bourse.

        Returns:
            float: La somme actuelle dans la bourse, arrondie à deux décimales.
        """
        return round(self.__bourse, 2)

    def ajouter(self, somme: float) -> None:
        """
        Ajoute une somme à la bourse.

        Args:
            somme (float): La somme à ajouter.
        """
        self.__bourse += round(somme, 2)

    def retirer(self, somme: float) -> None:
        """
        Retire une somme de la bourse.

        Args:
            somme (float): La somme à retirer.
        """
        self.__bourse -= round(somme, 2)

    def __str__(self) -> str:
        """Retourne un texte avec la quantité d'argent présent dans la bourse."""
        return f"Argent: {round(self.__bourse, 0)}💲"
