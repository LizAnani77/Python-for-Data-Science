# Exercise 05: Pimp my image - Apply color filters to images

import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    # Utilisation: =, +, -, *
    result = 255 - array
    return result


def ft_red(array: np.ndarray) -> np.ndarray:
    """Applies red filter to the image (keeps only red channel)."""
    # Utilisation: =, *
    result = array.copy()
    result[:, :, 1] = result[:, :, 1] * 0
    result[:, :, 2] = result[:, :, 2] * 0
    return result


def ft_green(array: np.ndarray) -> np.ndarray:
    """Applies green filter to the image (keeps only green channel)."""
    # Utilisation: =, -
    result = array.copy()
    result[:, :, 0] = result[:, :, 0] - result[:, :, 0]
    result[:, :, 2] = result[:, :, 2] - result[:, :, 2]
    return result


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Applies blue filter to the image (keeps only blue channel)."""
    # Utilisation: =
    result = np.zeros_like(array)
    result[:, :, 2] = array[:, :, 2]
    return result


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Converts the image to grayscale."""
    # Utilisation: =, /
    result = array.copy()
    grey = result[:, :, 0] / 3 + result[:, :, 1] / 3 + result[:, :, 2] / 3
    grey = grey.astype(np.uint8)
    result[:, :, 0] = grey
    result[:, :, 1] = grey
    result[:, :, 2] = grey
    return result
