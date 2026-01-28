# Exercice 01 : GOT S1E7 - Familles Baratheon et Lannister

from S1E9 import Character


class Baratheon(Character):
    """Represente la famille Baratheon."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructeur de la classe Baratheon."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Retourne la representation en chaine de caracteres."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Retourne la representation en chaine de caracteres."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Represente la famille Lannister."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructeur de la classe Lannister."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Retourne la representation en chaine de caracteres."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Retourne la representation en chaine de caracteres."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Methode de classe pour creer un personnage Lannister."""
        return cls(first_name, is_alive)
