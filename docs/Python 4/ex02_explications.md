# Explications des notions de l'exercice 02 : My first decorating

## 1. Les décorateurs (Decorators)

Un **décorateur** est une fonction qui modifie le comportement d'une autre fonction.

```python
@callLimit(3)
def f():
    print("f()")
```

### Équivalence

```python
# Avec @
@callLimit(3)
def f():
    print("f()")

# Équivalent sans @
def f():
    print("f()")
f = callLimit(3)(f)
```

### Visualisation

```
@callLimit(3)
def f():
    ...
      │
      ▼
┌─────────────────────────────┐
│ 1. callLimit(3) est appelé  │
│    → retourne callLimiter   │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ 2. callLimiter(f) est appelé│
│    → retourne limit_function│
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ 3. f = limit_function       │
│    (f est remplacé)         │
└─────────────────────────────┘
```

---

## 2. Décorateur avec paramètres

Un décorateur avec paramètres nécessite **trois niveaux** de fonctions.

```python
def callLimit(limit: int):           # Niveau 1: Paramètres
    def callLimiter(function):       # Niveau 2: Reçoit la fonction
        def limit_function(...):     # Niveau 3: Remplace la fonction
            ...
        return limit_function
    return callLimiter
```

### Pourquoi trois niveaux ?

| Niveau | Fonction | Reçoit | Retourne |
|--------|----------|--------|----------|
| 1 | `callLimit` | `limit` | `callLimiter` |
| 2 | `callLimiter` | `function` | `limit_function` |
| 3 | `limit_function` | `*args, **kwds` | Résultat |

### Visualisation

```
callLimit(3)
     │
     ▼
callLimiter  ◄── Niveau 2 (décorateur)
     │
     │  @callLimit(3) appliqué à f
     ▼
callLimiter(f)
     │
     ▼
limit_function  ◄── Niveau 3 (wrapper)
```

---

## 3. Le wrapper `limit_function`

Le **wrapper** est la fonction qui remplace l'originale.

```python
def limit_function(*args: Any, **kwds: Any):
    if count[0] < limit:
        count[0] += 1
        return function(*args, **kwds)
    else:
        print(f"Error: {function} call too many times")
        return None
    return limit_function
```

### Rôle du wrapper

| Étape | Action |
|-------|--------|
| 1 | Vérifier si la limite est atteinte |
| 2 | Incrémenter le compteur |
| 3 | Appeler la fonction originale |
| 4 | Retourner le résultat |

### Visualisation

```
f()  ← Appelle en réalité limit_function()
 │
 ▼
┌─────────────────────────────────┐
│ limit_function()                │
│                                 │
│   count[0] < limit ?            │
│        │                        │
│   ┌────┴────┐                   │
│   │ Oui     │ Non               │
│   ▼         ▼                   │
│ count++   print("Error...")     │
│ function()  return None         │
└─────────────────────────────────┘
```

---

## 4. Le compteur avec `count = [0]`

Comme pour l'exercice 01, on utilise une liste pour modifier une variable capturée.

```python
def callLimit(limit: int):
    count = [0]  # Liste pour permettre la modification
```

### Pourquoi une liste ?

```python
# ❌ Ne fonctionne pas
count = 0
def limit_function(...):
    count += 1  # Crée une variable locale

# ✅ Fonctionne
count = [0]
def limit_function(...):
    count[0] += 1  # Modifie l'objet existant
```

### Visualisation

```
callLimit(3)
     │
     ▼
count = [0]  ← Créé une fois
     │
     ▼
callLimiter(f)
     │
     ▼
limit_function  ← Capture count

f()  → count[0] = 1
f()  → count[0] = 2
f()  → count[0] = 3
f()  → count[0] >= limit → Error
```

---

## 5. Transmission des arguments `*args, **kwds`

Le wrapper doit transmettre les arguments à la fonction originale.

```python
def limit_function(*args: Any, **kwds: Any):
    # ...
    return function(*args, **kwds)
```

### Pourquoi ?

La fonction décorée peut avoir n'importe quels paramètres :

```python
@callLimit(3)
def add(a, b):
    return a + b

add(2, 3)  # args = (2, 3)
```

### Visualisation

```
add(2, 3)
    │
    ▼
limit_function(2, 3)
    │
    │  args = (2, 3)
    │  kwds = {}
    │
    ▼
function(*args, **kwds)
    │
    ▼
add(2, 3)  ← Fonction originale
    │
    ▼
   5
```

---

## 6. La syntaxe `@décorateur`

Le symbole `@` est du **sucre syntaxique**.

```python
@callLimit(3)
def f():
    print("f()")
```

### Équivalent explicite

```python
def f():
    print("f()")

f = callLimit(3)(f)
```

### Décomposition

```python
f = callLimit(3)(f)
    │           │
    │           └── Appel 2: callLimiter(f)
    │
    └── Appel 1: callLimit(3) → callLimiter
```

---

## 7. Décorateurs multiples

On peut empiler plusieurs décorateurs.

```python
@decorateur1
@decorateur2
def f():
    pass

# Équivalent à:
f = decorateur1(decorateur2(f))
```

### Ordre d'application

```
@decorateur1
@decorateur2
def f():
    ...

Application: de bas en haut
1. decorateur2(f)
2. decorateur1(résultat)
```

---

## 8. Compteurs indépendants par fonction

Chaque fonction décorée a son propre compteur.

```python
@callLimit(3)
def f():
    print("f()")

@callLimit(1)
def g():
    print("g()")
```

### Visualisation

```
┌─────────────────────┐       ┌─────────────────────┐
│ Closure pour f      │       │ Closure pour g      │
│                     │       │                     │
│ count = [0]         │       │ count = [0]         │
│ limit = 3           │       │ limit = 1           │
│ function = f orig   │       │ function = g orig   │
└─────────────────────┘       └─────────────────────┘
         │                             │
    indépendants                  indépendants
```

---

## 9. Affichage de l'erreur

Quand la limite est atteinte, on affiche un message d'erreur.

```python
print(f"Error: {function} call too many times")
```

### Format de sortie

```
Error: <function g at 0x7fabdc243ee0> call too many times
       │              │
       │              └── Adresse mémoire
       └── Nom de la fonction
```

### `{function}` affiche

Quand on met une fonction dans un f-string, Python affiche sa représentation :

```python
def g():
    pass

print(f"{g}")
# <function g at 0x7fabdc243ee0>
```

---

## 10. Retour `None` en cas d'erreur

Quand la limite est atteinte, le wrapper retourne `None`.

```python
else:
    print(f"Error: {function} call too many times")
    return None
```

### Comportement

| Situation | Retour |
|-----------|--------|
| Appel autorisé | Résultat de `function()` |
| Limite atteinte | `None` |

---

## 11. Structure du fichier callLimit.py

```
callLimit.py
│
├── Import
│   └── from typing import Any
│
└── Fonction callLimit(limit: int)
    │
    ├── count = [0]
    │
    └── Fonction callLimiter(function)
        │
        └── Fonction limit_function(*args, **kwds)
            │
            ├── if count[0] < limit:
            │   ├── count[0] += 1
            │   └── return function(*args, **kwds)
            │
            └── else:
                ├── print(f"Error: ...")
                └── return None
```

---

## 12. Le fichier tester.py

### Code du testeur

```python
from callLimit import callLimit

@callLimit(3)
def f():
    print("f()")

@callLimit(1)
def g():
    print("g()")

for i in range(3):
    f()
    g()
```

### Sortie attendue

```
$> python tester.py
f()
g()
f()
Error: <function g at 0x7fabdc243ee0> call too many times
f()
Error: <function g at 0x7fabdc243ee0> call too many times
$>
```

---

## 13. Analyse de la sortie

### Tableau récapitulatif

| Itération | f() count | f() résultat | g() count | g() résultat |
|-----------|-----------|--------------|-----------|--------------|
| 0 | 0→1 | "f()" | 0→1 | "g()" |
| 1 | 1→2 | "f()" | 1 | Error |
| 2 | 2→3 | "f()" | 1 | Error |

### Explication détaillée

```
Itération 0:
├── f() : count_f=0 < 3 → OK → count_f=1 → "f()"
└── g() : count_g=0 < 1 → OK → count_g=1 → "g()"

Itération 1:
├── f() : count_f=1 < 3 → OK → count_f=2 → "f()"
└── g() : count_g=1 < 1 → NON → Error

Itération 2:
├── f() : count_f=2 < 3 → OK → count_f=3 → "f()"
└── g() : count_g=1 < 1 → NON → Error
```

---

## 14. Flux d'exécution complet

```
@callLimit(3)
def f():
    ...
       │
       ▼
┌─────────────────────────────────┐
│ callLimit(3)                    │
│   limit = 3                     │
│   count = [0]                   │
│   return callLimiter            │
└─────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────┐
│ callLimiter(f)                  │
│   function = f (originale)      │
│   return limit_function         │
└─────────────────────────────────┘
       │
       ▼
f = limit_function (avec closure)

f()
 │
 ▼
┌─────────────────────────────────┐
│ limit_function()                │
│   count[0] = 0 < 3 ? Oui        │
│   count[0] = 1                  │
│   return function()             │
│          │                      │
│          ▼                      │
│   print("f()")                  │
└─────────────────────────────────┘
```

---

## 15. Cas d'usage des décorateurs

### Logging

```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Appel de {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

### Mesure de temps

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Durée: {time.time() - start}s")
        return result
    return wrapper
```

### Cache (memoization)

```python
def cache(func):
    memo = {}
    def wrapper(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return wrapper
```

---

## 16. Le mot-clé `nonlocal` (alternative)

On pourrait aussi utiliser `nonlocal` au lieu d'une liste.

```python
def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args, **kwds):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            # ...
```

### Comparaison

| Approche | Avantage |
|----------|----------|
| `count = [0]` | Plus explicite |
| `nonlocal count` | Plus lisible |

---

## 17. Récapitulatif des nouvelles notions

| Concept | Description |
|---------|-------------|
| Décorateur | Fonction qui modifie une fonction |
| `@decorator` | Sucre syntaxique |
| 3 niveaux | Décorateur avec paramètres |
| Wrapper | Fonction qui remplace l'originale |
| `*args, **kwds` | Transmission des arguments |
| Closure | Capture de `count` et `limit` |
| `count = [0]` | Compteur modifiable |
| Compteurs indépendants | Un par fonction décorée |