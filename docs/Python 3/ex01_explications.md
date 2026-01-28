# Explications des notions de l'exercice 01 : GOT S1E7

## 1. Importer depuis un autre module

L'exercice 01 réutilise la classe `Character` créée dans l'exercice 00.

```python
from S1E9 import Character
```

### Structure des fichiers

```
ex01/
├── S1E9.py      # Contient Character et Stark (copié depuis ex00)
└── S1E7.py      # Contient Baratheon et Lannister (nouveau)
```

### Syntaxes d'import

| Syntaxe | Description | Utilisation |
|---------|-------------|-------------|
| `from module import classe` | Importe une classe | `Character(...)` |
| `import module` | Importe le module | `S1E9.Character(...)` |
| `from module import *` | Importe tout | ⚠️ Interdit |

### Comment Python trouve le module ?

```
Python cherche S1E9.py dans cet ordre :

1. Répertoire courant ← Trouvé ici
2. PYTHONPATH
3. Répertoires système

ex01/
├── S1E9.py   ← Python le trouve
└── S1E7.py   ← Fichier qui importe
```

---

## 2. Enrichir une sous-classe

Les classes `Baratheon` et `Lannister` héritent de `Character` et ajoutent des attributs.

```python
def __init__(self, first_name: str, is_alive: bool = True):
    super().__init__(first_name, is_alive)  # Hérités
    self.family_name = "Baratheon"          # Nouveaux
    self.eyes = "brown"
    self.hairs = "dark"
```

### Visualisation de l'héritage

```
         Character (ABC)
         ┌─────────────────┐
         │ first_name      │
         │ is_alive        │
         │ die()           │
         └────────┬────────┘
                  │
       ┌──────────┴──────────┐
       ▼                     ▼
┌─────────────────┐   ┌─────────────────┐
│   Baratheon     │   │   Lannister     │
├─────────────────┤   ├─────────────────┤
│ family_name     │   │ family_name     │
│ eyes            │   │ eyes            │
│ hairs           │   │ hairs           │
├─────────────────┤   ├─────────────────┤
│ __str__()       │   │ __str__()       │
│ __repr__()      │   │ __repr__()      │
│                 │   │ create_lannister│
└─────────────────┘   └─────────────────┘
```

### Attributs par famille

| Attribut | Baratheon | Lannister |
|----------|-----------|-----------|
| `family_name` | `"Baratheon"` | `"Lannister"` |
| `eyes` | `"brown"` | `"blue"` |
| `hairs` | `"dark"` | `"light"` |

---

## 3. Ordre d'initialisation des attributs

L'ordre dans `__init__` est important : d'abord le parent, puis les nouveaux attributs.

```python
def __init__(self, first_name: str, is_alive: bool = True):
    super().__init__(first_name, is_alive)  # 1. Parent d'abord
    self.family_name = "Baratheon"          # 2. Puis les nouveaux
    self.eyes = "brown"
    self.hairs = "dark"
```

### Flux de création

```
Baratheon("Robert")
         │
         ▼
┌─────────────────────────────────┐
│ 1. super().__init__("Robert")   │
│    → first_name = "Robert"      │
│    → is_alive = True            │
└─────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│ 2. Attributs Baratheon          │
│    → family_name = "Baratheon"  │
│    → eyes = "brown"             │
│    → hairs = "dark"             │
└─────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│ Objet final:                    │
│ {                               │
│   'first_name': 'Robert',       │
│   'is_alive': True,             │
│   'family_name': 'Baratheon',   │
│   'eyes': 'brown',              │
│   'hairs': 'dark'               │
│ }                               │
└─────────────────────────────────┘
```

---

## 4. La méthode `__str__`

`__str__` définit la représentation **lisible** d'un objet.

```python
def __str__(self):
    return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
```

### Quand est-elle appelée ?

| Situation | Appelle `__str__` |
|-----------|-------------------|
| `print(objet)` | ✅ |
| `str(objet)` | ✅ |
| `f"{objet}"` | ✅ |

### Sans vs avec `__str__`

```
Sans __str__:
>>> print(Robert)
<S1E7.Baratheon object at 0x7f8b8c0b4a90>

Avec __str__:
>>> print(Robert)
Vector: ('Baratheon', 'brown', 'dark')
```

---

## 5. La méthode `__repr__`

`__repr__` définit la représentation **technique** d'un objet.

```python
def __repr__(self):
    return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
```

### Différence `__str__` vs `__repr__`

| Aspect | `__str__` | `__repr__` |
|--------|-----------|------------|
| Public | Utilisateur | Développeur |
| Objectif | Lisibilité | Précision |
| Appelé par | `print()` | Terminal, `repr()` |
| Fallback | Utilise `__repr__` | Utilise `object.__repr__` |

### Quand `__repr__` est appelé

```python
>>> Robert          # Terminal interactif → __repr__
>>> [Robert]        # Dans une liste → __repr__
>>> repr(Robert)    # Explicitement → __repr__
```

---

## 6. Accès vs appel de méthode

Le testeur accède aux méthodes **sans les appeler** :

```python
print(Robert.__str__)   # Accès (sans parenthèses)
print(Robert.__str__()) # Appel (avec parenthèses)
```

### Différence

| Syntaxe | Action | Résultat |
|---------|--------|----------|
| `obj.__str__` | Accès | `<bound method ...>` |
| `obj.__str__()` | Appel | `"Vector: (...)"` |

### Sortie du testeur

```
<bound method Baratheon.__str__ of Vector: ('Baratheon', 'brown', 'dark')>
│                                   │
│                                   └── __repr__ de l'objet
└── Type de l'attribut
```

### Visualisation

```
Robert.__str__
      │
      ▼
┌─────────────────────────────────────────────────────────────┐
│ <bound method Baratheon.__str__ of Vector: ('Baratheon'...)>│
│                                                             │
│  "bound method" = méthode liée à une instance               │
│  "of Vector..." = représentation de l'instance (__repr__)   │
└─────────────────────────────────────────────────────────────┘

Robert.__str__()
      │
      ▼
┌─────────────────────────────────────┐
│ "Vector: ('Baratheon', 'brown'...)" │
└─────────────────────────────────────┘
```

---

## 7. Le décorateur `@classmethod`

Une **méthode de classe** reçoit la classe comme premier argument, pas l'instance.

```python
@classmethod
def create_lannister(cls, first_name: str, is_alive: bool = True):
    return cls(first_name, is_alive)
```

### Comparaison des types de méthodes

| Type | Décorateur | 1er param | Reçoit |
|------|------------|-----------|--------|
| Instance | aucun | `self` | L'objet |
| Classe | `@classmethod` | `cls` | La classe |
| Statique | `@staticmethod` | aucun | Rien |

### Visualisation

```
Méthode d'instance              Méthode de classe
──────────────────              ─────────────────

cersei.die()                    Lannister.create_lannister(...)
      │                                   │
      ▼                                   ▼
┌───────────┐                       ┌───────────┐
│   self    │                       │    cls    │
│ = cersei  │                       │= Lannister│
└───────────┘                       └───────────┘
```

---

## 8. Le paramètre `cls`

`cls` est une convention pour nommer le premier paramètre d'une méthode de classe.

```python
@classmethod
def create_lannister(cls, first_name: str, is_alive: bool = True):
    return cls(first_name, is_alive)
```

### Que représente `cls` ?

| Appel | `cls` vaut |
|-------|------------|
| `Lannister.create_lannister(...)` | `Lannister` |
| Depuis une sous-classe | La sous-classe |

### Pourquoi `cls` et pas `Lannister` ?

```python
# ❌ Nom en dur (moins flexible)
def create_lannister(first_name, is_alive=True):
    return Lannister(first_name, is_alive)

# ✅ Utilise cls (flexible avec l'héritage)
@classmethod
def create_lannister(cls, first_name, is_alive=True):
    return cls(first_name, is_alive)
```

---

## 9. Utilisation de `create_lannister`

### Syntaxe d'appel

```python
Jaime = Lannister.create_lannister("Jaime", True)
```

### Flux d'exécution

```
Lannister.create_lannister("Jaime", True)
                │
                ▼
┌───────────────────────────────────┐
│ @classmethod                      │
│ def create_lannister(cls, ...):   │
│                                   │
│   cls = Lannister                 │
│   first_name = "Jaime"            │
│   is_alive = True                 │
│                                   │
│   return cls(first_name, is_alive)│
│          │                        │
│          └── Lannister("Jaime")   │
└───────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────┐
│ Équivalent à :                    │
│ Lannister("Jaime", True)          │
└───────────────────────────────────┘
```

### Équivalence

```python
# Ces deux lignes produisent le même résultat :
Jaime = Lannister.create_lannister("Jaime", True)
Jaime = Lannister("Jaime", True)
```

---

## 10. Pattern Factory

Les `@classmethod` sont souvent utilisées comme **factory methods**.

### Qu'est-ce qu'une factory ?

Une factory est une méthode qui **crée et retourne** des instances.

```
┌─────────────────────────────────────────┐
│           Factory Method                │
│                                         │
│  Entrée: paramètres                     │
│          │                              │
│          ▼                              │
│  ┌─────────────────┐                    │
│  │ Logique de      │                    │
│  │ création        │                    │
│  └────────┬────────┘                    │
│           │                             │
│           ▼                             │
│  Sortie: nouvelle instance              │
└─────────────────────────────────────────┘
```

### Avantages

| Avantage | Description |
|----------|-------------|
| Lisibilité | Nom explicite |
| Flexibilité | Fonctionne avec l'héritage |
| Alternatives | Plusieurs "constructeurs" possibles |

---

## 11. La fonction `type()`

Le testeur utilise `type()` pour obtenir des informations sur la classe.

```python
print(f"Name : {Jaime.first_name, type(Jaime).__name__}, Alive : {Jaime.is_alive}")
```

### Décomposition

| Expression | Résultat |
|------------|----------|
| `type(Jaime)` | `<class 'S1E7.Lannister'>` |
| `type(Jaime).__name__` | `'Lannister'` |

### Visualisation

```
type(Jaime)
     │
     ▼
<class 'S1E7.Lannister'>
            │
            └──► .__name__ ──► 'Lannister'
```

### Autres fonctions utiles

| Fonction | Description | Exemple |
|----------|-------------|---------|
| `type(obj)` | Classe de l'objet | `<class 'Lannister'>` |
| `type(obj).__name__` | Nom de la classe | `'Lannister'` |
| `isinstance(obj, cls)` | Vérifie le type | `True/False` |

---

## 12. Les f-strings

Les f-strings permettent d'insérer des expressions dans des chaînes.

```python
f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
```

### Syntaxe

```python
f"texte {expression} texte"
```

### Exemples

| Expression | Résultat |
|------------|----------|
| `f"Nom: {name}"` | `"Nom: Robert"` |
| `f"2+2 = {2+2}"` | `"2+2 = 4"` |
| `f"{obj.attr}"` | Valeur de l'attribut |

### Dans le code

```python
self.family_name = "Baratheon"
self.eyes = "brown"
self.hairs = "dark"

f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
# → "Vector: ('Baratheon', 'brown', 'dark')"
```

---

## 13. Structure du fichier S1E7.py

```
S1E7.py
│
├── Import
│   └── from S1E9 import Character
│
├── Classe Baratheon (Character)
│   ├── Docstring
│   ├── __init__
│   │   ├── super().__init__(...)
│   │   ├── family_name = "Baratheon"
│   │   ├── eyes = "brown"
│   │   └── hairs = "dark"
│   ├── __str__
│   └── __repr__
│
└── Classe Lannister (Character)
    ├── Docstring
    ├── __init__
    │   ├── super().__init__(...)
    │   ├── family_name = "Lannister"
    │   ├── eyes = "blue"
    │   └── hairs = "light"
    ├── __str__
    ├── __repr__
    └── @classmethod create_lannister
```

---

## 14. Le fichier tester.py

### Code du testeur

```python
from S1E7 import Baratheon, Lannister

Robert = Baratheon("Robert")
print(Robert.__dict__)
print(Robert.__str__)
print(Robert.__repr__)
print(Robert.is_alive)
Robert.die()
print(Robert.is_alive)
print(Robert.__doc__)
print("---")
Cersei = Lannister("Cersei")
print(Cersei.__dict__)
print(Cersei.__str__)
print(Cersei.is_alive)
print("---")
Jaime = Lannister.create_lannister("Jaime", True)
print(f"Name : {Jaime.first_name, type(Jaime).__name__}, Alive : {Jaime.is_alive}")
```

### Sortie attendue

```
$> python tester.py
{'first_name': 'Robert', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'brown', 'hairs': 'dark'}
<bound method Baratheon.__str__ of Vector: ('Baratheon', 'brown', 'dark')>
<bound method Baratheon.__repr__ of Vector: ('Baratheon', 'brown', 'dark')>
True
False
Representing the Baratheon family.
---
{'first_name': 'Cersei', 'is_alive': True, 'family_name': 'Lannister', 'eyes': 'blue', 'hairs': 'light'}
<bound method Lannister.__str__ of Vector: ('Lannister', 'blue', 'light')>
True
---
Name : ('Jaime', 'Lannister'), Alive : True
$>
```

---

## 15. Analyse de la sortie

### Partie Robert (Baratheon)

| Ligne | Code | Explication |
|-------|------|-------------|
| 1 | `Robert.__dict__` | Tous les attributs |
| 2 | `Robert.__str__` | Méthode (non appelée) |
| 3 | `Robert.__repr__` | Méthode (non appelée) |
| 4 | `Robert.is_alive` | `True` |
| 5 | `Robert.die()` | Modifie is_alive |
| 6 | `Robert.is_alive` | `False` |
| 7 | `Robert.__doc__` | Docstring |

### Partie Cersei (Lannister)

| Ligne | Code | Explication |
|-------|------|-------------|
| 9 | `Cersei.__dict__` | Attributs Lannister |
| 10 | `Cersei.__str__` | Méthode (non appelée) |
| 11 | `Cersei.is_alive` | `True` |

### Partie Jaime (create_lannister)

| Ligne | Code | Explication |
|-------|------|-------------|
| 13 | `create_lannister(...)` | Factory method |
| 14 | `type(Jaime).__name__` | `'Lannister'` |

---

## 16. Flux d'exécution complet

```
                    python tester.py
                           │
                           ▼
              ┌────────────────────────────┐
              │ from S1E7 import ...       │
              │ (charge aussi S1E9)        │
              └─────────────┬──────────────┘
                            │
              ┌─────────────┴──────────────┐
              │                            │
              ▼                            ▼
    ┌─────────────────┐          ┌─────────────────┐
    │ Robert =        │          │ Cersei =        │
    │ Baratheon(...)  │          │ Lannister(...)  │
    │                 │          │                 │
    │ eyes: brown     │          │ eyes: blue      │
    │ hairs: dark     │          │ hairs: light    │
    └────────┬────────┘          └────────┬────────┘
             │                            │
             ▼                            │
    ┌─────────────────┐                   │
    │ Robert.die()    │                   │
    │ → is_alive=False│                   │
    └─────────────────┘                   │
                                          │
                                          ▼
                                ┌─────────────────┐
                                │ Jaime =         │
                                │ Lannister       │
                                │ .create_lannister│
                                │ ("Jaime", True) │
                                └────────┬────────┘
                                         │
                                         ▼
                                ┌─────────────────┐
                                │ Affichage final │
                                │ avec type()    │
                                └─────────────────┘
```

---

## 17. Récapitulatif des nouvelles notions

| Concept | Rôle dans l'exercice |
|---------|---------------------|
| Import module | `from S1E9 import Character` |
| Attributs enfant | `family_name`, `eyes`, `hairs` |
| `__str__` | Représentation lisible |
| `__repr__` | Représentation technique |
| `@classmethod` | Factory method |
| `cls` | Référence à la classe |
| `type().__name__` | Nom de la classe |
| f-strings | Formatage de chaînes |