# Exercice 02 : DiamondTrap - Classe King avec heritage multiple

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Represente le Roi Joffrey avec heritage en diamant."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructeur de la classe King."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color: str):
        """Definit la couleur des yeux."""
        self.eyes = color

    def set_hairs(self, color: str):
        """Definit la couleur des cheveux."""
        self.hairs = color

    def get_eyes(self):
        """Retourne la couleur des yeux."""
        return self.eyes

    def get_hairs(self):
        """Retourne la couleur des cheveux."""
        return self.hairs
