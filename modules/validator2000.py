class Validateur:
    def choix(question: str, whitelist: list[str]) -> bool:
        """
        Demande une réponse de l'utilisateur jusqu'à ce que ce soit une valeur enregistrée dans la liste blanche.
        Cela permet de s'assurer d'obtenir une réponse valide, qui ne cassera pas le programme.

        Args:
            question (str): La question à poser à l'utilisateur.
            whitelist (list[str]): La liste des réponses acceptée.

        Returns:
            str: La réponse de l'utilisateur parmi les éléments de la liste des réponses acceptables.
        """
        reponse = ""
        while reponse not in whitelist:
            reponse = input(question)

        return reponse