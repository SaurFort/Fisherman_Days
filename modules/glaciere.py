from modules.poisson import Poisson

class Glaciere:
    def __init__(self):
        """Initialise une glacière de niveau 1 et avec le stock vide."""
        self.niveau = 1
        self.__stock = []

    def total_places(self) -> int:
        """
        Retourne le nombre total de places disponible dans la glacière selon son niveau.

        Returns:
            int: Le nombre total de places dans la glacière.
        """
        if self.niveau == 1:
            return 5
        elif self.niveau == 2:
            return 12
        elif self.niveau == 3:
            return 20
        else:
            return 30

    def vider(self):
        """Vide complètement la glacière."""
        self.__stock = []

    def sommet(self):
        """
        Retourne le dernier poisson de la glacière sans le retirer.

        Returns:
            Poisson: Le dernier poisson inséré dans la glacière.
        """
        return self.__stock[-1]
    
    def place_disponible(self) -> int:
        """
        Retourne le nombre de places disponibles dans la glacière.

        Returns:
            int: Le nombre de places disponibles.
        """
        return self.total_places() - len(self.__stock)

    def verifier_stock(self) -> bool:
        """
        Vérifie s'il y a de la place dans la glacière pour stocker un poisson.

        Returns:
            bool: True s'il y a de la place, False sinon.
        """
        if len(self.__stock) < self.total_places():
            return True

        return False

    def relacher_poisson(self) -> None:
        """Relâche le dernier poisson de la glacière s'il n'est pas un Fugu."""
        if len(self.__stock) > 0 and self.__stock[-1].categorie != "Fugu":
            self.__stock.pop(-1)

    def stocker_poisson(self, poisson: Poisson) -> None:
        """Stocke un poisson dans la glacière s'il y a de la place."""
        if self.verifier_stock():
            self.__stock.append(poisson)

    def recuperer_stock(self) -> dict:
        """
        Récupère le stock de poissons dans la glacière sous forme d'un dictionnaire

        Returns:
            dict: Un dictionnaire avec les catégories de poissons comme clés et le nombre de poissons
                  de chaque catégorie comme valeurs.
        """
        compte = {}
        for poisson in self.__stock:
            if not poisson.categorie in compte.keys():
                compte[poisson.categorie] = 1
            else:
                compte[poisson.categorie] += 1

        return compte

    def __str__(self) -> str:
        """Retourne une version textuelle du stock de la glacière."""
        compte = self.recuperer_stock()

        texte = ""
        if len(compte) > 0:
            for categorie in compte:
                texte += f"{categorie}: {str(compte[categorie])}\n "
            texte += f"Emplacements restants: {self.place_disponible()}"
        else:
            texte ="Votre glacière est vide |❌|"
        
        return texte

    def __len__(self) -> int:
        """Retourne le nombre de poissons dans la glacière."""
        return len(self.__stock)
