# Explications des notions de l'exercice 00 : Calculate my statistics

## 1. Les arguments variables `*args`

`*args` permet de passer un **nombre variable** d'arguments positionnels.

```python
def ft_statistics(*args: Any, **kwargs: Any) -> None:
```

### Fonctionnement

```python
ft_statistics(1, 42, 360, 11, 64, ...)
              │   │   │    │   │
              └───┴───┴────┴───┴──► args = (1, 42, 360, 11, 64, ...)
```

### `args` est un tuple

```python
def exemple(*args):
    print(type(args))  # <class 'tuple'>
    print(args)        # (1, 42, 360, 11, 64)
```

---

## 2. Les arguments nommés `**kwargs`

`**kwargs` permet de passer un **nombre variable** d'arguments nommés (clé=valeur).

### Fonctionnement

```python
ft_statistics(..., toto="mean", tutu="median")
                   │            │
                   └────────────┴──► kwargs = {"toto": "mean", "tutu": "median"}
```

### `kwargs` est un dictionnaire

```python
def exemple(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    print(kwargs)        # {'toto': 'mean', 'tutu': 'median'}
```

---

## 3. Combinaison `*args` et `**kwargs`

### Visualisation

```
ft_statistics(1, 42, 360, toto="mean", tutu="median")
              ───┬─────    ──────────┬──────────────
                 │                   │
                 ▼                   ▼
┌─────────────────────┐    ┌─────────────────────┐
│ *args               │    │ **kwargs            │
│ = (1, 42, 360)      │    │ = {"toto": "mean",  │
│                     │    │    "tutu": "median"}│
└─────────────────────┘    └─────────────────────┘
```

### Règle

```python
def fonction(*args, **kwargs):  # *args AVANT **kwargs
    pass
```

---

## 4. Les fonctions imbriquées (Nested Functions)

Une fonction peut être définie **à l'intérieur** d'une autre fonction.

```python
def ft_statistics(*args, **kwargs):
    
    def mean(data):
        return sum(data) / len(data)
    
    def median(data):
        # ...
```

### Portée (Scope)

```
ft_statistics (fonction externe)
│
├── mean()      ← Fonction interne
├── median()    ← Fonction interne
├── quartile()  ← Fonction interne
├── var()       ← Fonction interne
└── std()       ← Fonction interne
```

### Avantages

| Avantage | Description |
|----------|-------------|
| Encapsulation | Fonctions cachées de l'extérieur |
| Organisation | Code regroupé logiquement |

---

## 5. La moyenne (Mean)

La **moyenne** est la somme des valeurs divisée par leur nombre.

### Formule

```
mean = (x1 + x2 + ... + xn) / n
```

### Implémentation

```python
def mean(data):
    return sum(data) / len(data)
```

### Exemple

```
data = [1, 42, 360, 11, 64]

mean = (1 + 42 + 360 + 11 + 64) / 5
     = 478 / 5
     = 95.6
```

---

## 6. La médiane (Median)

La **médiane** est la valeur centrale d'une série triée.

### Règles

| Cas | Méthode |
|-----|---------|
| n impair | Valeur du milieu |
| n pair | Moyenne des deux valeurs centrales |

### Implémentation

```python
def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]
```

### Exemple (n impair)

```
data = [1, 42, 360, 11, 64]

Tri: [1, 11, 42, 64, 360]
           │
           ▼
      médiane = 42
```

---

## 7. Les quartiles (Quartile)

Les **quartiles** divisent les données en 4 parties égales.

### Définition

| Quartile | Percentile |
|----------|------------|
| Q1 | 25% |
| Q2 | 50% (médiane) |
| Q3 | 75% |

### Implémentation

```python
def quartile(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    q1_idx = int(n * 0.25)
    q3_idx = int(n * 0.75)
    return [float(sorted_data[q1_idx]), float(sorted_data[q3_idx])]
```

### Exemple

```
data = [1, 42, 360, 11, 64]
sorted = [1, 11, 42, 64, 360]
n = 5

q1_idx = int(5 * 0.25) = 1 → sorted[1] = 11
q3_idx = int(5 * 0.75) = 3 → sorted[3] = 64

Résultat: [11.0, 64.0]
```

---

## 8. La variance (Var)

La **variance** mesure la dispersion des données autour de la moyenne.

### Formule

```
var = Σ(xi - mean)² / n
```

### Implémentation

```python
def var(data):
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)
```

### Visualisation

```
Pour chaque xi:
     xi ────► (xi - mean) ────► (xi - mean)²
                                     │
                                     ▼
                               Σ / n = variance
```

---

## 9. L'écart-type (Standard Deviation)

L'**écart-type** est la racine carrée de la variance.

### Formule

```
std = √var
```

### Implémentation

```python
def std(data):
    return var(data) ** 0.5
```

### Relation

```
variance ──────► √ ──────► écart-type
    │                          │
 unité²                      unité
```

---

## 10. Le dictionnaire d'opérations

Un dictionnaire mappe les noms d'opérations aux fonctions.

```python
operations = {
    "mean": mean,
    "median": median,
    "quartile": quartile,
    "var": var,
    "std": std
}
```

### Utilisation

```python
# Au lieu de:
if value == "mean":
    mean(data)
elif value == "median":
    median(data)
# ...

# On fait:
operations[value](data)
```

### Visualisation

```
operations["mean"]
        │
        ▼
┌───────────────────┐
│ Référence vers    │
│ la fonction mean  │
└─────────┬─────────┘
          │
          ▼
    mean(data) → résultat
```

---

## 11. Parcours de `kwargs`

On parcourt les arguments nommés avec `.items()`.

```python
for key, value in kwargs.items():
    if len(args) == 0:
        print("ERROR")
    elif value in operations:
        result = operations[value](list(args))
        print(f"{value} : {result}")
```

### Exemple

```python
kwargs = {"toto": "mean", "tutu": "median"}

for key, value in kwargs.items():
    # Itération 1: key="toto", value="mean"
    # Itération 2: key="tutu", value="median"
```

---

## 12. Gestion des erreurs

### Cas d'erreurs

| Situation | Comportement |
|-----------|--------------|
| `args` vide | Affiche "ERROR" |
| Opération inconnue | N'affiche rien |
| Opération valide | Affiche le résultat |

### Code

```python
for key, value in kwargs.items():
    if len(args) == 0:
        print("ERROR")
    elif value in operations:
        result = operations[value](list(args))
        print(f"{value} : {result}")
```

---

## 13. L'import `Any` depuis `typing`

```python
from typing import Any
```

### Signification

| Type | Description |
|------|-------------|
| `Any` | Accepte n'importe quel type |

### Utilisation

```python
def ft_statistics(*args: Any, **kwargs: Any) -> None:
```

---

## 14. Structure du fichier statistics.py

```
statistics.py
│
├── Import
│   └── from typing import Any
│
└── Fonction ft_statistics(*args, **kwargs)
    │
    ├── Fonctions imbriquées
    │   ├── mean(data)
    │   ├── median(data)
    │   ├── quartile(data)
    │   ├── var(data)
    │   └── std(data)
    │
    ├── Dictionnaire operations
    │
    └── Boucle sur kwargs
```

---

## 15. Le fichier tester.py

### Code du testeur

```python
from statistics import ft_statistics

ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")
```

### Sortie attendue

```
$> python tester.py
mean : 95.6
median : 42
quartile : [11.0, 64.0]
-----
std : 17982.70124086944
var : 323377543.9183673
-----
-----
ERROR
ERROR
ERROR
$>
```

---

## 16. Analyse de la sortie

### Test 1 : Opérations basiques

```
args = (1, 42, 360, 11, 64)

mean: (1+42+360+11+64)/5 = 95.6
median: [1,11,42,64,360] → 42
quartile: [11.0, 64.0]
```

### Test 2 : std et var

```
args = (5, 75, 450, 18, 597, 27474, 48575)

std: 17982.70124086944
var: 323377543.9183673
```

### Test 3 : Opérations inconnues

```
"heheh" not in operations → rien affiché
"kdekem" not in operations → rien affiché
```

### Test 4 : Pas de données

```
args = ()  # vide

len(args) == 0 → ERROR (x3 pour chaque kwarg)
```

---

## 17. Flux d'exécution complet

```
ft_statistics(1, 42, 360, toto="mean")
                    │
                    ▼
┌─────────────────────────────────────┐
│ args = (1, 42, 360)                 │
│ kwargs = {"toto": "mean"}           │
└─────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────┐
│ for key, value in kwargs.items():   │
│     key = "toto", value = "mean"    │
└─────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────┐
│ len(args) == 0 ? Non                │
│ "mean" in operations ? Oui          │
└─────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────┐
│ operations["mean"]([1, 42, 360])    │
│ = mean([1, 42, 360])                │
│ = 134.33...                         │
└─────────────────────────────────────┘
                    │
                    ▼
           print("mean : 134.33...")
```

---

## 18. Récapitulatif des nouvelles notions

| Concept | Description |
|---------|-------------|
| `*args` | Arguments positionnels variables (tuple) |
| `**kwargs` | Arguments nommés variables (dict) |
| Fonctions imbriquées | Fonctions dans une fonction |
| `kwargs.items()` | Parcours clé-valeur |
| Dict de fonctions | Mapper noms → fonctions |
| Mean | Somme / n |
| Median | Valeur centrale |
| Quartile | Q1 (25%) et Q3 (75%) |
| Variance | Dispersion² |
| Écart-type | √variance |