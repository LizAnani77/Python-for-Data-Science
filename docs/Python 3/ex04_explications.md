# Explications des notions de l'exercice 04 : Calculate my dot product

## 1. Le décorateur `@staticmethod`

Une **méthode statique** est une méthode qui n'a pas besoin d'accéder à l'instance (`self`) ni à la classe (`cls`).

```python
@staticmethod
def dotproduct(V1: list[float], V2: list[float]) -> None:
    result = sum(a * b for a, b in zip(V1, V2))
    print(f"Dot product is: {result}")
```

### Comparaison des trois types de méthodes

| Type | Décorateur | 1er paramètre | Accès |
|------|------------|---------------|-------|
| Instance | aucun | `self` | Instance + classe |
| Classe | `@classmethod` | `cls` | Classe uniquement |
| Statique | `@staticmethod` | aucun | Rien |

### Visualisation

```
Méthode d'instance          Méthode de classe          Méthode statique
──────────────────          ─────────────────          ────────────────

obj.methode()               Classe.methode()           Classe.methode()
     │                            │                          │
     ▼                            ▼                          ▼
┌──────────┐                ┌──────────┐                ┌──────────┐
│   self   │                │   cls    │                │  (rien)  │
└──────────┘                └──────────┘                └──────────┘
```

---

## 2. Appel sans instanciation

Grâce à `@staticmethod`, on peut appeler les méthodes directement sur la classe.

```python
calculator.dotproduct(a, b)  # Pas besoin de créer un objet
```

### Comparaison

```python
# Sans @staticmethod (méthode d'instance)
calc = calculator()      # Doit créer une instance
calc.dotproduct(a, b)    # Appel via l'instance

# Avec @staticmethod
calculator.dotproduct(a, b)  # Appel direct sur la classe
```

### Visualisation

```
Sans @staticmethod:              Avec @staticmethod:

┌─────────────────┐              ┌─────────────────┐
│ 1. Créer objet  │              │ Appel direct    │
│ calc = calc..() │              │ calculator.     │
└────────┬────────┘              │   dotproduct()  │
         │                       └─────────────────┘
         ▼
┌─────────────────┐
│ 2. Appeler      │
│ calc.dotprod..()│
└─────────────────┘
```

### Avantages de `@staticmethod`

| Avantage | Description |
|----------|-------------|
| Pas d'instanciation | Appel direct sur la classe |
| Organisation | Regroupe les fonctions liées |
| Clarté | Indique que la méthode n'utilise pas l'instance |

---

## 3. La fonction `zip()`

`zip()` combine plusieurs itérables élément par élément.

```python
zip(V1, V2)
```

### Fonctionnement

```python
V1 = [5, 10, 2]
V2 = [2, 4, 3]

zip(V1, V2)
```

### Visualisation

```
V1 = [5,  10, 2]
      │   │   │
V2 = [2,  4,  3]
      │   │   │
      ▼   ▼   ▼
    (5,2)(10,4)(2,3)
```

### Résultat

```python
list(zip(V1, V2))
# [(5, 2), (10, 4), (2, 3)]
```

### Utilisation avec une boucle

```python
for a, b in zip(V1, V2):
    print(f"a={a}, b={b}")

# a=5, b=2
# a=10, b=4
# a=2, b=3
```

---

## 4. Le produit scalaire (Dot Product)

Le **produit scalaire** est une opération mathématique entre deux vecteurs.

### Formule

```
V1 · V2 = (a1 × b1) + (a2 × b2) + (a3 × b3) + ...
```

### Exemple

```
V1 = [5, 10, 2]
V2 = [2, 4, 3]

Produit scalaire = (5×2) + (10×4) + (2×3)
                 = 10 + 40 + 6
                 = 56
```

### Visualisation

```
V1 = [5,    10,   2]
      ×      ×    ×
V2 = [2,    4,    3]
      =      =    =
    [10,   40,    6]
      └──────┼────┘
             ▼
            56 (somme)
```

---

## 5. Implémentation du produit scalaire

```python
@staticmethod
def dotproduct(V1: list[float], V2: list[float]) -> None:
    result = sum(a * b for a, b in zip(V1, V2))
    print(f"Dot product is: {result}")
```

### Décomposition

| Étape | Code | Résultat |
|-------|------|----------|
| 1 | `zip(V1, V2)` | `[(5,2), (10,4), (2,3)]` |
| 2 | `a * b for ...` | `10, 40, 6` |
| 3 | `sum(...)` | `56` |

### Expression génératrice

```python
sum(a * b for a, b in zip(V1, V2))
    │                   │
    │                   └── Parcourt les paires
    └── Multiplie et somme
```

### Équivalent détaillé

```python
total = 0
for a, b in zip(V1, V2):
    total += a * b
print(f"Dot product is: {total}")
```

---

## 6. Addition de vecteurs

L'addition de vecteurs additionne les éléments correspondants.

```python
@staticmethod
def add_vec(V1: list[float], V2: list[float]) -> None:
    result = [float(a + b) for a, b in zip(V1, V2)]
    print(f"Add Vector is : {result}")
```

### Formule

```
V1 + V2 = [a1+b1, a2+b2, a3+b3, ...]
```

### Exemple

```
V1 = [5, 10, 2]
V2 = [2, 4, 3]

V1 + V2 = [5+2, 10+4, 2+3]
        = [7, 14, 5]
```

### Visualisation

```
V1 = [5,    10,   2]
      +      +    +
V2 = [2,    4,    3]
      =      =    =
   = [7.0, 14.0, 5.0]
```

---

## 7. Soustraction de vecteurs

La soustraction de vecteurs soustrait les éléments correspondants.

```python
@staticmethod
def sous_vec(V1: list[float], V2: list[float]) -> None:
    result = [float(a - b) for a, b in zip(V1, V2)]
    print(f"Sous Vector is: {result}")
```

### Formule

```
V1 - V2 = [a1-b1, a2-b2, a3-b3, ...]
```

### Exemple

```
V1 = [5, 10, 2]
V2 = [2, 4, 3]

V1 - V2 = [5-2, 10-4, 2-3]
        = [3, 6, -1]
```

### Visualisation

```
V1 = [5,    10,   2]
      -      -    -
V2 = [2,    4,    3]
      =      =    =
   = [3.0, 6.0, -1.0]
```

---

## 8. Conversion en `float()`

Les résultats sont convertis en float pour garantir le format de sortie.

```python
result = [float(a + b) for a, b in zip(V1, V2)]
```

### Pourquoi ?

| Entrée | Sans `float()` | Avec `float()` |
|--------|----------------|----------------|
| `[5, 10, 2]` (int) | `[7, 14, 5]` | `[7.0, 14.0, 5.0]` |

### Garantit la cohérence

```python
# Le testeur utilise des int
a = [5, 10, 2]

# Mais la sortie attendue contient des float
# Add Vector is : [7.0, 14.0, 5.0]
```

---

## 9. La fonction `sum()`

`sum()` calcule la somme des éléments d'un itérable.

```python
sum(a * b for a, b in zip(V1, V2))
```

### Syntaxe

```python
sum(iterable)
sum(iterable, start)  # Avec valeur initiale
```

### Exemples

| Expression | Résultat |
|------------|----------|
| `sum([1, 2, 3])` | `6` |
| `sum([1, 2, 3], 10)` | `16` |
| `sum(x*2 for x in [1,2,3])` | `12` |

---

## 10. Expression génératrice vs List comprehension

### Comparaison

| Type | Syntaxe | Mémoire |
|------|---------|---------|
| List comprehension | `[expr for x in iter]` | Crée une liste |
| Expression génératrice | `(expr for x in iter)` | Génère à la volée |

### Dans le code

```python
# Expression génératrice (produit scalaire)
sum(a * b for a, b in zip(V1, V2))

# List comprehension (addition de vecteurs)
[float(a + b) for a, b in zip(V1, V2)]
```

### Pourquoi cette différence ?

| Opération | Besoin | Utilisation |
|-----------|--------|-------------|
| Produit scalaire | Juste la somme | Expression génératrice |
| Addition vecteurs | Liste résultat | List comprehension |

---

## 11. Les annotations de type avancées

L'exercice utilise `list[float]` comme annotation de type.

```python
def dotproduct(V1: list[float], V2: list[float]) -> None:
```

### Syntaxe

| Annotation | Signification |
|------------|---------------|
| `list` | Une liste quelconque |
| `list[float]` | Une liste de floats |
| `list[int]` | Une liste d'entiers |

### Note sur la compatibilité

```python
# Python 3.9+
def func(x: list[float]) -> None:

# Python 3.7-3.8 (avec import)
from typing import List
def func(x: List[float]) -> None:
```

---

## 12. Structure du fichier ft_calculator.py

```
ft_calculator.py
│
└── Classe calculator
    │
    ├── Docstring
    │
    ├── @staticmethod
    │   dotproduct(V1, V2) → None
    │   └── Produit scalaire
    │
    ├── @staticmethod
    │   add_vec(V1, V2) → None
    │   └── Addition de vecteurs
    │
    └── @staticmethod
        sous_vec(V1, V2) → None
        └── Soustraction de vecteurs
```

---

## 13. Le fichier tester.py

### Code du testeur

```python
from ft_calculator import calculator

a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a, b)
calculator.add_vec(a, b)
calculator.sous_vec(a, b)
```

### Sortie attendue

```
$> python tester.py
Dot product is: 56
Add Vector is : [7.0, 14.0, 5.0]
Sous Vector is: [3.0, 6.0, -1.0]
$>
```

---

## 14. Analyse de la sortie

### Produit scalaire

```
a = [5, 10, 2]
b = [2, 4, 3]

(5×2) + (10×4) + (2×3)
  10  +   40   +   6
         = 56
```

### Addition de vecteurs

```
a = [5,    10,   2]
     +      +    +
b = [2,    4,    3]
     =      =    =
  [7.0, 14.0, 5.0]
```

### Soustraction de vecteurs

```
a = [5,    10,   2]
     -      -    -
b = [2,    4,    3]
     =      =    =
  [3.0,  6.0, -1.0]
```

---

## 15. Flux d'exécution complet

```
                 python tester.py
                        │
                        ▼
           ┌────────────────────────┐
           │ a = [5, 10, 2]         │
           │ b = [2, 4, 3]          │
           └───────────┬────────────┘
                       │
                       ▼
           ┌────────────────────────┐
           │ calculator.dotproduct  │
           │                        │
           │ zip(a,b) →             │
           │ [(5,2),(10,4),(2,3)]   │
           │                        │
           │ 5×2 + 10×4 + 2×3 = 56  │
           └───────────┬────────────┘
                       │
                       ▼
           ┌────────────────────────┐
           │ calculator.add_vec     │
           │                        │
           │ [5+2, 10+4, 2+3]       │
           │ = [7.0, 14.0, 5.0]     │
           └───────────┬────────────┘
                       │
                       ▼
           ┌────────────────────────┐
           │ calculator.sous_vec    │
           │                        │
           │ [5-2, 10-4, 2-3]       │
           │ = [3.0, 6.0, -1.0]     │
           └────────────────────────┘
```

---

## 16. Différence avec l'exercice 03

| Aspect | Exercice 03 | Exercice 04 |
|--------|-------------|-------------|
| Opération | Vecteur-scalaire | Vecteur-vecteur |
| Méthodes | Dunder (`__add__`) | Statiques |
| Appel | `v1 + 5` | `calculator.add_vec(a, b)` |
| Instance | Nécessaire | Non nécessaire |

### Visualisation

```
Exercice 03:                    Exercice 04:

[1, 2, 3] + 5                   [1, 2, 3] + [4, 5, 6]
     │                               │
     ▼                               ▼
[1+5, 2+5, 3+5]                 [1+4, 2+5, 3+6]
= [6, 7, 8]                     = [5, 7, 9]
```

---

## 17. Récapitulatif des nouvelles notions

| Concept | Description |
|---------|-------------|
| `@staticmethod` | Méthode sans `self` ni `cls` |
| Appel sur classe | `calculator.methode()` |
| `zip()` | Combine des itérables |
| Produit scalaire | Σ(ai × bi) |
| Addition vecteurs | [a1+b1, a2+b2, ...] |
| Soustraction vecteurs | [a1-b1, a2-b2, ...] |
| Expression génératrice | `(expr for x in iter)` |
| `sum()` | Somme d'un itérable |