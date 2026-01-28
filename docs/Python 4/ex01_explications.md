# Explications des notions de l'exercice 01 : Outer_inner

## 1. Les fermetures (Closures)

Une **closure** est une fonction interne qui "capture" des variables de sa fonction externe.

```python
def outer(x, function):
    count = [x]
    
    def inner():
        count[0] = function(count[0])
        return count[0]
    
    return inner
```

### Définition

| Terme | Description |
|-------|-------------|
| Closure | Fonction + son environnement capturé |
| Fonction externe | `outer` |
| Fonction interne | `inner` |
| Variable capturée | `count`, `function` |

### Visualisation

```
outer(3, square)
       │
       ▼
┌─────────────────────────────┐
│ Environnement de outer      │
│                             │
│  count = [3]                │
│  function = square          │
│                             │
│  ┌───────────────────────┐  │
│  │ inner()               │  │
│  │ (capture count,       │  │
│  │  function)            │  │
│  └───────────────────────┘  │
└─────────────────────────────┘
       │
       ▼
   return inner  ← inner "emporte" count et function
```

---

## 2. La fonction `square`

`square` retourne le carré d'un nombre.

```python
def square(x: int | float) -> int | float:
    """Retourne le carré de x."""
    return x ** 2
```

### Exemples

| Entrée | Sortie |
|--------|--------|
| `square(3)` | `9` |
| `square(9)` | `81` |
| `square(81)` | `6561` |

### Visualisation

```
square(3)
    │
    ▼
  3 ** 2 = 9
```

---

## 3. La fonction `pow`

`pow` retourne x élevé à la puissance x.

```python
def pow(x: int | float) -> int | float:
    """Retourne x élevé à la puissance x."""
    return x ** x
```

### Exemples

| Entrée | Calcul | Sortie |
|--------|--------|--------|
| `pow(2)` | 2² | `4` |
| `pow(3)` | 3³ | `27` |
| `pow(1.5)` | 1.5^1.5 | `1.837...` |

### Visualisation

```
pow(1.5)
    │
    ▼
  1.5 ** 1.5 = 1.8371173070873836
```

---

## 4. L'annotation de type `int | float`

L'opérateur `|` permet d'accepter plusieurs types (Python 3.10+).

```python
def square(x: int | float) -> int | float:
```

### Équivalent ancien

```python
from typing import Union

def square(x: Union[int, float]) -> Union[int, float]:
```

### Signification

| Annotation | Accepte |
|------------|---------|
| `int` | Entiers uniquement |
| `float` | Flottants uniquement |
| `int \| float` | Entiers OU flottants |

---

## 5. La fonction `outer`

`outer` crée et retourne une closure.

```python
def outer(x: int | float, function) -> object:
    count = [x]

    def inner() -> float:
        count[0] = function(count[0])
        return count[0]

    return inner
```

### Paramètres

| Paramètre | Description |
|-----------|-------------|
| `x` | Valeur initiale |
| `function` | Fonction à appliquer |

### Retour

`outer` retourne la fonction `inner` (pas son résultat).

```python
my_counter = outer(3, square)
# my_counter EST la fonction inner
# my_counter() APPELLE la fonction inner
```

---

## 6. Pourquoi `count = [x]` et pas `count = x` ?

### Le problème avec une variable simple

```python
def outer(x, function):
    count = x  # Variable simple
    
    def inner():
        count = function(count)  # ❌ Crée une NOUVELLE variable locale
        return count
    
    return inner
```

### La solution avec une liste

```python
def outer(x, function):
    count = [x]  # Liste (objet mutable)
    
    def inner():
        count[0] = function(count[0])  # ✅ Modifie l'élément de la liste
        return count[0]
    
    return inner
```

### Explication

| Approche | Problème |
|----------|----------|
| `count = x` | L'assignation `count = ...` crée une variable locale |
| `count = [x]` | La modification `count[0] = ...` modifie l'objet existant |

### Visualisation

```
Avec count = x:                   Avec count = [x]:

outer                             outer
├── count = 3                     ├── count = [3]
│                                 │         │
inner                             inner     │
├── count = 9  ← NOUVELLE         │         │
│   variable locale               │         ▼
                                  └── count[0] = 9
                                      (même objet modifié)
```

---

## 7. Alternative : le mot-clé `nonlocal`

Une autre solution utilise `nonlocal`.

```python
def outer(x, function):
    count = x
    
    def inner():
        nonlocal count  # Indique que count vient de outer
        count = function(count)
        return count
    
    return inner
```

### Comparaison

| Approche | Code |
|----------|------|
| Liste | `count = [x]` puis `count[0] = ...` |
| nonlocal | `nonlocal count` puis `count = ...` |

### Note

L'exercice interdit `global`, mais `nonlocal` est autorisé (différent).

---

## 8. Fonctions comme paramètres

En Python, les fonctions sont des **objets de première classe**.

```python
def outer(x, function):
    # function est une fonction passée en paramètre
```

### Exemples

```python
outer(3, square)   # Passe la fonction square
outer(1.5, pow)    # Passe la fonction pow
```

### Visualisation

```
outer(3, square)
         │
         ▼
┌─────────────────┐
│ function =      │
│   <function     │
│    square>      │
└─────────────────┘
```

### Ce qu'on peut faire avec une fonction

| Action | Exemple |
|--------|---------|
| Passer en paramètre | `outer(3, square)` |
| Assigner à une variable | `f = square` |
| Retourner | `return inner` |
| Stocker dans une liste | `[square, pow]` |

---

## 9. Retourner une fonction

`outer` retourne la fonction `inner` sans l'appeler.

```python
def outer(x, function):
    # ...
    def inner():
        # ...
    return inner  # Sans parenthèses !
```

### Différence

| Syntaxe | Signification |
|---------|---------------|
| `return inner` | Retourne la fonction |
| `return inner()` | Retourne le résultat de l'appel |

### Visualisation

```
outer(3, square)
       │
       ▼
   return inner  ← La fonction elle-même
       │
       ▼
my_counter = inner  ← my_counter EST inner

my_counter()  ← Appelle inner
       │
       ▼
      9
```

---

## 10. État persistant entre les appels

La closure conserve son état entre les appels.

```python
my_counter = outer(3, square)

print(my_counter())  # 9     (3² = 9)
print(my_counter())  # 81    (9² = 81)
print(my_counter())  # 6561  (81² = 6561)
```

### Visualisation

```
Appel 1: my_counter()
┌─────────────────────────┐
│ count[0] = 3            │
│ count[0] = square(3)    │
│ count[0] = 9            │
│ return 9                │
└─────────────────────────┘

Appel 2: my_counter()
┌─────────────────────────┐
│ count[0] = 9            │  ← Garde la valeur précédente
│ count[0] = square(9)    │
│ count[0] = 81           │
│ return 81               │
└─────────────────────────┘

Appel 3: my_counter()
┌─────────────────────────┐
│ count[0] = 81           │
│ count[0] = square(81)   │
│ count[0] = 6561         │
│ return 6561             │
└─────────────────────────┘
```

---

## 11. Plusieurs closures indépendantes

Chaque appel à `outer` crée une closure indépendante.

```python
my_counter = outer(3, square)
another_counter = outer(1.5, pow)
```

### Visualisation

```
┌─────────────────────┐       ┌─────────────────────┐
│ my_counter          │       │ another_counter     │
│                     │       │                     │
│ count = [3]         │       │ count = [1.5]       │
│ function = square   │       │ function = pow      │
└─────────────────────┘       └─────────────────────┘
         │                             │
         │ indépendants                │
         └─────────────────────────────┘
```

---

## 12. Structure du fichier in_out.py

```
in_out.py
│
├── Fonction square(x)
│   └── return x ** 2
│
├── Fonction pow(x)
│   └── return x ** x
│
└── Fonction outer(x, function)
    │
    ├── count = [x]
    │
    ├── Fonction inner()
    │   ├── count[0] = function(count[0])
    │   └── return count[0]
    │
    └── return inner
```

---

## 13. Le fichier tester.py

### Code du testeur

```python
from in_out import outer
from in_out import square
from in_out import pow

my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())
```

### Sortie attendue

```
$> python tester.py
9
81
6561
---
1.8371173070873836
3.056683336818703
30.42684786675409
$>
```

---

## 14. Analyse de la sortie

### Avec `square` (x²)

```
Départ: 3
Appel 1: 3² = 9
Appel 2: 9² = 81
Appel 3: 81² = 6561
```

### Avec `pow` (x^x)

```
Départ: 1.5
Appel 1: 1.5^1.5 = 1.8371173070873836
Appel 2: 1.837...^1.837... = 3.056683336818703
Appel 3: 3.056...^3.056... = 30.42684786675409
```

---

## 15. Flux d'exécution complet

```
my_counter = outer(3, square)
                │
                ▼
┌─────────────────────────────────┐
│ outer(3, square)                │
│                                 │
│   x = 3                         │
│   function = square             │
│   count = [3]                   │
│                                 │
│   def inner(): ...              │
│                                 │
│   return inner                  │
└─────────────────────────────────┘
                │
                ▼
my_counter = inner (avec count=[3], function=square)

my_counter()
      │
      ▼
┌─────────────────────────────────┐
│ inner()                         │
│                                 │
│   count[0] = function(count[0]) │
│   count[0] = square(3)          │
│   count[0] = 9                  │
│                                 │
│   return 9                      │
└─────────────────────────────────┘
```

---

## 16. Cas d'usage des closures

### Factory functions

```python
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

### Compteurs

```python
def counter():
    count = [0]
    def increment():
        count[0] += 1
        return count[0]
    return increment
```

### Callbacks avec état

Les closures permettent de conserver un état sans utiliser de classes.

---

## 17. Récapitulatif des nouvelles notions

| Concept | Description |
|---------|-------------|
| Closure | Fonction + environnement capturé |
| Fonction imbriquée | Fonction définie dans une fonction |
| `count = [x]` | Astuce pour modifier une variable capturée |
| `nonlocal` | Alternative à la liste |
| `int \| float` | Union de types (Python 3.10+) |
| Fonction comme paramètre | Passer une fonction à une autre |
| Retourner une fonction | `return inner` sans parenthèses |
| État persistant | La closure conserve son état |