# Exercise 04: The Even and the Odd

import sys


def main():
    # Fonction principale qui vérifie si un nombre est pair ou impair
    args = sys.argv[1:]

    if len(args) == 0:
        return

    try:
        assert len(args) == 1, "more than one argument is provided"
        number = int(args[0])
    except ValueError:
        print("AssertionError: argument is not an integer")
        return
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    main()
