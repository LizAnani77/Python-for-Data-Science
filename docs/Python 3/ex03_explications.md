# Explications des notions de l'exercice 03 : Calculate my vector

## 1. La surcharge d'opérateurs (Operator Overloading)

La **surcharge d'opérateurs** permet de définir le comportement des opérateurs (`+`, `-`, `*`, `/`) pour nos propres classes.

```python
v1 = calculator([1.0, 2.0, 3.0])
v1 + 5  # Utilise __add__
```

### Principe

| Opération | Méthode appelée |
|-----------|-----------------|
| `obj + x` | `obj.__add__(x)` |
| `obj - x` | `obj.__sub__(x)` |
| `obj * x` | `obj.__mul__(x)` |
| `obj / x` | `obj.__truediv__(x)` |

### Visualisation

```
v1 + 5
   │
   ▼
┌─────────────────────────┐
│ Python traduit en :     │
│ v1.__add__(5)           │
└─────────────────────────┘
   │
   ▼
┌─────────────────────────┐
│ Exécute la méthode      │
│ __add__ de calculator   │
└─────────────────────────┘
```

---

## 2. Les méthodes magiques (Dunder Methods)

Les méthodes entourées de `__` sont appelées **dunder methods** (double underscore) ou **méthodes magiques**.

### Méthodes arithmétiques

| Méthode | Opérateur | Exemple |
|---------|-----------|---------|
| `__add__` | `+` | `a + b` |
| `__sub__` | `-` | `a - b` |
| `__mul__` | `*` | `a * b` |
| `__truediv__` | `/` | `a / b` |
| `__floordiv__` | `//` | `a // b` |
| `__mod__` | `%` | `a % b` |
| `__pow__` | `**` | `a ** b` |

### Méthodes déjà vues

| Méthode | Rôle |
|---------|------|
| `__init__` | Constructeur |
| `__str__` | Conversion en string |
| `__repr__` | Représentation technique |
| `__dict__` | Dictionnaire des attributs |

---

## 3. La méthode `__add__`

`__add__` définit le comportement de l'opérateur `+`.

```python
def __add__(self, scalar) -> None:
    self.vector = [x + scalar for x in self.vector]
    print(self.vector)
```

### Flux d'exécution

```
v1 = calculator([0.0, 1.0, 2.0])
v1 + 5
   │
   ▼
┌─────────────────────────────────┐
│ __add__(self, scalar)           │
│                                 │
│ self.vector = [0.0, 1.0, 2.0]   │
│ scalar = 5                      │
│                                 │
│ Calcul:                         │
│ [0.0+5, 1.0+5, 2.0+5]           │
│ = [5.0, 6.0, 7.0]               │
└─────────────────────────────────┘
   │
   ▼
Affiche: [5.0, 6.0, 7.0]
```

### Visualisation de l'opération

```
Vecteur initial:     [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
                       +    +    +    +    +    +
Scalaire:              5    5    5    5    5    5
                       =    =    =    =    =    =
Résultat:            [5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
```

---

## 4. La méthode `__mul__`

`__mul__` définit le comportement de l'opérateur `*`.

```python
def __mul__(self, scalar) -> None:
    self.vector = [x * scalar for x in self.vector]
    print(self.vector)
```

### Visualisation de l'opération

```
Vecteur initial:     [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
                       ×    ×    ×    ×    ×    ×
Scalaire:              5    5    5    5    5    5
                       =    =    =    =    =    =
Résultat:            [0.0, 5.0, 10.0, 15.0, 20.0, 25.0]
```

---

## 5. La méthode `__sub__`

`__sub__` définit le comportement de l'opérateur `-`.

```python
def __sub__(self, scalar) -> None:
    self.vector = [x - scalar for x in self.vector]
    print(self.vector)
```

### Visualisation de l'opération

```
Vecteur initial:     [10.0, 15.0, 20.0]
                       -     -     -
Scalaire:              5     5     5
                       =     =     =
Résultat:            [5.0, 10.0, 15.0]
```

---

## 6. La méthode `__truediv__`

`__truediv__` définit le comportement de l'opérateur `/`.

```python
def __truediv__(self, scalar) -> None:
    if scalar == 0:
        print("Error: Division by zero")
        return
    self.vector = [x / scalar for x in self.vector]
    print(self.vector)
```

### Gestion de la division par zéro

```
v3 / 5                           v3 / 0
   │                                │
   ▼                                ▼
┌─────────────────┐          ┌─────────────────┐
│ scalar == 0 ?   │          │ scalar == 0 ?   │
│      Non        │          │      Oui        │
└────────┬────────┘          └────────┬────────┘
         │                            │
         ▼                            ▼
┌─────────────────┐          ┌─────────────────┐
│ Calcul normal   │          │ "Error: Div..." │
│ [x/5 for x...] │          │ return          │
└─────────────────┘          └─────────────────┘
```

### Visualisation de l'opération

```
Vecteur initial:     [5.0, 10.0, 15.0]
                       ÷     ÷     ÷
Scalaire:              5     5     5
                       =     =     =
Résultat:            [1.0, 2.0, 3.0]
```

---

## 7. Les List Comprehensions

Une **list comprehension** est une syntaxe concise pour créer des listes.

```python
[x + scalar for x in self.vector]
```

### Syntaxe

```python
[expression for element in iterable]
```

### Équivalent avec boucle for

```python
# List comprehension
result = [x + scalar for x in self.vector]

# Équivalent avec for
result = []
for x in self.vector:
    result.append(x + scalar)
```

### Visualisation

```
self.vector = [0.0, 1.0, 2.0]
scalar = 5

[x + scalar for x in self.vector]
     │               │
     │               └── Parcourt [0.0, 1.0, 2.0]
     │
     └── Applique x + 5 à chaque élément

Itération 1: x = 0.0 → 0.0 + 5 = 5.0
Itération 2: x = 1.0 → 1.0 + 5 = 6.0
Itération 3: x = 2.0 → 2.0 + 5 = 7.0

Résultat: [5.0, 6.0, 7.0]
```

### Avantages

| Aspect | Boucle for | List comprehension |
|--------|------------|-------------------|
| Lignes | 3-4 lignes | 1 ligne |
| Lisibilité | Explicite | Concis |
| Performance | Standard | Légèrement plus rapide |

---

## 8. Modification in-place

Les méthodes modifient le vecteur **en place** (directement dans l'objet).

```python
def __add__(self, scalar) -> None:
    self.vector = [x + scalar for x in self.vector]  # Modifie self.vector
    print(self.vector)
```

### Visualisation

```
Avant v1 + 5:
┌─────────────────────────────┐
│ v1                          │
│ vector = [0.0, 1.0, 2.0]    │
└─────────────────────────────┘

Après v1 + 5:
┌─────────────────────────────┐
│ v1                          │
│ vector = [5.0, 6.0, 7.0]    │  ← Modifié !
└─────────────────────────────┘
```

### Conséquence : chaînage d'opérations

```python
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5  # [5.0, 10.0, 15.0]
v3 / 5  # [1.0, 2.0, 3.0]  ← Opère sur le résultat précédent
```

---

## 9. Retour `None` vs retour de valeur

Les méthodes retournent `None` et affichent le résultat.

```python
def __add__(self, scalar) -> None:  # Retourne None
    self.vector = [x + scalar for x in self.vector]
    print(self.vector)  # Affiche le résultat
```

### Comparaison

| Approche | Code | Usage |
|----------|------|-------|
| Retourne None | `v1 + 5` | Modifie v1, affiche |
| Retourne self | `v1 = v1 + 5` | Permet le chaînage |
| Retourne nouveau | `v2 = v1 + 5` | v1 inchangé |

### Dans cet exercice

```python
v1 + 5      # ✅ Affiche et modifie v1
x = v1 + 5  # x sera None (pas utile)
```

---

## 10. Opérations vecteur-scalaire

### Qu'est-ce qu'un scalaire ?

Un **scalaire** est un nombre unique (pas une liste).

| Type | Exemple |
|------|---------|
| Scalaire | `5`, `3.14`, `-2` |
| Vecteur | `[1, 2, 3]` |

### Opération vecteur-scalaire

```
Vecteur:    [a, b, c]
             ○  ○  ○
Opération:   +  +  +
             ○  ○  ○
Scalaire:    s  s  s

Résultat:   [a+s, b+s, c+s]
```

### Chaque élément est traité individuellement

```python
[0.0, 1.0, 2.0] + 5

    0.0 + 5 = 5.0
    1.0 + 5 = 6.0
    2.0 + 5 = 7.0

Résultat: [5.0, 6.0, 7.0]
```

---

## 11. Convention de nommage : minuscule

La classe s'appelle `calculator` (minuscule), ce qui déroge à la convention PascalCase.

```python
class calculator:  # minuscule (inhabituel)
    pass

class Calculator:  # PascalCase (convention standard)
    pass
```

### Conventions Python (PEP 8)

| Élément | Convention | Exemple |
|---------|------------|---------|
| Classe | PascalCase | `Calculator` |
| Fonction | snake_case | `calculate_sum` |
| Variable | snake_case | `my_vector` |
| Constante | MAJUSCULES | `MAX_VALUE` |

### Dans cet exercice

L'énoncé demande `calculator` en minuscule, donc on respecte l'énoncé.

---

## 12. Structure du fichier ft_calculator.py

```
ft_calculator.py
│
└── Classe calculator
    │
    ├── Docstring
    │
    ├── __init__(vector: list)
    │   └── self.vector = vector
    │
    ├── __add__(scalar) → None
    │   └── Addition élément par élément
    │
    ├── __mul__(scalar) → None
    │   └── Multiplication élément par élément
    │
    ├── __sub__(scalar) → None
    │   └── Soustraction élément par élément
    │
    └── __truediv__(scalar) → None
        ├── Vérification division par zéro
        └── Division élément par élément
```

---

## 13. Le fichier tester.py

### Code du testeur

```python
from ft_calculator import calculator

v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 5
```

### Sortie attendue

```
$> python tester.py
[5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
---
[0.0, 5.0, 10.0, 15.0, 20.0, 25.0]
---
[5.0, 10.0, 15.0]
[1.0, 2.0, 3.0]
$>
```

---

## 14. Analyse de la sortie

### Opération v1 + 5

```
[0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
  +5   +5   +5   +5   +5   +5
[5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
```

### Opération v2 * 5

```
[0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
  ×5   ×5   ×5   ×5   ×5   ×5
[0.0, 5.0, 10.0, 15.0, 20.0, 25.0]
```

### Opérations v3 - 5 puis v3 / 5

```
Étape 1: v3 - 5
[10.0, 15.0, 20.0]
  -5    -5    -5
[5.0, 10.0, 15.0]

Étape 2: v3 / 5 (sur le résultat précédent)
[5.0, 10.0, 15.0]
  ÷5    ÷5   ÷5
[1.0, 2.0, 3.0]
```

---

## 15. Flux d'exécution complet

```
                 python tester.py
                        │
                        ▼
           ┌────────────────────────┐
           │ v1 = calculator(...)   │
           │ vector = [0,1,2,3,4,5] │
           └───────────┬────────────┘
                       │
                       ▼
           ┌────────────────────────┐
           │ v1 + 5                 │
           │ → v1.__add__(5)        │
           │ → [5,6,7,8,9,10]       │
           └───────────┬────────────┘
                       │
                       ▼
           ┌────────────────────────┐
           │ v2 = calculator(...)   │
           │ v2 * 5                 │
           │ → v2.__mul__(5)        │
           │ → [0,5,10,15,20,25]    │
           └───────────┬────────────┘
                       │
                       ▼
           ┌────────────────────────┐
           │ v3 = calculator(...)   │
           │ v3 - 5                 │
           │ → [5,10,15]            │
           │                        │
           │ v3 / 5                 │
           │ → [1,2,3]              │
           └────────────────────────┘
```

---

## 16. Opérateurs inversés (pour aller plus loin)

Python propose aussi des opérateurs **inversés** pour gérer `5 + v1`.

| Méthode | Opération | Appelée quand |
|---------|-----------|---------------|
| `__add__` | `v1 + 5` | Objet à gauche |
| `__radd__` | `5 + v1` | Objet à droite |

### Exemple (non demandé dans l'exercice)

```python
def __radd__(self, scalar):
    return self.__add__(scalar)
```

### Sans `__radd__`

```python
v1 + 5  # ✅ Fonctionne
5 + v1  # ❌ TypeError
```

---

## 17. Récapitulatif des nouvelles notions

| Concept | Description |
|---------|-------------|
| `__add__` | Surcharge de `+` |
| `__sub__` | Surcharge de `-` |
| `__mul__` | Surcharge de `*` |
| `__truediv__` | Surcharge de `/` |
| List comprehension | `[x + s for x in v]` |
| Modification in-place | Modifie `self.vector` |
| Opération vecteur-scalaire | Applique à chaque élément |