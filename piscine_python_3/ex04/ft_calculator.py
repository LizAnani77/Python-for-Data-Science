# Exercice 04 : Calculatrice pour operations vecteur-vecteur


class calculator:
    """Classe calculatrice pour operations vecteur-vecteur."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calcule et affiche le produit scalaire de deux vecteurs."""
        result = sum(a * b for a, b in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Additionne deux vecteurs et affiche le resultat."""
        result = [float(a + b) for a, b in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Soustrait deux vecteurs et affiche le resultat."""
        result = [float(a - b) for a, b in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
