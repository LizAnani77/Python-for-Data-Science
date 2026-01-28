# Exercise 04: Rotate me

import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_transpose(array: np.ndarray) -> np.ndarray:
    """Transpose manuellement un tableau 2D (sans utiliser de bibliothèque)."""
    rows = len(array)
    cols = len(array[0])

    # Créer un nouveau tableau avec les dimensions inversées
    transposed = [[array[j][i] for j in range(rows)] for i in range(cols)]
    return np.array(transposed)


def main():
    """Charge une image, coupe un carré, transpose et affiche."""
    try:
        img = ft_load("animal.jpeg")
        if img is None:
            return

        # Définir la zone de zoom (400x400 pixels)
        start_y = 100
        start_x = 450
        size = 400

        # Extraire la zone et convertir en niveaux de gris
        zoomed = img[start_y:start_y + size, start_x:start_x + size]
        grey = np.mean(zoomed, axis=2, keepdims=True).astype(np.uint8)

        print(f"The shape of image is: {grey.shape} or ({grey.shape[0]}, {grey.shape[1]})")
        print(grey)

        # Transpose manuel (on enlève la dimension du canal)
        grey_2d = grey.squeeze()
        transposed = ft_transpose(grey_2d)

        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        # Afficher l'image transposée
        plt.imshow(transposed, cmap='gray')
        plt.title("Transposed Image")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.savefig("rotated_image.png")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
