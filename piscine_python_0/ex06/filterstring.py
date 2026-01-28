# Exercise 06: Filter words by length using lambda and list comprehension

import sys
from ft_filter import ft_filter


def main():
    """Filtre les mots d'une chaîne selon leur longueur."""
    args = sys.argv[1:]

    try:
        assert len(args) == 2, "the arguments are bad"
        text = args[0]
        assert isinstance(text, str), "the arguments are bad"
        n = int(args[1])
    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")
        return

    # Utilisation de lambda et list comprehension avec ft_filter
    words = text.split()
    result = list(ft_filter(lambda word: len(word) > n, words))

    print(result)


if __name__ == "__main__":
    main()
