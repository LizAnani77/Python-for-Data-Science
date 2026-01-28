# Explications des notions de l'exercice 00

## 1. Les annotations de type (Type Hints)

Les **annotations de type** documentent les types attendus par une fonction. Elles n'empêchent rien à l'exécution mais améliorent la lisibilité et permettent aux outils d'analyse de détecter des erreurs.

```python
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
```

| Syntaxe | Signification |
|---------|---------------|
| `height: list` | Le paramètre `height` doit être une liste |
| `list[int \| float]` | Liste contenant des entiers **ou** des décimaux |
| `-> list[int \| float]` | La fonction retourne une liste d'int ou float |
| `\|` | Opérateur "ou" pour les types (Python 3.10+) |

---

## 2. Les Docstrings

Une **docstring** est une chaîne de documentation placée immédiatement après la définition d'une fonction.

```python
def give_bmi(...):
    """Calcule le BMI à partir des listes de tailles et poids."""
```

| Accès | Résultat |
|-------|----------|
| `give_bmi.__doc__` | `"Calcule le BMI à partir des listes de tailles et poids."` |
| `help(give_bmi)` | Affiche la documentation complète |

**Obligation de l'exercice :** Toutes les fonctions doivent avoir une docstring.

---

## 3. La gestion d'erreurs (Try/Except)

Le bloc `try/except` permet de **capturer les erreurs** sans faire planter le programme.

```python
try:
    # Code susceptible de lever une exception
    result = weight / height
except Exception as e:
    # Code exécuté si une erreur survient
    print(f"Error: {e}")
    return []
```

| Mot-clé | Rôle |
|---------|------|
| `try` | Délimite le code à surveiller |
| `except` | Capture l'erreur et définit le comportement alternatif |
| `Exception` | Type générique qui capture toutes les erreurs |
| `as e` | Stocke le message d'erreur dans la variable `e` |

### Types d'exceptions courants

| Exception | Déclenchée quand... |
|-----------|---------------------|
| `TypeError` | Mauvais type de données |
| `ValueError` | Valeur incorrecte (ex: nombre négatif) |
| `IndexError` | Index hors limites d'une liste |
| `ZeroDivisionError` | Division par zéro |

---

## 4. La fonction `isinstance()`

Vérifie si une variable est d'un **type spécifique**. Retourne `True` ou `False`.

```python
isinstance(height, list)           # height est-il une liste ?
isinstance(h, (int, float))        # h est-il un int OU un float ?
```

| Appel | Résultat |
|-------|----------|
| `isinstance([1, 2], list)` | `True` |
| `isinstance(3.14, (int, float))` | `True` |
| `isinstance("hello", int)` | `False` |

---

## 5. La fonction `zip()`

Combine **plusieurs itérables** élément par élément, créant des tuples.

```python
height = [1.80, 2.00, 1.75]
weight = [70, 80, 65]

for h, w in zip(height, weight):
    print(h, w)
```

| Itération | `h` | `w` |
|-----------|-----|-----|
| 1ère | 1.80 | 70 |
| 2ème | 2.00 | 80 |
| 3ème | 1.75 | 65 |

**Utilité ici :** Vérifier que chaque élément des deux listes est valide.

---

## 6. NumPy : les tableaux (arrays)

**NumPy** est une bibliothèque de calcul numérique. Son objet principal est le `ndarray` (tableau multidimensionnel).

### Conversion liste → array

```python
import numpy as np

height_arr = np.array([1.80, 2.00, 1.75])
weight_arr = np.array([70, 80, 65])
```

### Vectorisation

L'avantage majeur : les opérations s'appliquent à **tous les éléments simultanément**.

```python
# Sans NumPy (boucle nécessaire)
bmi = []
for i in range(len(height)):
    bmi.append(weight[i] / (height[i] ** 2))

# Avec NumPy (une seule ligne)
bmi_arr = weight_arr / (height_arr ** 2)
```

| Opération | Effet |
|-----------|-------|
| `height_arr ** 2` | Élève tous les éléments au carré |
| `weight_arr / height_arr` | Divise élément par élément |
| `bmi_arr > 25` | Compare chaque élément à 25, retourne des booléens |

---

## 7. La méthode `tolist()`

Convertit un **array NumPy** en **liste Python** standard.

```python
bmi_arr = np.array([21.6, 20.0, 21.2])
bmi_list = bmi_arr.tolist()
```

| Variable | Type | Valeur |
|----------|------|--------|
| `bmi_arr` | `numpy.ndarray` | `array([21.6, 20.0, 21.2])` |
| `bmi_list` | `list` | `[21.6, 20.0, 21.2]` |

**Pourquoi ?** L'exercice demande de retourner une `list`, pas un array NumPy.

---

## 8. La formule du BMI (Body Mass Index)

```
BMI = poids (kg) / taille² (m)
```

| BMI | Catégorie |
|-----|-----------|
| < 18.5 | Insuffisance pondérale |
| 18.5 - 24.9 | Poids normal |
| 25 - 29.9 | Surpoids |
| ≥ 30 | Obésité |

### Exemple de calcul

```python
height = [2.71, 1.15]
weight = [165.3, 38.4]

# Calcul : 165.3 / (2.71)² = 22.51
#          38.4 / (1.15)² = 29.04
```

---

## 9. Comparaison et booléens avec NumPy

```python
bmi_arr = np.array([22.5, 29.0])
result = bmi_arr > 26
```

| Élément | Comparaison | Résultat |
|---------|-------------|----------|
| 22.5 | 22.5 > 26 | `False` |
| 29.0 | 29.0 > 26 | `True` |

**Résultat final :** `[False, True]`

---

## 10. Structure attendue du fichier

```
ex00/
└── give_bmi.py
```

Le fichier doit contenir :

- Les imports explicites (`import numpy as np`)
- Les deux fonctions avec leurs docstrings
- Pas de code dans le scope global
- Pas de variables globales