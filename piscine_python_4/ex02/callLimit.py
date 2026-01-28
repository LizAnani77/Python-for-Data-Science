# Exercice 02 : Mon premier decorateur - Limiteur d'appels

from typing import Any


def callLimit(limit: int):
    """Fabrique de decorateur qui limite le nombre d'appels a une fonction."""
    count = [0]

    def callLimiter(function):
        """Decorateur qui enveloppe la fonction avec une limitation d'appels."""
        def limit_function(*args: Any, **kwds: Any):
            """Wrapper qui verifie le nombre d'appels avant execution."""
            if count[0] < limit:
                count[0] += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
                return None
        return limit_function
    return callLimiter
