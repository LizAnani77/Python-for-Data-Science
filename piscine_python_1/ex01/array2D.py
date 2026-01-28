# Exercise 01: 2D array - Slice a 2D array

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Affiche la forme d'un tableau 2D et retourne une version tronquée."""
    try:
        if not isinstance(family, list):
            raise TypeError("Family must be a list")
        if not family:
            raise ValueError("Family list is empty")
        if not all(isinstance(row, list) for row in family):
            raise TypeError("Family must be a 2D list")

        row_len = len(family[0])
        if not all(len(row) == row_len for row in family):
            raise ValueError("All rows must have the same size")

        arr = np.array(family)
        print(f"My shape is : {arr.shape}")

        sliced_arr = arr[start:end]
        print(f"My new shape is : {sliced_arr.shape}")

        return sliced_arr.tolist()
    except Exception as e:
        print(f"Error: {e}")
        return []
