# Explications des notions de l'exercice 02 : DiamondTrap

## 1. L'héritage multiple

En Python, une classe peut hériter de **plusieurs** classes parentes simultanément.

```python
class King(Baratheon, Lannister):
    pass
```

### Syntaxe

```python
class Enfant(Parent1, Parent2, Parent3):
    pass
```

### Comparaison héritage simple vs multiple

| Type | Syntaxe | Exemple |
|------|---------|---------|
| Simple | `class A(B)` | `Stark(Character)` |
| Multiple | `class A(B, C)` | `King(Baratheon, Lannister)` |

### Visualisation

```
Héritage simple:                 Héritage multiple:

    Character                   Baratheon   Lannister
        │                            │         │
        ▼                            └────┬────┘
      Stark                               │
                                          ▼
                                        King
```

---

## 2. Le problème du diamant (Diamond Problem)

Le **diamond problem** survient quand deux classes parentes héritent d'une même classe ancêtre.

### Pourquoi "diamant" ?

La forme de l'héritage ressemble à un diamant :

```
              Character
             ╱         ╲
            ╱           ╲
      Baratheon      Lannister
            ╲           ╱
             ╲         ╱
               King
```

### Le problème concret

Quand `King` appelle `super().__init__()` :

| Question | Problème potentiel |
|----------|-------------------|
| Quel `__init__` appeler ? | Baratheon ou Lannister ? |
| Combien de fois ? | `Character.__init__` appelé 2 fois ? |
| Dans quel ordre ? | Baratheon puis Lannister ? L'inverse ? |

### Sans solution

```
King.__init__()
      │
      ├──► Baratheon.__init__()
      │         │
      │         └──► Character.__init__()  ← 1ère fois
      │
      └──► Lannister.__init__()
                │
                └──► Character.__init__()  ← 2ème fois ❌
```

---

## 3. La solution : MRO et C3 Linearization

Python résout le diamond problem avec l'algorithme **C3 linearization** depuis Python 2.3.

### MRO (Method Resolution Order)

Le MRO définit l'**ordre unique** dans lequel Python cherche les méthodes.

```python
print(King.__mro__)
```

### Résultat

```
(
  <class 'King'>,
  <class 'Baratheon'>,
  <class 'Lannister'>,
  <class 'Character'>,
  <class 'ABC'>,
  <class 'object'>
)
```

### Visualisation linéaire

```
King → Baratheon → Lannister → Character → ABC → object
 │         │            │           │        │       │
 1         2            3           4        5       6
```

### Règles du C3

| Règle | Application |
|-------|-------------|
| Enfant avant parents | `King` en premier |
| Ordre de déclaration | `Baratheon` avant `Lannister` |
| Parent commun en dernier | `Character` après les deux enfants |
| Chaque classe une seule fois | `Character` n'apparaît qu'une fois |

---

## 4. Comment `super()` utilise le MRO

Avec le MRO, `super()` appelle la classe **suivante dans la chaîne**, pas forcément le parent direct.

### Flux d'exécution réel

```
King("Joffrey")
       │
       ▼
┌─────────────────────────────────────┐
│ King.__init__                       │
│   super().__init__("Joffrey")       │
│         │                           │
│         │  MRO: suivant = Baratheon │
│         ▼                           │
└─────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────┐
│ Baratheon.__init__                  │
│   super().__init__("Joffrey")       │
│         │                           │
│         │  MRO: suivant = Lannister │
│         ▼                           │
│   self.family_name = "Baratheon"    │
│   self.eyes = "brown"               │
│   self.hairs = "dark"               │
└─────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────┐
│ Lannister.__init__                  │
│   super().__init__("Joffrey")       │
│         │                           │
│         │  MRO: suivant = Character │
│         ▼                           │
│   self.family_name = "Lannister"    │  ← Écrase !
│   self.eyes = "blue"                │  ← Écrase !
│   self.hairs = "light"              │  ← Écrase !
└─────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────┐
│ Character.__init__                  │
│   self.first_name = "Joffrey"       │
│   self.is_alive = True              │
└─────────────────────────────────────┘
```

### Ordre d'exécution des attributs

| Ordre | Classe | Attributs définis |
|-------|--------|-------------------|
| 1 | `Character` | `first_name`, `is_alive` |
| 2 | `Lannister` | `family_name`, `eyes`, `hairs` |
| 3 | `Baratheon` | `family_name`, `eyes`, `hairs` (écrase) |

### Résultat final

```python
Joffrey.__dict__
# {
#   'first_name': 'Joffrey',
#   'is_alive': True,
#   'family_name': 'Baratheon',  ← Baratheon gagne (dernier)
#   'eyes': 'brown',             ← Baratheon gagne
#   'hairs': 'dark'              ← Baratheon gagne
# }
```

---

## 5. Les getters

Un **getter** est une méthode qui **retourne** la valeur d'un attribut.

```python
def get_eyes(self):
    """Retourne la couleur des yeux."""
    return self.eyes

def get_hairs(self):
    """Retourne la couleur des cheveux."""
    return self.hairs
```

### Utilisation

```python
Joffrey = King("Joffrey")
print(Joffrey.get_eyes())   # "brown"
print(Joffrey.get_hairs())  # "dark"
```

### Convention de nommage

| Pattern | Exemple |
|---------|---------|
| `get_attribut()` | `get_eyes()` |
| `get_nom_attribut()` | `get_first_name()` |

---

## 6. Les setters

Un **setter** est une méthode qui **modifie** la valeur d'un attribut.

```python
def set_eyes(self, color: str):
    """Définit la couleur des yeux."""
    self.eyes = color

def set_hairs(self, color: str):
    """Définit la couleur des cheveux."""
    self.hairs = color
```

### Utilisation

```python
Joffrey = King("Joffrey")
print(Joffrey.eyes)         # "brown"

Joffrey.set_eyes("blue")
print(Joffrey.eyes)         # "blue"
```

### Convention de nommage

| Pattern | Exemple |
|---------|---------|
| `set_attribut(valeur)` | `set_eyes("blue")` |

---

## 7. Getters/Setters vs accès direct

### Comparaison

```python
# Accès direct
Joffrey.eyes = "blue"
print(Joffrey.eyes)

# Via getters/setters
Joffrey.set_eyes("blue")
print(Joffrey.get_eyes())
```

### Pourquoi utiliser des getters/setters ?

| Avantage | Exemple |
|----------|---------|
| Validation | Vérifier que la couleur est valide |
| Encapsulation | Cacher l'implémentation |
| Logging | Tracer les modifications |
| Calcul | Retourner une valeur calculée |

### Exemple avec validation

```python
def set_eyes(self, color: str):
    """Définit la couleur des yeux avec validation."""
    valid = ["blue", "brown", "green", "grey"]
    if color.lower() in valid:
        self.eyes = color
    else:
        raise ValueError(f"Couleur invalide: {color}")
```

---

## 8. Le décorateur `@property` (alternative)

Python propose une alternative plus élégante aux getters/setters classiques.

### Syntaxe

```python
class King(Baratheon, Lannister):
    
    @property
    def eyes(self):
        return self._eyes
    
    @eyes.setter
    def eyes(self, value):
        self._eyes = value
```

### Utilisation

```python
Joffrey.eyes = "blue"    # Appelle le setter
print(Joffrey.eyes)      # Appelle le getter
```

### Note

L'exercice demande des getters/setters classiques (`get_eyes`, `set_eyes`), pas `@property`.

---

## 9. Le contexte Game of Thrones

### Joffrey Baratheon

Joffrey est officiellement un Baratheon mais biologiquement un Lannister.

```
Officiellement:              Réalité:

Robert ──┬── Cersei         Jaime ──┬── Cersei
         │                          │
      Joffrey                    Joffrey
    (Baratheon)                (Lannister)
```

### L'incohérence physique

| Caractéristique | Baratheon | Lannister | Joffrey (réel) |
|-----------------|-----------|-----------|----------------|
| Yeux | Marron | Bleus | Bleus |
| Cheveux | Foncés | Clairs | Clairs |

### Le code reflète cette dualité

```python
Joffrey = King("Joffrey")
# Hérite des traits Baratheon par défaut

Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
# Corrigé vers ses vrais traits Lannister
```

---

## 10. Structure du fichier DiamondTrap.py

```
DiamondTrap.py
│
├── Import
│   └── from S1E7 import Baratheon, Lannister
│
└── Classe King (Baratheon, Lannister)
    │
    ├── Docstring
    │
    ├── __init__(first_name, is_alive=True)
    │   └── super().__init__(...)
    │
    ├── Setters
    │   ├── set_eyes(color)
    │   └── set_hairs(color)
    │
    └── Getters
        ├── get_eyes()
        └── get_hairs()
```

---

## 11. Le fichier tester.py

### Code du testeur

```python
from DiamondTrap import King

Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)
```

### Sortie attendue

```
$> python tester.py
{'first_name': 'Joffrey', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'brown', 'hairs': 'dark'}
blue
light
{'first_name': 'Joffrey', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'blue', 'hairs': 'light'}
$>
```

---

## 12. Analyse de la sortie

### Premier `__dict__` (après création)

```python
{
    'first_name': 'Joffrey',      # Character
    'is_alive': True,             # Character
    'family_name': 'Baratheon',   # Baratheon (via MRO)
    'eyes': 'brown',              # Baratheon
    'hairs': 'dark'               # Baratheon
}
```

### Après les setters

```python
Joffrey.set_eyes("blue")   # eyes: "brown" → "blue"
Joffrey.set_hairs("light") # hairs: "dark" → "light"
```

### Second `__dict__` (après modification)

```python
{
    'first_name': 'Joffrey',
    'is_alive': True,
    'family_name': 'Baratheon',   # Inchangé
    'eyes': 'blue',               # Modifié ✓
    'hairs': 'light'              # Modifié ✓
}
```

---

## 13. Vérifier le MRO

### Méthode 1 : `__mro__`

```python
print(King.__mro__)
```

### Méthode 2 : `mro()`

```python
print(King.mro())
```

### Résultat

```
[
    <class 'DiamondTrap.King'>,
    <class 'S1E7.Baratheon'>,
    <class 'S1E7.Lannister'>,
    <class 'S1E9.Character'>,
    <class 'abc.ABC'>,
    <class 'object'>
]
```

### Interprétation

| Position | Classe | Rôle |
|----------|--------|------|
| 1 | `King` | Classe actuelle |
| 2 | `Baratheon` | Premier parent |
| 3 | `Lannister` | Second parent |
| 4 | `Character` | Grand-parent commun |
| 5 | `ABC` | Base abstraite |
| 6 | `object` | Racine de tout |

---

## 14. Flux d'exécution complet

```
                 python tester.py
                        │
                        ▼
           ┌────────────────────────┐
           │ from DiamondTrap       │
           │   import King          │
           └───────────┬────────────┘
                       │
                       ▼
           ┌────────────────────────┐
           │ Joffrey = King(...)    │
           │                        │
           │ MRO résout l'héritage: │
           │ King → Baratheon →     │
           │ Lannister → Character  │
           └───────────┬────────────┘
                       │
                       ▼
           ┌────────────────────────┐
           │ print(__dict__)        │
           │ eyes: brown            │
           │ hairs: dark            │
           └───────────┬────────────┘
                       │
                       ▼
           ┌────────────────────────┐
           │ set_eyes("blue")       │
           │ set_hairs("light")     │
           └───────────┬────────────┘
                       │
                       ▼
           ┌────────────────────────┐
           │ print(__dict__)        │
           │ eyes: blue             │
           │ hairs: light           │
           └────────────────────────┘
```

---

## 15. Récapitulatif des nouvelles notions

| Concept | Description |
|---------|-------------|
| Héritage multiple | `class King(Baratheon, Lannister)` |
| Diamond problem | Ancêtre commun partagé |
| MRO | Ordre de résolution des méthodes |
| C3 linearization | Algorithme de résolution |
| Getter | Méthode pour lire un attribut |
| Setter | Méthode pour modifier un attribut |
| `__mro__` | Attribut pour voir l'ordre |