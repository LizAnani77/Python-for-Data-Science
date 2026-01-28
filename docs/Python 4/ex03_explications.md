# Explications des notions de l'exercice 03 : Data class

## 1. Les dataclasses

Une **dataclass** est une classe simplifiée pour stocker des données.

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    surname: str
```

### Comparaison classe normale vs dataclass

```python
# Classe normale
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def __repr__(self):
        return f"Student(name='{self.name}', surname='{self.surname}')"

# Dataclass (équivalent)
@dataclass
class Student:
    name: str
    surname: str
```

### Avantages

| Avantage | Description |
|----------|-------------|
| Moins de code | Pas besoin d'écrire `__init__` |
| `__repr__` automatique | Affichage lisible |
| `__eq__` automatique | Comparaison par valeurs |

---

## 2. Le décorateur `@dataclass`

`@dataclass` transforme une classe en dataclass.

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    surname: str
```

### Ce que génère `@dataclass`

```python
# @dataclass génère automatiquement:

def __init__(self, name: str, surname: str):
    self.name = name
    self.surname = surname

def __repr__(self):
    return f"Student(name='{self.name}', surname='{self.surname}')"

def __eq__(self, other):
    return (self.name, self.surname) == (other.name, other.surname)
```

### Visualisation

```
@dataclass
class Student:
    name: str
    surname: str
        │
        ▼
┌─────────────────────────────────┐
│ Python génère automatiquement: │
│                                 │
│ • __init__                      │
│ • __repr__                      │
│ • __eq__                        │
└─────────────────────────────────┘
```

---

## 3. Les annotations de type dans les dataclasses

Dans une dataclass, chaque attribut **doit** avoir une annotation de type.

```python
@dataclass
class Student:
    name: str           # Obligatoire
    surname: str        # Obligatoire
    active: bool = True # Avec valeur par défaut
```

### Ordre des attributs

```python
@dataclass
class Student:
    # D'abord les attributs SANS valeur par défaut
    name: str
    surname: str
    
    # Ensuite les attributs AVEC valeur par défaut
    active: bool = True
```

### Pourquoi cet ordre ?

```python
# ❌ Erreur : attribut sans défaut après attribut avec défaut
@dataclass
class Student:
    active: bool = True
    name: str  # TypeError!

# ✅ Correct
@dataclass
class Student:
    name: str
    active: bool = True
```

---

## 4. La fonction `field()`

`field()` permet de configurer un attribut de manière avancée.

```python
from dataclasses import dataclass, field

@dataclass
class Student:
    login: str = field(init=False)
    id: str = field(init=False)
```

### Paramètres de `field()`

| Paramètre | Description |
|-----------|-------------|
| `init=False` | Exclut du `__init__` |
| `repr=False` | Exclut du `__repr__` |
| `default=value` | Valeur par défaut |
| `default_factory=func` | Fonction pour valeur par défaut |

### Visualisation

```
@dataclass
class Student:
    name: str                      ← Dans __init__
    surname: str                   ← Dans __init__
    active: bool = True            ← Dans __init__ (optionnel)
    login: str = field(init=False) ← PAS dans __init__
    id: str = field(init=False)    ← PAS dans __init__
```

---

## 5. Le paramètre `init=False`

`init=False` exclut un attribut du constructeur généré.

```python
login: str = field(init=False)
id: str = field(init=False)
```

### Conséquence

```python
# Avec init=False, ces appels échouent:
student = Student(name="Edward", surname="agle", id="toto")
# TypeError: __init__() got an unexpected keyword argument 'id'

student = Student(name="Edward", surname="agle", login="test")
# TypeError: __init__() got an unexpected keyword argument 'login'
```

### Visualisation

```
Student(name="Edward", surname="agle")
                │
                ▼
┌─────────────────────────────────┐
│ __init__ généré:                │
│                                 │
│ def __init__(self, name,        │
│              surname,           │
│              active=True):      │
│     self.name = name            │
│     self.surname = surname      │
│     self.active = active        │
│     # login et id NON inclus    │
└─────────────────────────────────┘
```

---

## 6. La méthode `__post_init__`

`__post_init__` est appelée automatiquement **après** `__init__`.

```python
@dataclass
class Student:
    name: str
    surname: str
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        self.login = self.name[0].upper() + self.surname
        self.id = generate_id()
```

### Ordre d'exécution

```
Student("Edward", "agle")
           │
           ▼
┌─────────────────────────────────┐
│ 1. __init__ (généré)            │
│    self.name = "Edward"         │
│    self.surname = "agle"        │
│    self.active = True           │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 2. __post_init__ (manuel)       │
│    self.login = "Eagle"         │
│    self.id = "trannxhndgtolvh"  │
└─────────────────────────────────┘
```

### Cas d'usage

| Utilisation | Exemple |
|-------------|---------|
| Valeurs calculées | `login` basé sur `name` et `surname` |
| Génération | `id` aléatoire |
| Validation | Vérifier les valeurs |

---

## 7. Génération du login

Le login est créé à partir du nom et prénom.

```python
def __post_init__(self):
    self.login = self.name[0].upper() + self.surname
```

### Décomposition

```python
self.name = "Edward"
self.surname = "agle"

self.name[0]           # "E"
self.name[0].upper()   # "E"
self.surname           # "agle"

self.login = "E" + "agle"  # "Eagle"
```

### Visualisation

```
name = "Edward"    surname = "agle"
  │                    │
  ▼                    │
name[0] = "E"          │
  │                    │
  ▼                    │
"E".upper() = "E"      │
  │                    │
  └────────┬───────────┘
           │
           ▼
    "E" + "agle" = "Eagle"
```

---

## 8. La fonction `generate_id`

`generate_id` crée un identifiant aléatoire de 15 caractères.

```python
import random
import string

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))
```

### Décomposition

| Élément | Description |
|---------|-------------|
| `string.ascii_lowercase` | `"abcdefghijklmnopqrstuvwxyz"` |
| `random.choices(..., k=15)` | Choisit 15 lettres avec remise |
| `"".join(...)` | Concatène en une chaîne |

### Visualisation

```
random.choices(string.ascii_lowercase, k=15)
                        │
                        ▼
['t', 'r', 'a', 'n', 'n', 'x', 'h', 'n', 'd', 'g', 't', 'o', 'l', 'v', 'h']
                        │
                        ▼
            "".join([...])
                        │
                        ▼
              "trannxhndgtolvh"
```

---

## 9. Le module `random`

`random` fournit des fonctions pour la génération aléatoire.

### Fonctions utiles

| Fonction | Description |
|----------|-------------|
| `random.choice(seq)` | Un élément au hasard |
| `random.choices(seq, k=n)` | n éléments avec remise |
| `random.sample(seq, k=n)` | n éléments sans remise |
| `random.randint(a, b)` | Entier entre a et b |

### Différence `choices` vs `sample`

```python
# choices: peut répéter (avec remise)
random.choices("abc", k=5)  # ['a', 'b', 'a', 'a', 'c']

# sample: pas de répétition (sans remise)
random.sample("abc", k=3)   # ['c', 'a', 'b']
```

---

## 10. Le module `string`

`string` contient des constantes de caractères utiles.

### Constantes disponibles

| Constante | Valeur |
|-----------|--------|
| `string.ascii_lowercase` | `"abcdefghijklmnopqrstuvwxyz"` |
| `string.ascii_uppercase` | `"ABCDEFGHIJKLMNOPQRSTUVWXYZ"` |
| `string.ascii_letters` | Minuscules + majuscules |
| `string.digits` | `"0123456789"` |

---

## 11. La méthode `str.join()`

`join()` concatène une liste de chaînes.

```python
"".join(['a', 'b', 'c'])  # "abc"
```

### Syntaxe

```python
séparateur.join(itérable)
```

### Exemples

| Expression | Résultat |
|------------|----------|
| `"".join(['a', 'b', 'c'])` | `"abc"` |
| `"-".join(['a', 'b', 'c'])` | `"a-b-c"` |
| `" ".join(['Hello', 'World'])` | `"Hello World"` |

---

## 12. `__repr__` automatique

La dataclass génère automatiquement `__repr__`.

```python
student = Student(name="Edward", surname="agle")
print(student)
# Student(name='Edward', surname='agle', active=True, login='Eagle', id='trannxhndgtolvh')
```

### Sans dataclass

```python
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

student = Student("Edward", "agle")
print(student)
# <__main__.Student object at 0x7f...>
```

### Avec dataclass

```python
@dataclass
class Student:
    name: str
    surname: str

student = Student("Edward", "agle")
print(student)
# Student(name='Edward', surname='agle')
```

---

## 13. Structure du fichier new_student.py

```
new_student.py
│
├── Imports
│   ├── import random
│   ├── import string
│   └── from dataclasses import dataclass, field
│
├── Fonction generate_id()
│   └── return "".join(random.choices(...))
│
└── @dataclass
    class Student:
    │
    ├── Attributs
    │   ├── name: str
    │   ├── surname: str
    │   ├── active: bool = True
    │   ├── login: str = field(init=False)
    │   └── id: str = field(init=False)
    │
    └── __post_init__(self)
        ├── self.login = ...
        └── self.id = generate_id()
```

---

## 14. Le fichier tester.py (test 1)

### Code du testeur

```python
from new_student import Student

student = Student(name="Edward", surname="agle")
print(student)
```

### Sortie attendue

```
$> python tester.py
Student(name='Edward', surname='agle', active=True, login='Eagle', id='trannxhndgtolvh')
$>
```

### Note

L'`id` est aléatoire, donc différent à chaque exécution.

---

## 15. Le fichier tester.py (test 2)

### Code du testeur

```python
from new_student import Student

student = Student(name="Edward", surname="agle", id="toto")
print(student)
```

### Sortie attendue

```
$> python tester.py
...
TypeError: Student.__init__() got an unexpected keyword argument 'id'
$>
```

### Explication

`login` et `id` ont `init=False`, donc ils ne peuvent pas être passés au constructeur.

---

## 16. Flux d'exécution complet

```
from new_student import Student
              │
              ▼
┌─────────────────────────────────┐
│ Import du module                │
│ - generate_id définie           │
│ - Student définie               │
└──────────────┬──────────────────┘
               │
               ▼
student = Student(name="Edward", surname="agle")
               │
               ▼
┌─────────────────────────────────┐
│ Appel __init__                  │
│   self.name = "Edward"          │
│   self.surname = "agle"         │
│   self.active = True            │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ Appel __post_init__             │
│   self.login = "Eagle"          │
│   self.id = "trannxhndgtolvh"   │
└──────────────┬──────────────────┘
               │
               ▼
print(student)
               │
               ▼
┌─────────────────────────────────┐
│ Appel __repr__ (généré)         │
│ Student(name='Edward', ...)     │
└─────────────────────────────────┘
```

---

## 17. Récapitulatif des nouvelles notions

| Concept | Description |
|---------|-------------|
| `@dataclass` | Décorateur pour classes de données |
| `field()` | Configuration avancée d'attributs |
| `init=False` | Exclut du constructeur |
| `__post_init__` | Appelé après `__init__` |
| `random.choices()` | Choix aléatoires avec remise |
| `string.ascii_lowercase` | Lettres minuscules |
| `"".join()` | Concaténation de liste |
| `__repr__` automatique | Affichage généré |