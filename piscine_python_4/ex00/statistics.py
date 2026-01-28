# Exercice 00 : Calculer mes statistiques

from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Calcule et affiche les statistiques selon les requetes kwargs."""
    def mean(data):
        """Calcule la moyenne des donnees."""
        return sum(data) / len(data)

    def median(data):
        """Calcule la mediane des donnees."""
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]

    def quartile(data):
        """Calcule les 25eme et 75eme percentiles."""
        sorted_data = sorted(data)
        n = len(sorted_data)
        q1_idx = int(n * 0.25)
        q3_idx = int(n * 0.75)
        return [float(sorted_data[q1_idx]), float(sorted_data[q3_idx])]

    def var(data):
        """Calcule la variance des donnees."""
        m = mean(data)
        return sum((x - m) ** 2 for x in data) / len(data)

    def std(data):
        """Calcule l'ecart-type des donnees."""
        return var(data) ** 0.5

    operations = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "var": var,
        "std": std
    }

    for key, value in kwargs.items():
        if len(args) == 0:
            print("ERROR")
        elif value in operations:
            result = operations[value](list(args))
            print(f"{value} : {result}")
