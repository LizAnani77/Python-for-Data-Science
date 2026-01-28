# Exercise 00: Give my BMI - Calculate BMI and apply limit

import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """Calcule le BMI à partir des listes de tailles et poids."""
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError("Arguments must be lists")
        if len(height) != len(weight):
            raise ValueError("Lists must have the same size")
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
                raise TypeError("All elements must be int or float")
            if h <= 0 or w <= 0:
                raise ValueError("Height and weight must be positive")

        height_arr = np.array(height)
        weight_arr = np.array(weight)
        bmi_arr = weight_arr / (height_arr ** 2)
        return bmi_arr.tolist()
    except Exception as e:
        print(f"Error: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Retourne une liste de booléens (True si au-dessus de la limite)."""
    try:
        if not isinstance(bmi, list):
            raise TypeError("BMI must be a list")
        if not isinstance(limit, (int, float)):
            raise TypeError("Limit must be a number")
        for value in bmi:
            if not isinstance(value, (int, float)):
                raise TypeError("All BMI values must be int or float")

        bmi_arr = np.array(bmi)
        result = bmi_arr > limit
        return result.tolist()
    except Exception as e:
        print(f"Error: {e}")
        return []
