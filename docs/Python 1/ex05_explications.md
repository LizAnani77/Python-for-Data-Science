# Explications des notions de l'exercice 05

## 1. Les canaux de couleur RGB

Une image couleur est composée de **3 canaux** superposés : Rouge, Vert, Bleu.

```python
array.shape  # (257, 450, 3)
#                       │
#                       └── 3 canaux : R, G, B
```

### Accès aux canaux

```python
array[:, :, 0]  # Canal Rouge (toutes les lignes, toutes les colonnes, index 0)
array[:, :, 1]  # Canal Vert
array[:, :, 2]  # Canal Bleu
```

| Index | Canal | Couleur pure |
|-------|-------|--------------|
| 0 | Rouge (R) | `[255, 0, 0]` |
| 1 | Vert (G) | `[0, 255, 0]` |
| 2 | Bleu (B) | `[0, 0, 255]` |

### Visualisation

```
Image RGB = superposition de 3 couches:

Canal R          Canal G          Canal B          Image finale
┌─────────┐      ┌─────────┐      ┌─────────┐      ┌─────────┐
│ Rouge   │  +   │ Vert    │  +   │ Bleu    │  =   │ Couleur │
│ seul    │      │ seul    │      │ seul    │      │ complète│
└─────────┘      └─────────┘      └─────────┘      └─────────┘
```

---

## 2. Contraintes d'opérateurs par fonction

L'exercice impose des **restrictions sur les opérateurs** utilisables :

| Fonction | Opérateurs autorisés |
|----------|---------------------|
| `ft_invert` | `=`, `+`, `-`, `*` |
| `ft_red` | `=`, `*` |
| `ft_green` | `=`, `-` |
| `ft_blue` | `=` |
| `ft_grey` | `=`, `/` |

Ces contraintes forcent à trouver des solutions créatives pour chaque filtre.

---

## 3. Le filtre Invert (négatif)

**Principe :** Inverser chaque valeur de pixel → `255 - valeur`

```python
def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    result = 255 - array
    return result
```

### Explication mathématique

| Valeur originale | Calcul | Valeur inversée |
|------------------|--------|-----------------|
| 0 (noir) | 255 - 0 | 255 (blanc) |
| 255 (blanc) | 255 - 255 | 0 (noir) |
| 100 | 255 - 100 | 155 |

### Effet sur les couleurs

| Couleur originale | RGB original | RGB inversé | Couleur résultante |
|-------------------|--------------|-------------|-------------------|
| Rouge | `[255, 0, 0]` | `[0, 255, 255]` | Cyan |
| Vert | `[0, 255, 0]` | `[255, 0, 255]` | Magenta |
| Bleu | `[0, 0, 255]` | `[255, 255, 0]` | Jaune |

### Pourquoi ça marche sur tout l'array ?

NumPy applique l'opération **élément par élément** (broadcasting) :

```python
255 - array  # Soustrait 255 de CHAQUE pixel, CHAQUE canal
```

---

## 4. Le filtre Rouge

**Principe :** Garder uniquement le canal rouge, mettre les autres à zéro.

```python
def ft_red(array: np.ndarray) -> np.ndarray:
    """Applies red filter to the image."""
    result = array.copy()
    result[:, :, 1] = result[:, :, 1] * 0  # Vert → 0
    result[:, :, 2] = result[:, :, 2] * 0  # Bleu → 0
    return result
```

### Pourquoi `* 0` au lieu de `= 0` ?

La contrainte autorise uniquement `=` et `*`. On utilise `* 0` pour mettre à zéro.

| Opération | Résultat | Autorisé ? |
|-----------|----------|------------|
| `canal = 0` | Zéro | ✅ (mais utilise `=` différemment) |
| `canal * 0` | Zéro | ✅ |
| `canal - canal` | Zéro | ❌ (pas autorisé ici) |

### Effet visuel

```
Pixel original: [120, 80, 200]  (violet)
                  R    G    B

Après filtre:   [120,  0,   0]  (rouge foncé)
```

---

## 5. Le filtre Vert

**Principe :** Garder uniquement le canal vert.

```python
def ft_green(array: np.ndarray) -> np.ndarray:
    """Applies green filter to the image."""
    result = array.copy()
    result[:, :, 0] = result[:, :, 0] - result[:, :, 0]  # Rouge → 0
    result[:, :, 2] = result[:, :, 2] - result[:, :, 2]  # Bleu → 0
    return result
```

### Astuce : `x - x = 0`

Avec seulement `=` et `-`, on utilise la propriété mathématique :

```python
valeur - valeur = 0
```

| Canal | Opération | Résultat |
|-------|-----------|----------|
| Rouge | `R - R` | 0 |
| Vert | (inchangé) | Valeur originale |
| Bleu | `B - B` | 0 |

---

## 6. Le filtre Bleu

**Principe :** Garder uniquement le canal bleu.

```python
def ft_blue(array: np.ndarray) -> np.ndarray:
    """Applies blue filter to the image."""
    result = np.zeros_like(array)
    result[:, :, 2] = array[:, :, 2]
    return result
```

### La fonction `np.zeros_like()`

Crée un array de **zéros** avec la même shape et le même dtype qu'un autre array.

```python
array.shape        # (257, 450, 3)
array.dtype        # uint8

result = np.zeros_like(array)
result.shape       # (257, 450, 3)
result.dtype       # uint8
# Tous les éléments sont à 0
```

### Pourquoi cette approche ?

Avec uniquement `=`, on ne peut pas faire `* 0` ni `- canal`. Solution :
1. Créer un array tout noir (zéros)
2. Copier seulement le canal bleu

---

## 7. Le filtre Gris (Grayscale)

**Principe :** Calculer la moyenne des 3 canaux et l'appliquer à tous.

```python
def ft_grey(array: np.ndarray) -> np.ndarray:
    """Converts the image to grayscale."""
    result = array.copy()
    grey = result[:, :, 0] / 3 + result[:, :, 1] / 3 + result[:, :, 2] / 3
    grey = grey.astype(np.uint8)
    result[:, :, 0] = grey
    result[:, :, 1] = grey
    result[:, :, 2] = grey
    return result
```

### Pourquoi `/3` trois fois au lieu de `(R+G+B)/3` ?

La contrainte n'autorise que `=` et `/`. On ne peut pas utiliser `+` directement.

**Astuce mathématique :**
```
(R + G + B) / 3  =  R/3 + G/3 + B/3
```

On divise d'abord, puis on additionne (l'addition est implicite dans l'expression).

### Pourquoi les 3 canaux à la même valeur ?

Pour afficher du **gris** en RGB, les trois canaux doivent être égaux :

| R | G | B | Couleur |
|---|---|---|---------|
| 0 | 0 | 0 | Noir |
| 128 | 128 | 128 | Gris moyen |
| 255 | 255 | 255 | Blanc |
| 100 | 100 | 100 | Gris foncé |

---

## 8. La méthode `copy()`

```python
result = array.copy()
```

### Pourquoi copier ?

En Python/NumPy, l'affectation crée une **référence**, pas une copie :

```python
# Sans copy() - PROBLÈME
result = array
result[:, :, 1] = 0  # Modifie AUSSI array !

# Avec copy() - CORRECT
result = array.copy()
result[:, :, 1] = 0  # array reste intact
```

| Opération | `result` modifié | `array` modifié |
|-----------|------------------|-----------------|
| `result = array` | ✅ | ✅ (même objet!) |
| `result = array.copy()` | ✅ | ❌ (indépendant) |

---

## 9. Le slicing avancé `[:, :, n]`

La notation `[:, :, n]` sélectionne **tout** sur les deux premières dimensions et l'index `n` sur la troisième.

```python
array[:, :, 0]  # Toutes lignes, toutes colonnes, canal 0 (Rouge)
```

### Décomposition

| Partie | Signification |
|--------|---------------|
| `:` (1er) | Toutes les lignes |
| `:` (2ème) | Toutes les colonnes |
| `0` (3ème) | Canal index 0 |

### Exemples

```python
array.shape  # (257, 450, 3)

array[:, :, 0].shape  # (257, 450) - Canal Rouge seul
array[:, :, 1].shape  # (257, 450) - Canal Vert seul
array[0, :, :].shape  # (450, 3)   - Première ligne, tous canaux
array[:, 0, :].shape  # (257, 3)   - Première colonne, tous canaux
```

---

## 10. Broadcasting NumPy

Le **broadcasting** permet d'effectuer des opérations entre arrays de dimensions différentes.

```python
255 - array  # 255 (scalaire) - array (3D)
```

### Comment ça fonctionne ?

NumPy "étend" automatiquement le scalaire pour correspondre à la shape de l'array :

```python
# Conceptuellement :
255                    →  [[[255, 255, 255], ...], ...]
array                  =  [[[19, 42, 83], ...], ...]
255 - array            =  [[[236, 213, 172], ...], ...]
```

### Règles du broadcasting

| Opération | Shapes compatibles ? | Résultat |
|-----------|---------------------|----------|
| `(3,) + (3,)` | ✅ | `(3,)` |
| `(257, 450, 3) - 255` | ✅ | `(257, 450, 3)` |
| `(257, 450) + (450,)` | ✅ | `(257, 450)` |
| `(257, 450) + (3,)` | ❌ | Erreur |

---

## 11. Conversion de type avec `astype()`

```python
grey = grey.astype(np.uint8)
```

### Pourquoi c'est nécessaire ?

La division `/` produit des **floats** :

```python
result = array / 3
print(result.dtype)  # float64
```

Mais les images utilisent des **uint8** (0-255). Il faut reconvertir.

| Avant | Après `astype(np.uint8)` |
|-------|--------------------------|
| `85.333...` (float64) | `85` (uint8) |
| `127.666...` (float64) | `127` (uint8) |

### Attention à l'overflow

```python
np.uint8(256)   # 0 (overflow!)
np.uint8(-1)    # 255 (underflow!)
```

---

## 12. Résumé des techniques par filtre

| Filtre | Technique principale | Opérateurs |
|--------|---------------------|------------|
| Invert | `255 - array` | `-` |
| Red | `canal * 0` | `*` |
| Green | `canal - canal` | `-` |
| Blue | `zeros_like` + copie | `=` |
| Grey | `R/3 + G/3 + B/3` | `/` |

---

## 13. Affichage des images avec Matplotlib

Pour afficher les résultats :

```python
import matplotlib.pyplot as plt

plt.imshow(ft_invert(array))
plt.title("Inverted")
plt.show()
```

### Afficher plusieurs images

```python
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

axes[0, 0].imshow(array)
axes[0, 0].set_title("Original")

axes[0, 1].imshow(ft_invert(array))
axes[0, 1].set_title("Invert")

# etc.

plt.tight_layout()
plt.show()
```

---

## 14. Structure attendue des fichiers

```
ex05/
├── load_image.py    ← Copie de l'ex02
├── pimp_image.py    ← Les 5 fonctions de filtre
└── landscape.jpg    ← Image de test
```

Chaque fonction doit :

- Avoir une **docstring** (accessible via `fonction.__doc__`)
- Respecter les **opérateurs autorisés**
- Retourner un array de **même shape** que l'entrée
- Ne pas modifier l'array original (utiliser `copy()`)