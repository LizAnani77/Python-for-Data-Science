# Exercise 05: First standalone program python

import sys
import string


def count_characters(text: str) -> dict:
    """Compte les différents types de caractères dans une chaîne."""
    counts = {
        'upper': 0,
        'lower': 0,
        'punctuation': 0,
        'spaces': 0,
        'digits': 0
    }

    for char in text:
        if char.isupper():
            counts['upper'] += 1
        elif char.islower():
            counts['lower'] += 1
        elif char in string.punctuation:
            counts['punctuation'] += 1
        elif char.isspace():
            counts['spaces'] += 1
        elif char.isdigit():
            counts['digits'] += 1

    return counts


def display_counts(text: str) -> None:
    """Affiche le comptage des caractères."""
    counts = count_characters(text)
    total = len(text)

    print(f"The text contains {total} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")


def main():
    # Fonction principale qui analyse une chaîne de caractères
    args = sys.argv[1:]

    try:
        assert len(args) <= 1, "more than one argument is provided"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return

    if len(args) == 0:
        print("What is the text to count?")
        text = sys.stdin.readline()
    else:
        text = args[0]

    display_counts(text)


if __name__ == "__main__":
    main()
