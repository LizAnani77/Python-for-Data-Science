# Explications des notions de l'exercice 06

## Partie 1 : ft_filter.py

### 1. La fonction native `filter()`

`filter()` est une fonction intégrée à Python qui filtre les éléments d'un itérable selon une condition.

```python
filter(fonction, iterable)
```

Elle garde uniquement les éléments pour lesquels `fonction(element)` renvoie `True`.

---

### 2. Les expressions génératrices

```python
(item for item in iterable if condition)
```

C'est comme une list comprehension, mais avec des **parenthèses** au lieu de crochets.

**Différence clé :**

| Syntaxe | Type | Comportement |
|---------|------|--------------|
| `[x for x in lst]` | `list` | Crée toute la liste en mémoire |
| `(x for x in lst)` | `generator` | Génère les éléments à la demande |

Le générateur est plus économe en mémoire (important pour de grandes données).

---

### 3. Le cas `function is None`

Quand `filter()` reçoit `None` comme fonction, elle filtre les éléments "truthy" (qui sont vrais en contexte booléen).

Valeurs "falsy" en Python : `None`, `0`, `""`, `[]`, `{}`, `False`

---

## Partie 2 : filterstring.py

### 4. Les fonctions `lambda`

Une **lambda** est une fonction anonyme (sans nom) sur une seule ligne.

```python
lambda paramètres: expression
```

Équivalences :

```python
# Lambda
lambda word: len(word) > n

# Fonction classique équivalente
def ma_fonction(word):
    return len(word) > n
```

Les lambdas sont pratiques pour des fonctions courtes qu'on utilise une seule fois.

---

### 5. La méthode `split()`

```python
"Hello the World".split()
```

`split()` découpe une chaîne en liste de mots. Par défaut, elle sépare sur les espaces.

| Appel | Résultat |
|-------|----------|
| `"Hello the World".split()` | `['Hello', 'the', 'World']` |
| `"a,b,c".split(",")` | `['a', 'b', 'c']` |

---

### 6. La fonction `isinstance()`

```python
isinstance(text, str)
```

Vérifie si un objet est d'un type donné. Plus souple que `type() ==` car elle gère l'héritage.

---

### 7. Capture multiple d'exceptions

```python
except (AssertionError, ValueError):
```

Les parenthèses permettent de capturer **plusieurs types** d'exceptions avec le même bloc de traitement.

---

### 8. Conversion en liste avec `list()`

```python
result = list(ft_filter(...))
```

`ft_filter()` renvoie un générateur. Pour l'afficher comme une liste `['Hello', 'World']`, on le convertit avec `list()`.

---

### 9. Flux de l'exercice

```
"Hello the World", 4
        ↓
    split()
        ↓
['Hello', 'the', 'World']
        ↓
ft_filter(lambda word: len(word) > 4, ...)
        ↓
['Hello', 'World']  (seuls les mots de plus de 4 lettres)
```