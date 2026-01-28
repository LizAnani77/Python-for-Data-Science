# Explications des notions de l'exercice 04

## 1. Qu'est-ce qu'une transposition ?

La **transposition** d'une matrice consiste à échanger les lignes et les colonnes. L'élément à la position `[i][j]` devient l'élément à la position `[j][i]`.

### Exemple visuel

```
Matrice originale (3×4):        Matrice transposée (4×3):
┌─────────────────────┐         ┌───────────────┐
│  1   2   3   4      │         │  1   5   9    │
│  5   6   7   8      │   →     │  2   6  10    │
│  9  10  11  12      │         │  3   7  11    │
└─────────────────────┘         │  4   8  12    │
                                └───────────────┘
```

| Position originale | Valeur | Position transposée |
|--------------------|--------|---------------------|
| `[0][0]` | 1 | `[0][0]` |
| `[0][1]` | 2 | `[1][0]` |
| `[1][2]` | 7 | `[2][1]` |
| `[2][3]` | 12 | `[3][2]` |

### Formule générale

```
transposed[i][j] = original[j][i]
```

---

## 2. Transposition vs Rotation

**Attention !** Transposer n'est **pas** la même chose que pivoter de 90°.

### Comparaison visuelle

```
Original:           Transposé:          Rotation 90° horaire:
┌───────┐           ┌───────┐           ┌───────┐
│ 1 2 3 │           │ 1 4 7 │           │ 7 4 1 │
│ 4 5 6 │     →     │ 2 5 8 │     vs    │ 8 5 2 │
│ 7 8 9 │           │ 3 6 9 │           │ 9 6 3 │
└───────┘           └───────┘           └───────┘
```

| Opération | Transformation |
|-----------|----------------|
| Transposition | Miroir selon la diagonale principale |
| Rotation 90° | Transposition + inversion horizontale |

### Sur une image

Pour une image carrée en niveaux de gris :
- **Transposition** : l'image est "basculée" selon la diagonale
- L'effet visuel ressemble à une rotation, mais c'est mathématiquement différent

---

## 3. Implémentation manuelle de la transposition

L'exercice **interdit** d'utiliser les fonctions de transposition des bibliothèques (`np.transpose()`, `.T`, etc.). On doit le faire manuellement.

```python
def ft_transpose(array: np.ndarray) -> np.ndarray:
    """Transpose manuellement un tableau 2D."""
    rows = len(array)
    cols = len(array[0])
    
    transposed = [[array[j][i] for j in range(rows)] for i in range(cols)]
    
    return np.array(transposed)
```

### Décomposition étape par étape

```python
rows = len(array)      # Nombre de lignes de l'original
cols = len(array[0])   # Nombre de colonnes de l'original
```

| Array | `rows` | `cols` |
|-------|--------|--------|
| `[[1,2,3], [4,5,6]]` | 2 | 3 |
| 400×400 | 400 | 400 |

---

## 4. Les list comprehensions imbriquées

La transposition utilise une **double list comprehension** :

```python
transposed = [[array[j][i] for j in range(rows)] for i in range(cols)]
```

### Lecture de droite à gauche

```python
# Boucle externe : pour chaque colonne i de l'original
for i in range(cols):
    # Boucle interne : pour chaque ligne j de l'original
    nouvelle_ligne = []
    for j in range(rows):
        nouvelle_ligne.append(array[j][i])
    transposed.append(nouvelle_ligne)
```

### Exemple détaillé

```python
array = [[1, 2, 3],
         [4, 5, 6]]
# rows = 2, cols = 3

# i = 0 : nouvelle ligne = [array[0][0], array[1][0]] = [1, 4]
# i = 1 : nouvelle ligne = [array[0][1], array[1][1]] = [2, 5]
# i = 2 : nouvelle ligne = [array[0][2], array[1][2]] = [3, 6]

transposed = [[1, 4],
              [2, 5],
              [3, 6]]
```

---

## 5. Pourquoi `array[j][i]` et pas `array[i][j]` ?

C'est le cœur de la transposition !

```python
# On veut que transposed[i][j] = array[j][i]
# Donc pour construire transposed[i], on parcourt array[j][i] pour tout j

transposed[i] = [array[j][i] for j in range(rows)]
```

### Visualisation

```
Original array[j][i]:          Transposed[i][j]:
        i=0  i=1  i=2                 j=0  j=1
j=0  │   1    2    3   │      i=0  │   1    4   │
j=1  │   4    5    6   │      i=1  │   2    5   │
                              i=2  │   3    6   │

Pour construire la ligne i=0 du transposé:
  - On prend array[0][0] = 1
  - On prend array[1][0] = 4
  → transposed[0] = [1, 4]
```

---

## 6. La méthode `squeeze()` revisitée

Avant de transposer, on doit passer de 3D à 2D car notre fonction ne gère que les tableaux 2D.

```python
grey.shape       # (400, 400, 1) ← 3D
grey_2d = grey.squeeze()
grey_2d.shape    # (400, 400) ← 2D
```

### Pourquoi c'est nécessaire ?

```python
# Avec shape (400, 400, 1)
len(grey)        # 400 (lignes)
len(grey[0])     # 400 (colonnes)
len(grey[0][0])  # 1 (canal) ← Problème!

# grey[j][i] retourne [valeur] au lieu de valeur
# La transposition ne fonctionnerait pas correctement
```

---

## 7. Différence `len()` vs `.shape`

| Méthode | Ce qu'elle retourne | Sur un array 3D |
|---------|---------------------|-----------------|
| `len(arr)` | Taille de la 1ère dimension | 400 |
| `arr.shape` | Tuple de toutes les dimensions | (400, 400, 1) |

```python
arr = np.zeros((400, 400, 1))

len(arr)        # 400
len(arr[0])     # 400
len(arr[0][0])  # 1

arr.shape       # (400, 400, 1)
arr.shape[0]    # 400
arr.shape[1]    # 400
arr.shape[2]    # 1
```

---

## 8. Conversion liste → array NumPy

À la fin de `ft_transpose`, on reconvertit en array NumPy :

```python
return np.array(transposed)
```

| Étape | Type | Contenu |
|-------|------|---------|
| Avant | `list` de `list` | `[[1,4], [2,5], [3,6]]` |
| Après | `np.ndarray` | `array([[1,4], [2,5], [3,6]])` |

**Pourquoi ?** Matplotlib et NumPy travaillent mieux avec des arrays qu'avec des listes.

---

## 9. Effet de la transposition sur une image carrée

Pour une image carrée (400×400), la transposition :
- Garde les **mêmes dimensions** (400×400)
- Échange les pixels symétriquement par rapport à la **diagonale**

```
Image originale:              Image transposée:
┌─────────────────┐           ┌─────────────────┐
│ ╲               │           │ ╲               │
│   ╲   Zone A    │           │   ╲   Zone B    │
│     ╲           │           │     ╲           │
│       ╲         │           │       ╲         │
│ Zone B  ╲       │    →      │ Zone A  ╲       │
│           ╲     │           │           ╲     │
│             ╲   │           │             ╲   │
└─────────────────┘           └─────────────────┘
       Diagonale                    Diagonale
```

Les zones A et B sont **échangées** par rapport à la diagonale.

---

## 10. Fonctions interdites vs autorisées

### ❌ Interdit pour la transposition

```python
arr.T                    # Attribut de transposition
np.transpose(arr)        # Fonction NumPy
arr.transpose()          # Méthode NumPy
np.swapaxes(arr, 0, 1)   # Échange d'axes
```

### ✅ Autorisé

```python
len()                    # Longueur
range()                  # Itération
list comprehension       # Construction de listes
np.array()              # Conversion finale
```

---

## 11. Flux d'exécution complet

```
1. Charger l'image (768 × 1024 × 3)
         ↓
2. Extraire zone 400×400 (zoom)
         ↓
3. Convertir en gris (400 × 400 × 1)
         ↓
4. Squeeze → (400 × 400)
         ↓
5. Transposer manuellement → (400 × 400)
         ↓
6. Afficher l'image transposée
```

### Évolution des shapes

| Étape | Shape | Description |
|-------|-------|-------------|
| Image chargée | (768, 1024, 3) | RGB couleur |
| Zone zoomée | (400, 400, 3) | Carré RGB |
| Niveaux de gris | (400, 400, 1) | Gris avec canal |
| Après squeeze | (400, 400) | Gris 2D |
| Après transpose | (400, 400) | Transposé (même taille car carré) |

---

## 12. Structure attendue des fichiers

```
ex04/
├── load_image.py    ← Copie de l'ex02
├── rotate.py        ← Programme principal avec ft_transpose
└── animal.jpeg      ← Image du raton laveur
```

Le fichier `rotate.py` doit :

- Contenir une fonction `ft_transpose` **manuelle** (sans bibliothèque)
- Charger l'image et extraire une zone carrée
- Convertir en niveaux de gris
- Transposer et afficher le résultat
- Afficher les shapes avant et après transposition