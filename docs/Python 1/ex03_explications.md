# Explications des notions de l'exercice 03

## 1. Importer depuis un module local

```python
from load_image import ft_load
```

On réutilise la fonction `ft_load` créée dans l'exercice 02. Le fichier `load_image.py` doit être dans le même dossier.

| Syntaxe | Signification |
|---------|---------------|
| `from load_image` | Depuis le fichier `load_image.py` |
| `import ft_load` | Importer la fonction `ft_load` |

### Structure du dossier

```
ex03/
├── load_image.py    ← Contient ft_load()
└── zoom.py          ← Programme principal
```

---

## 2. Le slicing 2D pour "zoomer"

Le **zoom** consiste à extraire une **région rectangulaire** de l'image. On utilise le slicing sur plusieurs dimensions.

```python
zoomed = img[start_y:start_y + size, start_x:start_x + size]
```

### Syntaxe du slicing multidimensionnel

```python
arr[lignes, colonnes, canaux]
arr[y1:y2, x1:x2, :]
```

| Paramètre | Signification |
|-----------|---------------|
| `start_y:start_y + size` | Lignes de start_y à start_y + 399 |
| `start_x:start_x + size` | Colonnes de start_x à start_x + 399 |

### Visualisation du zoom

```
Image originale (768 × 1024):
┌────────────────────────────────────────┐
│                                        │
│        ┌──────────┐                    │
│        │  ZONE    │ ← Zone extraite    │
│        │  400×400 │   (zoom)           │
│        └──────────┘                    │
│                                        │
└────────────────────────────────────────┘

Après slicing: image 400 × 400
```

### Exemple concret

```python
start_y = 100   # Début ligne 100
start_x = 450   # Début colonne 450
size = 400      # Carré de 400×400

# Extrait les lignes 100-499 et colonnes 450-849
zoomed = img[100:500, 450:850]
```

---

## 3. Conversion RGB → Niveaux de gris

Pour convertir une image couleur en niveaux de gris, on calcule la **moyenne des 3 canaux RGB**.

```python
grey = np.mean(zoomed, axis=2, keepdims=True).astype(np.uint8)
```

### Formule de conversion

```
Gris = (Rouge + Vert + Bleu) / 3
```

| Pixel RGB | Calcul | Valeur grise |
|-----------|--------|--------------|
| `[255, 0, 0]` (rouge) | (255+0+0)/3 | 85 |
| `[0, 255, 0]` (vert) | (0+255+0)/3 | 85 |
| `[100, 100, 100]` | (100+100+100)/3 | 100 |
| `[255, 255, 255]` (blanc) | (255+255+255)/3 | 255 |

---

## 4. Le paramètre `axis` dans NumPy

Le paramètre `axis` indique **sur quelle dimension** effectuer l'opération.

```python
np.mean(zoomed, axis=2)
```

### Visualisation des axes d'un array 3D

```
zoomed.shape = (400, 400, 3)
                 │    │   │
              axis=0  │   │
                   axis=1 │
                       axis=2
```

| Axis | Dimension | Opération `mean` |
|------|-----------|------------------|
| `axis=0` | Lignes (hauteur) | Moyenne verticale |
| `axis=1` | Colonnes (largeur) | Moyenne horizontale |
| `axis=2` | Canaux (R,G,B) | Moyenne des couleurs → **gris** |

### Exemple simplifié

```python
pixel = [120, 130, 140]  # [R, G, B]
#         0    1    2    ← indices (axis=2)

np.mean(pixel)  # (120 + 130 + 140) / 3 = 130
```

---

## 5. Le paramètre `keepdims`

`keepdims=True` conserve la dimension réduite (avec taille 1) au lieu de la supprimer.

```python
# Sans keepdims (défaut: False)
grey = np.mean(zoomed, axis=2)
print(grey.shape)  # (400, 400) ← 2D

# Avec keepdims=True
grey = np.mean(zoomed, axis=2, keepdims=True)
print(grey.shape)  # (400, 400, 1) ← 3D conservé
```

| keepdims | Shape résultante | Description |
|----------|------------------|-------------|
| `False` | `(400, 400)` | Dimension supprimée |
| `True` | `(400, 400, 1)` | Dimension conservée (taille 1) |

**Pourquoi l'utiliser ?** L'exercice demande une shape `(400, 400, 1)` ou `(400, 400)`.

---

## 6. La méthode `astype()`

`astype()` convertit un array vers un autre **type de données**.

```python
grey = np.mean(...).astype(np.uint8)
```

### Problème sans conversion

```python
np.mean([120, 130, 140])  # Résultat: 130.0 (float64)
```

`np.mean()` retourne des **floats**, mais les images utilisent des **uint8** (0-255).

| Avant | Après `astype(np.uint8)` |
|-------|--------------------------|
| `130.0` (float64) | `130` (uint8) |
| `127.6` (float64) | `127` (uint8, tronqué) |

---

## 7. Matplotlib : afficher des images

**Matplotlib** est la bibliothèque standard pour créer des graphiques et afficher des images.

```python
import matplotlib.pyplot as plt
```

### Afficher une image

```python
plt.imshow(image_array)
plt.show()
```

---

## 8. `plt.imshow()` et les colormaps

`imshow()` affiche un array comme une image. Pour les images en niveaux de gris, on spécifie un **colormap**.

```python
plt.imshow(grey, cmap='gray')
```

### Colormaps courants

| Colormap | Effet |
|----------|-------|
| `'gray'` | Niveaux de gris (noir → blanc) |
| `'viridis'` | Dégradé bleu-vert-jaune (défaut) |
| `'hot'` | Noir → rouge → jaune → blanc |
| `'coolwarm'` | Bleu → blanc → rouge |

### Sans colormap sur une image 2D

```python
plt.imshow(grey)  # Applique 'viridis' par défaut → couleurs fausses!
```

**Important :** Toujours utiliser `cmap='gray'` pour les images en niveaux de gris.

---

## 9. La méthode `squeeze()`

`squeeze()` supprime les dimensions de **taille 1** d'un array.

```python
grey.shape           # (400, 400, 1)
grey.squeeze().shape # (400, 400)
```

### Pourquoi l'utiliser ?

`plt.imshow()` peut mal interpréter une image avec shape `(400, 400, 1)`. En "pressant" l'array, on obtient `(400, 400)` qui est clairement 2D.

| Avant squeeze | Après squeeze |
|---------------|---------------|
| `(400, 400, 1)` | `(400, 400)` |
| `(1, 400, 400)` | `(400, 400)` |
| `(400, 400)` | `(400, 400)` (inchangé) |

---

## 10. Configurer l'affichage Matplotlib

```python
plt.title("Zoomed Image")   # Titre du graphique
plt.xlabel("X axis")        # Label axe X
plt.ylabel("Y axis")        # Label axe Y
plt.savefig("output.png")   # Sauvegarder en fichier
plt.show()                  # Afficher la fenêtre
```

### Les axes sur l'image

L'exercice demande d'afficher les **échelles** sur les axes X et Y. Matplotlib le fait automatiquement avec `imshow()`.

```
        0   50  100  150  200  250  300  350
      ┌──────────────────────────────────────┐
    0 │                                      │
   50 │                                      │
  100 │          [IMAGE]                     │
  150 │                                      │
  200 │                                      │
  ...
```

---

## 11. Le pattern `if __name__ == "__main__":`

```python
def main():
    # Code principal

if __name__ == "__main__":
    main()
```

### Explication

| Variable | Valeur quand... |
|----------|-----------------|
| `__name__` = `"__main__"` | Le fichier est exécuté directement |
| `__name__` = `"zoom"` | Le fichier est importé comme module |

### Pourquoi c'est utile ?

```python
# Si on exécute: python zoom.py
# → __name__ == "__main__" → main() s'exécute

# Si on importe: from zoom import quelque_chose
# → __name__ == "zoom" → main() ne s'exécute PAS
```

**Avantage :** Le code peut être à la fois un script exécutable ET un module importable.

---

## 12. Flux d'exécution complet

```
1. Charger l'image (768 × 1024 × 3)
         ↓
2. Afficher shape originale
         ↓
3. Slicer pour zoomer (400 × 400 × 3)
         ↓
4. Convertir en gris (400 × 400 × 1)
         ↓
5. Afficher nouvelle shape
         ↓
6. Afficher l'image avec Matplotlib
```

---

## 13. Structure attendue du fichier

```
ex03/
├── load_image.py    ← Copie de l'ex02
├── zoom.py          ← Programme principal
└── animal.jpeg      ← Image du raton laveur
```

Le fichier `zoom.py` doit :

- Importer `ft_load` depuis `load_image.py`
- Charger et afficher l'image originale
- Extraire une zone carrée (zoom)
- Convertir en niveaux de gris (1 canal)
- Afficher la nouvelle shape : `(400, 400, 1)` ou `(400, 400)`
- Afficher l'image avec les échelles sur les axes