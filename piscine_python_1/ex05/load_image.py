# Exercise 02: Load my image

import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Charge une image et affiche ses informations (format RGB)."""
    try:
        if not isinstance(path, str):
            raise TypeError("Path must be a string")

        img = Image.open(path)

        if img.format not in ['JPEG', 'JPG', 'PNG']:
            raise ValueError(f"Unsupported format: {img.format}")

        img_rgb = img.convert('RGB')
        arr = np.array(img_rgb)

        print(f"The shape of image is: {arr.shape}")
        return arr
    except FileNotFoundError:
        print(f"Error: File not found: {path}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
