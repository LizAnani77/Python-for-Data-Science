# Exercice 03 : Calculatrice pour operations vecteur-scalaire


class calculator:
    """Classe calculatrice pour operations vecteur-scalaire."""

    def __init__(self, vector: list):
        """Constructeur de la classe calculator."""
        self.vector = vector

    def __add__(self, scalar) -> None:
        """Additionne un scalaire au vecteur."""
        self.vector = [x + scalar for x in self.vector]
        print(self.vector)

    def __mul__(self, scalar) -> None:
        """Multiplie le vecteur par un scalaire."""
        self.vector = [x * scalar for x in self.vector]
        print(self.vector)

    def __sub__(self, scalar) -> None:
        """Soustrait un scalaire du vecteur."""
        self.vector = [x - scalar for x in self.vector]
        print(self.vector)

    def __truediv__(self, scalar) -> None:
        """Divise le vecteur par un scalaire."""
        if scalar == 0:
            print("Error: Division by zero")
            return
        self.vector = [x / scalar for x in self.vector]
        print(self.vector)
