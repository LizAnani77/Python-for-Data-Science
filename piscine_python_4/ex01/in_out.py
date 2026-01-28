# Exercice 01 : Outer_inner - Fermetures (Closures)


def square(x: int | float) -> int | float:
    """Retourne le carre de x."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Retourne x eleve a la puissance x."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Retourne une fonction interne qui applique function a x de maniere repetee."""
    count = [x]

    def inner() -> float:
        """Applique function a la valeur courante et la met a jour."""
        count[0] = function(count[0])
        return count[0]

    return inner
