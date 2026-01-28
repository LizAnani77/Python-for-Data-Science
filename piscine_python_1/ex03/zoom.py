# Exercise 03: Zoom on me

import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    """Charge une image, affiche ses infos, zoom et affiche en niveaux de gris."""
    try:
        img = ft_load("animal.jpeg")
        if img is None:
            return

        print(img)

        # Définir la zone de zoom (400x400 pixels au centre)
        start_y = 100
        start_x = 450
        size = 400

        # Extraire la zone de zoom et convertir en niveaux de gris
        zoomed = img[start_y:start_y + size, start_x:start_x + size]

        # Conversion en niveaux de gris (moyenne des canaux RGB)
        grey = np.mean(zoomed, axis=2, keepdims=True).astype(np.uint8)

        print(f"New shape after slicing: {grey.shape} or ({grey.shape[0]}, {grey.shape[1]})")
        print(grey)

        # Afficher l'image avec les échelles
        plt.imshow(grey.squeeze(), cmap='gray')
        plt.title("Zoomed Image")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.savefig("zoomed_image.png")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
