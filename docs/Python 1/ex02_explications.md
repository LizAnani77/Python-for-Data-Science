# Explications des notions de l'exercice 02

## 1. La bibliothèque PIL (Pillow)

**Pillow** est la bibliothèque de référence pour manipuler des images en Python. C'est un fork moderne de PIL (Python Imaging Library).

```python
from PIL import Image
```

### Installation

```bash
pip install Pillow
```

**Note :** On installe `Pillow` mais on importe `PIL` (pour compatibilité historique).

---

## 2. Ouvrir une image avec `Image.open()`

La fonction `Image.open()` charge une image depuis un fichier.

```python
img = Image.open("landscape.jpg")
```

| Attribut | Description | Exemple |
|----------|-------------|---------|
| `img.format` | Format du fichier | `'JPEG'` |
| `img.size` | Dimensions (largeur, hauteur) | `(450, 257)` |
| `img.mode` | Mode colorimétrique | `'RGB'` |

### Formats supportés par Pillow

| Format | Extensions | Description |
|--------|------------|-------------|
| JPEG | `.jpg`, `.jpeg` | Compression avec perte, photos |
| PNG | `.png` | Compression sans perte, transparence |
| GIF | `.gif` | Animations, 256 couleurs max |
| BMP | `.bmp` | Non compressé, volumineux |

---

## 3. Les modes colorimétriques

Une image peut être stockée dans différents **modes** selon le type d'information couleur.

| Mode | Canaux | Description |
|------|--------|-------------|
| `'1'` | 1 | Noir et blanc (1 bit par pixel) |
| `'L'` | 1 | Niveaux de gris (8 bits) |
| `'RGB'` | 3 | Rouge, Vert, Bleu |
| `'RGBA'` | 4 | RGB + canal Alpha (transparence) |
| `'CMYK'` | 4 | Cyan, Magenta, Jaune, Noir (impression) |

### Conversion de mode

```python
img_rgb = img.convert('RGB')
```

| Méthode | Effet |
|---------|-------|
| `img.convert('RGB')` | Convertit en RGB (3 canaux) |
| `img.convert('L')` | Convertit en niveaux de gris |
| `img.convert('RGBA')` | Ajoute un canal de transparence |

**Pourquoi convertir ?** Certaines images JPEG peuvent être en mode `'CMYK'`. La conversion garantit un format uniforme.

---

## 4. Représentation d'une image comme array NumPy

Une image est essentiellement une **grille de pixels**. Chaque pixel a des valeurs de couleur.

```python
arr = np.array(img_rgb)
```

### Structure de l'array

```
arr.shape = (hauteur, largeur, canaux)
            (  257  ,  450  ,   3   )
```

| Dimension | Signification |
|-----------|---------------|
| 1ère (257) | Nombre de lignes (hauteur en pixels) |
| 2ème (450) | Nombre de colonnes (largeur en pixels) |
| 3ème (3) | Nombre de canaux (R, G, B) |

### Visualisation de la structure

```
Image 257×450 RGB:

     ┌─────────────────────────────────────┐
     │  Colonne 0   Colonne 1  ...  Col 449│
     ├─────────────────────────────────────┤
Ligne 0 │ [R,G,B]    [R,G,B]   ...  [R,G,B] │
Ligne 1 │ [R,G,B]    [R,G,B]   ...  [R,G,B] │
  ...   │   ...        ...     ...    ...   │
Ligne 256│ [R,G,B]    [R,G,B]   ...  [R,G,B] │
     └─────────────────────────────────────┘
```

---

## 5. Les valeurs des pixels

Chaque canal de couleur est stocké sur **8 bits**, soit des valeurs de 0 à 255.

```python
pixel = arr[0][0]  # Premier pixel (coin supérieur gauche)
# Exemple: [19, 42, 83]
```

| Canal | Index | Valeur | Signification |
|-------|-------|--------|---------------|
| Rouge (R) | 0 | 19 | Peu de rouge |
| Vert (G) | 1 | 42 | Un peu de vert |
| Bleu (B) | 2 | 83 | Plus de bleu |

### Exemples de couleurs

| Couleur | Valeur RGB |
|---------|------------|
| Noir | `[0, 0, 0]` |
| Blanc | `[255, 255, 255]` |
| Rouge pur | `[255, 0, 0]` |
| Vert pur | `[0, 255, 0]` |
| Bleu pur | `[0, 0, 255]` |

---

## 6. Accéder aux pixels

### Accès à un pixel spécifique

```python
# arr[ligne][colonne] ou arr[y][x]
pixel = arr[100][200]  # Pixel à la ligne 100, colonne 200
```

### Accès à un canal spécifique

```python
arr[100][200][0]  # Valeur Rouge du pixel
arr[100][200][1]  # Valeur Verte du pixel
arr[100][200][2]  # Valeur Bleue du pixel
```

### Accès à une région

```python
arr[0:50, 0:100]     # Rectangle : 50 premières lignes, 100 premières colonnes
arr[:, :, 0]         # Tous les pixels, canal Rouge uniquement
```

---

## 7. Le type de données (`dtype`)

Les arrays d'images utilisent généralement le type `uint8` (unsigned integer 8 bits).

```python
print(arr.dtype)  # uint8
```

| Type | Plage | Utilisation |
|------|-------|-------------|
| `uint8` | 0 à 255 | Standard pour les images |
| `float32` | 0.0 à 1.0 | Calculs, normalisation |
| `float64` | 0.0 à 1.0 | Haute précision |

**Attention :** Les opérations sur `uint8` peuvent provoquer des dépassements (overflow).

```python
np.uint8(250) + np.uint8(10)  # Résultat: 4 (pas 260!)
```

---

## 8. Gestion des erreurs spécifiques

### FileNotFoundError

```python
except FileNotFoundError:
    print(f"Error: File not found: {path}")
```

Cette exception est levée quand le fichier n'existe pas ou le chemin est incorrect.

### Vérification du format

```python
if img.format not in ['JPEG', 'JPG', 'PNG']:
    raise ValueError(f"Unsupported format: {img.format}")
```

| Extension fichier | `img.format` |
|-------------------|--------------|
| `.jpg` | `'JPEG'` |
| `.jpeg` | `'JPEG'` |
| `.png` | `'PNG'` |

**Note :** `.jpg` et `.jpeg` retournent tous deux `'JPEG'` comme format.

---

## 9. Différence entre `size` et `shape`

| Attribut | Source | Format | Exemple |
|----------|--------|--------|---------|
| `img.size` | PIL | (largeur, hauteur) | `(450, 257)` |
| `arr.shape` | NumPy | (hauteur, largeur, canaux) | `(257, 450, 3)` |

**Attention à l'ordre inversé !**

```python
img = Image.open("landscape.jpg")
arr = np.array(img)

print(img.size)   # (450, 257) → largeur × hauteur
print(arr.shape)  # (257, 450, 3) → hauteur × largeur × canaux
```

---

## 10. Affichage de l'array (print)

Quand on affiche un array NumPy volumineux, Python tronque automatiquement l'affichage :

```python
print(arr)
```

```
[[[19 42 83]
  [23 42 84]
  [28 43 84]
  ...
  [ 0  0  0]
  [ 1  1  1]
  [ 1  1  1]]]
```

Les `...` indiquent que des éléments sont masqués pour la lisibilité.

### Contrôler l'affichage

```python
np.set_printoptions(threshold=np.inf)  # Afficher TOUS les éléments
np.set_printoptions(threshold=1000)    # Limiter à 1000 éléments
```

---

## 11. Retourner `None` en cas d'erreur

```python
except Exception as e:
    print(f"Error: {e}")
    return None
```

| Situation | Retour |
|-----------|--------|
| Succès | `np.ndarray` (l'array de l'image) |
| Erreur | `None` |

**Pourquoi `None` ?** Permet à l'appelant de vérifier si le chargement a réussi :

```python
arr = ft_load("image.jpg")
if arr is not None:
    # Traitement de l'image
```

---

## 12. Structure attendue du fichier

```
ex02/
└── load_image.py
```

Le fichier doit contenir :

- Imports explicites (`import numpy as np`, `from PIL import Image`)
- La fonction `ft_load` avec sa docstring
- Gestion des erreurs (fichier non trouvé, format non supporté)
- Support des formats JPG, JPEG (et optionnellement PNG)
- Affichage de la shape avant de retourner l'array