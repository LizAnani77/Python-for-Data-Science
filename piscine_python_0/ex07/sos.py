# Exercise 07: Dictionaries SoS - Morse code encoder

import sys


NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}


def encode_morse(text: str) -> str:
    """Encode une chaîne en code Morse."""
    result = []
    for char in text.upper():
        if char in NESTED_MORSE:
            result.append(NESTED_MORSE[char])
        else:
            raise ValueError("Invalid character")
    return " ".join(result)


def main():
    """Fonction principale qui encode une chaîne en Morse."""
    args = sys.argv[1:]

    try:
        assert len(args) == 1, "the arguments are bad"
        morse_code = encode_morse(args[0])
        print(morse_code)
    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
