# Exercice 00 : GOT S1E9 - Classe abstraite Character et classe Stark

from abc import ABC, abstractmethod


class Character(ABC):
    """Classe abstraite representant un personnage de Game of Thrones."""

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructeur de la classe Character."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Change l'etat de sante du personnage a False."""
        self.is_alive = False


class Stark(Character):
    """Classe representant un membre de la famille Stark."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructeur de la classe Stark."""
        super().__init__(first_name, is_alive)
