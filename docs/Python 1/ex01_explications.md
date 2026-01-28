# Explications des notions de l'exercice 01

## 1. Les listes 2D (listes imbriquées)

Une **liste 2D** est une liste contenant d'autres listes. On peut la visualiser comme un tableau avec des lignes et des colonnes.

```python
family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]
```

| Représentation | Visualisation |
|----------------|---------------|
| `family[0]` | `[1.80, 78.4]` → 1ère ligne |
| `family[1]` | `[2.15, 102.7]` → 2ème ligne |
| `family[0][0]` | `1.80` → 1ère ligne, 1ère colonne |
| `family[2][1]` | `98.5` → 3ème ligne, 2ème colonne |

### Structure en mémoire

```
family ─┬─► [1.80, 78.4]    (ligne 0)
        ├─► [2.15, 102.7]   (ligne 1)
        ├─► [2.10, 98.5]    (ligne 2)
        └─► [1.88, 75.2]    (ligne 3)
```

---

## 2. La fonction `all()`

La fonction `all()` retourne `True` si **tous les éléments** d'un itérable sont vrais.

```python
all([True, True, True])   # True
all([True, False, True])  # False
all([])                   # True (cas particulier)
```

### Utilisation avec une condition

```python
# Vérifie que chaque élément de family est une liste
all(isinstance(row, list) for row in family)
```

| `family` | Résultat |
|----------|----------|
| `[[1, 2], [3, 4]]` | `True` |
| `[[1, 2], "hello"]` | `False` |
| `[[1, 2], 42]` | `False` |

---

## 3. Les expressions génératrices

Une **expression génératrice** produit des valeurs une par une, sans créer de liste en mémoire.

```python
# Expression génératrice (entre parenthèses)
isinstance(row, list) for row in family

# Équivalent avec une boucle
for row in family:
    yield isinstance(row, list)
```

### Différence avec une liste en compréhension

| Syntaxe | Type | Mémoire |
|---------|------|---------|
| `[x for x in range(1000)]` | Liste | Stocke 1000 éléments |
| `(x for x in range(1000))` | Générateur | Produit à la demande |

**Utilité :** Plus efficace en mémoire quand on n'a besoin que de parcourir les éléments une fois.

---

## 4. L'attribut `shape` de NumPy

L'attribut `shape` retourne un **tuple** décrivant les dimensions d'un array.

```python
import numpy as np

arr = np.array([[1.80, 78.4],
                [2.15, 102.7],
                [2.10, 98.5],
                [1.88, 75.2]])

print(arr.shape)  # (4, 2)
```

| Dimension | Signification | Valeur |
|-----------|---------------|--------|
| 1ère | Nombre de lignes | 4 |
| 2ème | Nombre de colonnes | 2 |

### Exemples de shapes

| Array | Shape | Description |
|-------|-------|-------------|
| `[1, 2, 3]` | `(3,)` | 1D, 3 éléments |
| `[[1, 2], [3, 4]]` | `(2, 2)` | 2D, 2×2 |
| `[[[1], [2]], [[3], [4]]]` | `(2, 2, 1)` | 3D, 2×2×1 |

---

## 5. Le slicing (découpage)

Le **slicing** permet d'extraire une portion d'une séquence avec la syntaxe `[start:end]`.

```python
arr[start:end]
```

| Paramètre | Signification |
|-----------|---------------|
| `start` | Index de début (inclus) |
| `end` | Index de fin (exclu) |

### Exemples sur une liste 1D

```python
lst = ['a', 'b', 'c', 'd', 'e']
#       0    1    2    3    4
#      -5   -4   -3   -2   -1
```

| Slice | Résultat | Explication |
|-------|----------|-------------|
| `lst[0:2]` | `['a', 'b']` | Index 0 et 1 |
| `lst[1:4]` | `['b', 'c', 'd']` | Index 1, 2, 3 |
| `lst[2:]` | `['c', 'd', 'e']` | De l'index 2 à la fin |
| `lst[:3]` | `['a', 'b', 'c']` | Du début à l'index 2 |

### Slicing sur un array 2D

```python
family = [[1.80, 78.4],    # index 0
          [2.15, 102.7],   # index 1
          [2.10, 98.5],    # index 2
          [1.88, 75.2]]    # index 3

arr = np.array(family)
```

| Slice | Résultat | Shape |
|-------|----------|-------|
| `arr[0:2]` | Lignes 0 et 1 | `(2, 2)` |
| `arr[1:3]` | Lignes 1 et 2 | `(2, 2)` |
| `arr[2:]` | Lignes 2 et 3 | `(2, 2)` |

---

## 6. Les indices négatifs

Les indices négatifs comptent **depuis la fin** de la séquence.

```python
family = [[1.80, 78.4],    # index 0  ou -4
          [2.15, 102.7],   # index 1  ou -3
          [2.10, 98.5],    # index 2  ou -2
          [1.88, 75.2]]    # index 3  ou -1
```

| Index positif | Index négatif | Élément |
|---------------|---------------|---------|
| 0 | -4 | `[1.80, 78.4]` |
| 1 | -3 | `[2.15, 102.7]` |
| 2 | -2 | `[2.10, 98.5]` |
| 3 | -1 | `[1.88, 75.2]` |

### Slicing avec indices négatifs

```python
arr[1:-2]  # De l'index 1 jusqu'à -2 (exclu)
```

| Slice | Indices réels | Résultat |
|-------|---------------|----------|
| `arr[1:-2]` | 1 à 2 (exclu) | `[[2.15, 102.7]]` |
| `arr[:-1]` | 0 à 3 (exclu) | 3 premières lignes |
| `arr[-2:]` | -2 à fin | 2 dernières lignes |

---

## 7. Validation d'une liste 2D

Le code effectue plusieurs vérifications pour s'assurer que l'entrée est valide :

### Étape 1 : Vérifier que c'est une liste

```python
if not isinstance(family, list):
    raise TypeError("Family must be a list")
```

### Étape 2 : Vérifier que la liste n'est pas vide

```python
if not family:
    raise ValueError("Family list is empty")
```

**Note :** Une liste vide `[]` est évaluée comme `False` en contexte booléen.

### Étape 3 : Vérifier que chaque élément est une liste

```python
if not all(isinstance(row, list) for row in family):
    raise TypeError("Family must be a 2D list")
```

### Étape 4 : Vérifier que toutes les lignes ont la même taille

```python
row_len = len(family[0])
if not all(len(row) == row_len for row in family):
    raise ValueError("All rows must have the same size")
```

| Entrée | Problème |
|--------|----------|
| `"hello"` | Pas une liste |
| `[]` | Liste vide |
| `[1, 2, 3]` | Pas une liste 2D |
| `[[1, 2], [3]]` | Lignes de tailles différentes |

---

## 8. Flux d'exécution complet

```python
family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

slice_me(family, 0, 2)
```

| Étape | Action | Résultat |
|-------|--------|----------|
| 1 | Conversion en array | `np.array(family)` |
| 2 | Afficher shape original | `My shape is : (4, 2)` |
| 3 | Slicing `arr[0:2]` | 2 premières lignes |
| 4 | Afficher nouvelle shape | `My new shape is : (2, 2)` |
| 5 | Conversion en liste | `[[1.8, 78.4], [2.15, 102.7]]` |

---

## 9. Structure attendue du fichier

```
ex01/
└── array2D.py
```

Le fichier doit contenir :

- Import explicite de NumPy (`import numpy as np`)
- La fonction `slice_me` avec sa docstring
- Gestion des erreurs avec try/except
- Pas de code dans le scope global