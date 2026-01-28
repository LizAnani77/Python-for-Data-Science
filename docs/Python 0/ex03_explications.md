# Explications des notions de l'exercice 03

## 1. Les valeurs "Null" en Python

Python n'a pas un seul "null" comme d'autres langages. Il existe plusieurs valeurs considérées comme "vides" ou "fausses" :

| Valeur | Type | Description |
|--------|------|-------------|
| `None` | `NoneType` | Absence de valeur |
| `float("NaN")` | `float` | "Not a Number" (résultat indéfini) |
| `0` | `int` | Zéro entier |
| `""` | `str` | Chaîne vide |
| `False` | `bool` | Booléen faux |

---

## 2. L'opérateur `is` vs `==`

- `==` compare les **valeurs** (est-ce que ça vaut la même chose ?)
- `is` compare les **identités** (est-ce le même objet en mémoire ?)

**Pour `None` et `False`, on utilise `is` :**

- `object is None` → recommandé
- `object == None` → fonctionne mais déconseillé

`None` et `False` sont des **singletons** : il n'en existe qu'une seule instance en mémoire.

---

## 3. Le module `math` et `isnan()`

`NaN` (Not a Number) est une valeur spéciale des floats représentant un résultat mathématique indéfini (ex: `0/0`).

**Particularité de NaN :**

- `float("NaN") == float("NaN")` renvoie `False` !
- NaN n'est égal à rien, même pas à lui-même

C'est pourquoi on utilise `math.isnan()` pour le détecter de manière fiable.

---

## 4. Conditions multiples avec `and`

L'opérateur `and` permet de combiner plusieurs conditions. Les deux doivent être vraies :

```python
obj_type == float and math.isnan(object)
```

On vérifie d'abord que c'est un float (sinon `isnan()` pourrait échouer), puis qu'il est NaN.

---

## 5. Ordre des conditions

L'ordre des `if/elif` est important ici. `False` et `0` sont liés en Python :

- `bool` hérite de `int`
- `False == 0` est `True`
- `True == 1` est `True`

On doit donc vérifier le type exact avec `obj_type == bool` ou `obj_type == int` pour les distinguer.

---

## 6. Valeurs de retour comme code d'erreur

Convention classique en programmation :

- `return 0` → succès (tout s'est bien passé)
- `return 1` → erreur (type non reconnu)

Cette convention vient du monde Unix/C.