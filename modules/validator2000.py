class Validateur:
    def choix(question: str, whitelist: list[str]) -> bool:
        reponse = ""
        while reponse not in whitelist:
            reponse = input(question)

        return reponse