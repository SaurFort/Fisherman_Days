class Poisson:
    def __init__(self, categorie: str):
        """
        Initialise un poisson avec une catégorie donnée.
        La catégorie prend généralement les valeurs : `maquereau`, `aiglefin`, `thon` ou `merlin`.

        Args:
            categorie (str): La catégorie du poisson.
        """
        self.categorie = categorie