# Explications des notions de l'exercice 00 : GOT S1E9

## 1. La Programmation Orientée Objet (POO)

La **POO** est un paradigme de programmation qui organise le code autour d'**objets** plutôt que de fonctions.

### Concepts fondamentaux

| Concept | Description | Exemple GOT |
|---------|-------------|-------------|
| **Classe** | Modèle/plan pour créer des objets | `Stark` est le modèle |
| **Objet** | Instance concrète d'une classe | `Ned` est un objet Stark |
| **Attribut** | Variable appartenant à un objet | `first_name`, `is_alive` |
| **Méthode** | Fonction appartenant à une classe | `die()` |

### Analogie

```
Classe = Moule à gâteau
Objet  = Gâteau fabriqué avec ce moule

        ┌─────────────────┐
        │  Classe Stark   │  ← Le moule
        │  - first_name   │
        │  - is_alive     │
        │  - die()        │
        └────────┬────────┘
                 │
        ┌────────┴────────┐
        │    Instances    │
        ▼        ▼        ▼
      Ned     Arya     Lyanna   ← Les gâteaux
```

---

## 2. Le module `abc` (Abstract Base Classes)

Le module `abc` fournit les outils pour créer des **classes abstraites** en Python.

```python
from abc import ABC, abstractmethod
```

### Éléments importés

| Import | Description |
|--------|-------------|
| `ABC` | Classe de base pour créer une classe abstraite |
| `abstractmethod` | Décorateur pour marquer une méthode comme abstraite |

### Pourquoi une classe abstraite ?

Une classe abstraite est une classe qu'on **ne peut pas instancier directement**. Elle sert uniquement de modèle pour d'autres classes.

```
Sans classe abstraite:           Avec classe abstraite:
                                 
Character("hodor") ✅            Character("hodor") ❌ TypeError!
Stark("Ned") ✅                  Stark("Ned") ✅
```

---

## 3. Créer une classe abstraite

Pour créer une classe abstraite, on hérite de `ABC` :

```python
class Character(ABC):
    """Classe abstraite."""
    pass
```

### Visualisation de l'héritage

```
        ┌─────────────┐
        │     ABC     │  ← Classe de base Python
        └──────┬──────┘
               │ hérite
               ▼
        ┌─────────────┐
        │  Character  │  ← Notre classe abstraite
        └──────┬──────┘
               │ hérite
               ▼
        ┌─────────────┐
        │    Stark    │  ← Classe concrète (instanciable)
        └─────────────┘
```

### Test d'instanciation

```python
from S1E9 import Character

hodor = Character("hodor")
```

### Erreur attendue

```
TypeError: Can't instantiate abstract class Character with abstract method __init__
```

---

## 4. Le décorateur `@abstractmethod`

Un **décorateur** modifie le comportement d'une fonction ou méthode. `@abstractmethod` marque une méthode comme "obligatoire à implémenter".

```python
@abstractmethod
def __init__(self, first_name: str, is_alive: bool = True):
    self.first_name = first_name
    self.is_alive = is_alive
```

### Effet du décorateur

| Sans `@abstractmethod` | Avec `@abstractmethod` |
|------------------------|------------------------|
| Méthode normale | Méthode obligatoire |
| Classe instanciable | Classe non instanciable |

### Règles

| Règle | Description |
|-------|-------------|
| Position | Juste au-dessus de la méthode |
| Obligation | Toute sous-classe doit redéfinir cette méthode |
| Contenu | Peut contenir du code (sera hérité) |

---

## 5. L'héritage

L'**héritage** permet à une classe de récupérer les attributs et méthodes d'une autre classe.

```python
class Stark(Character):
    pass
```

### Vocabulaire

| Terme | Synonymes | Dans l'exercice |
|-------|-----------|-----------------|
| Classe parent | Base, Super, Mère | `Character` |
| Classe enfant | Dérivée, Sous-classe, Fille | `Stark` |

### Ce que Stark hérite de Character

```
Character                    Stark
┌──────────────────┐         ┌──────────────────┐
│ first_name       │────────►│ first_name       │ ✅ Hérité
│ is_alive         │────────►│ is_alive         │ ✅ Hérité
│ die()            │────────►│ die()            │ ✅ Hérité
│ __init__() ⚠️    │────────►│ __init__()       │ ⚠️ Doit redéfinir
└──────────────────┘         └──────────────────┘
```

---

## 6. Le mot-clé `self`

`self` représente l'**instance actuelle** de la classe. C'est toujours le premier paramètre des méthodes.

```python
def __init__(self, first_name):
    self.first_name = first_name
```

### Visualisation

```
Ned = Stark("Ned")           Arya = Stark("Arya")
         │                            │
         ▼                            ▼
┌─────────────────┐          ┌─────────────────┐
│ self = Ned      │          │ self = Arya     │
│                 │          │                 │
│ self.first_name │          │ self.first_name │
│    = "Ned"      │          │    = "Arya"     │
└─────────────────┘          └─────────────────┘
```

### Règles de `self`

| Règle | Exemple |
|-------|---------|
| Premier paramètre de toute méthode | `def die(self):` |
| Accès aux attributs | `self.is_alive` |
| Non passé lors de l'appel | `Ned.die()` pas `Ned.die(Ned)` |

---

## 7. Le constructeur `__init__`

`__init__` est une **méthode spéciale** appelée automatiquement lors de la création d'un objet.

```python
def __init__(self, first_name: str, is_alive: bool = True):
    self.first_name = first_name
    self.is_alive = is_alive
```

### Flux de création

```
Ned = Stark("Ned")
        │
        ▼
┌───────────────────────────────┐
│ 1. Python crée un objet vide  │
│    ┌─────────┐                │
│    │  Stark  │                │
│    │ (vide)  │                │
│    └─────────┘                │
└───────────────────────────────┘
        │
        ▼
┌───────────────────────────────┐
│ 2. Appel de __init__          │
│    self = objet vide          │
│    first_name = "Ned"         │
│    is_alive = True (défaut)   │
└───────────────────────────────┘
        │
        ▼
┌───────────────────────────────┐
│ 3. Objet rempli et retourné   │
│    ┌───────────────────┐      │
│    │ first_name = "Ned"│      │
│    │ is_alive = True   │      │
│    └───────────────────┘      │
└───────────────────────────────┘
```

### Les méthodes spéciales (dunder methods)

| Méthode | Appelée quand |
|---------|---------------|
| `__init__` | Création de l'objet |
| `__str__` | `print(objet)` |
| `__repr__` | `repr(objet)` |
| `__dict__` | Accès aux attributs |
| `__doc__` | Accès à la documentation |

---

## 8. La fonction `super()`

`super()` permet d'appeler une méthode de la classe **parent**.

```python
class Stark(Character):
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
```

### Flux d'exécution

```
Stark("Ned")
     │
     ▼
┌─────────────────────────────────┐
│ Stark.__init__(self, "Ned")     │
│                                 │
│   super().__init__("Ned", True) │───┐
└─────────────────────────────────┘   │
                                      │
     ┌────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────┐
│ Character.__init__(self, ...)   │
│                                 │
│   self.first_name = "Ned"       │
│   self.is_alive = True          │
└─────────────────────────────────┘
```

### Pourquoi utiliser `super()` ?

| Sans `super()` | Avec `super()` |
|----------------|----------------|
| Code dupliqué | Code réutilisé |
| Erreurs possibles | Cohérence garantie |
| Maintenance difficile | Maintenance facile |

---

## 9. Les paramètres par défaut

Un paramètre par défaut prend une valeur automatique si non spécifié.

```python
def __init__(self, first_name: str, is_alive: bool = True):
```

### Analyse

| Paramètre | Obligatoire | Valeur par défaut |
|-----------|-------------|-------------------|
| `first_name` | ✅ Oui | Aucune |
| `is_alive` | ❌ Non | `True` |

### Exemples d'appels

```python
Stark("Ned")              # is_alive = True (défaut)
Stark("Ned", True)        # is_alive = True (explicite)
Stark("Lyanna", False)    # is_alive = False
```

### Règle importante

```
Paramètres avec défaut APRÈS ceux sans défaut

✅ def __init__(self, first_name, is_alive=True):
❌ def __init__(self, is_alive=True, first_name):  # SyntaxError!
```

---

## 10. Les annotations de type (Type Hints)

Les annotations indiquent le type attendu des paramètres.

```python
def __init__(self, first_name: str, is_alive: bool = True):
```

### Syntaxe

| Élément | Syntaxe |
|---------|---------|
| Paramètre | `param: type` |
| Retour | `-> type` |
| Avec défaut | `param: type = valeur` |

### Types courants

| Type | Description | Exemple |
|------|-------------|---------|
| `str` | Chaîne | `"Ned"` |
| `int` | Entier | `42` |
| `bool` | Booléen | `True` |
| `float` | Décimal | `3.14` |
| `None` | Absence | `None` |

### Note importante

```
Les annotations sont INFORMATIVES uniquement.
Python ne vérifie PAS les types à l'exécution.
```

---

## 11. La méthode `die()`

La méthode `die()` change l'état du personnage.

```python
def die(self):
    self.is_alive = False
```

### Caractéristiques

| Aspect | Valeur |
|--------|--------|
| Paramètres | Aucun (seulement `self`) |
| Retour | `None` (implicite) |
| Effet | Modifie `self.is_alive` |

### Visualisation

```
Avant Ned.die():              Après Ned.die():

┌──────────────────┐          ┌──────────────────┐
│ Ned              │          │ Ned              │
│ ──────────────── │          │ ──────────────── │
│ first_name: "Ned"│          │ first_name: "Ned"│
│ is_alive: True   │ ───────► │ is_alive: False  │
└──────────────────┘          └──────────────────┘
```

---

## 12. L'attribut `__dict__`

`__dict__` est un dictionnaire contenant tous les **attributs d'instance**.

```python
Ned = Stark("Ned")
print(Ned.__dict__)
```

### Sortie

```python
{'first_name': 'Ned', 'is_alive': True}
```

### Contenu

| Inclus | Non inclus |
|--------|------------|
| Attributs d'instance | Méthodes |
| Valeurs actuelles | Attributs de classe |

---

## 13. L'attribut `__doc__` (Docstrings)

Les **docstrings** documentent le code et sont accessibles via `__doc__`.

```python
class Stark(Character):
    """Classe représentant un membre de la famille Stark."""
    
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructeur de la classe Stark."""
        super().__init__(first_name, is_alive)
    
    def die(self):
        """Change l'état de santé du personnage à False."""
        self.is_alive = False
```

### Accès aux docstrings

| Expression | Retourne |
|------------|----------|
| `Ned.__doc__` | Docstring de la classe |
| `Ned.__init__.__doc__` | Docstring du constructeur |
| `Ned.die.__doc__` | Docstring de la méthode |

### Règles

| Règle | Description |
|-------|-------------|
| Syntaxe | Triple guillemets `"""..."""` |
| Position | Juste après la définition |
| Obligatoire | Oui dans ce projet |

---

## 14. Structure du fichier S1E9.py

```
S1E9.py
│
├── Import
│   └── from abc import ABC, abstractmethod
│
├── Classe Character (ABC)
│   ├── Docstring
│   ├── @abstractmethod __init__
│   │   ├── first_name: str
│   │   └── is_alive: bool = True
│   └── die()
│
└── Classe Stark (Character)
    ├── Docstring
    └── __init__
        └── super().__init__(...)
```

---

## 15. Le fichier tester.py

### Code du testeur

```python
from S1E9 import Character, Stark

Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)
```

### Sortie attendue

```
$> python tester.py
{'first_name': 'Ned', 'is_alive': True}
True
False
Your docstring for Class
Your docstring for Constructor
Your docstring for Method
---
{'first_name': 'Lyanna', 'is_alive': False}
$>
```

### Analyse ligne par ligne

| Ligne | Code | Résultat |
|-------|------|----------|
| 1 | `Ned.__dict__` | Dictionnaire des attributs |
| 2 | `Ned.is_alive` | `True` |
| 3 | `Ned.die()` | (modifie is_alive) |
| 4 | `Ned.is_alive` | `False` |
| 5-7 | `__doc__` | Docstrings |
| 8 | `print("---")` | Séparateur |
| 9 | `Lyanna.__dict__` | `is_alive` déjà `False` |

---

## 16. Flux d'exécution complet

```
                    python tester.py
                           │
                           ▼
              ┌────────────────────────┐
              │ from S1E9 import ...   │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ Ned = Stark("Ned")     │
              │                        │
              │ → Stark.__init__()     │
              │ → super().__init__()   │
              │ → Character.__init__() │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ print(Ned.__dict__)    │
              │ {'first_name': 'Ned',  │
              │  'is_alive': True}     │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ Ned.die()              │
              │ → is_alive = False     │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ Lyanna = Stark(        │
              │   "Lyanna", False)     │
              │ → is_alive déjà False  │
              └────────────────────────┘
```

---

## 17. Récapitulatif des concepts

| Concept | Rôle dans l'exercice |
|---------|---------------------|
| `ABC` | Rendre `Character` abstraite |
| `@abstractmethod` | Forcer redéfinition de `__init__` |
| Héritage | `Stark` hérite de `Character` |
| `self` | Référence à l'instance |
| `__init__` | Initialisation des attributs |
| `super()` | Appel du constructeur parent |
| Paramètres défaut | `is_alive=True` |
| Type hints | `first_name: str` |
| Docstrings | Documentation obligatoire |
| `__dict__` | Visualiser les attributs |
| `__doc__` | Accéder aux docstrings |