# Exercice 03 : Data class - Dataclass Student

import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Genere une chaine aleatoire de 15 caracteres en minuscules."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Dataclass representant un etudiant."""

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Genere le login et l'id apres l'initialisation."""
        self.login = self.name[0].upper() + self.surname
        self.id = generate_id()
