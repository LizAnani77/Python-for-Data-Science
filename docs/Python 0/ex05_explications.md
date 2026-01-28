# Explications des notions de l'exercice 05

## 1. Le module `string`

Le module `string` contient des constantes utiles pour manipuler des chaînes.

| Constante | Contenu |
|-----------|---------|
| `string.punctuation` | `!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~` |
| `string.ascii_lowercase` | `abcdefghijklmnopqrstuvwxyz` |
| `string.ascii_uppercase` | `ABCDEFGHIJKLMNOPQRSTUVWXYZ` |
| `string.digits` | `0123456789` |

---

## 2. Les méthodes de chaînes pour tester les caractères

Python fournit des méthodes intégrées aux chaînes :

| Méthode | Vérifie si... |
|---------|---------------|
| `char.isupper()` | Le caractère est une majuscule |
| `char.islower()` | Le caractère est une minuscule |
| `char.isdigit()` | Le caractère est un chiffre |
| `char.isspace()` | Le caractère est un espace/tabulation/newline |

Ces méthodes renvoient `True` ou `False`.

---

## 3. L'opérateur `in`

`char in string.punctuation` vérifie si le caractère est **présent dans** la chaîne de ponctuation.

L'opérateur `in` fonctionne avec plusieurs types :

- Chaînes : `"a" in "abc"` → `True`
- Listes : `1 in [1, 2, 3]` → `True`
- Dictionnaires (teste les clés) : `"key" in {"key": "value"}` → `True`

---

## 4. Les dictionnaires comme compteurs

On utilise un dictionnaire pour stocker plusieurs compteurs nommés :

```python
counts = {
    'upper': 0,
    'lower': 0,
    ...
}
```

L'incrémentation se fait avec `+=` :

```python
counts['upper'] += 1  # équivaut à counts['upper'] = counts['upper'] + 1
```

---

## 5. Parcourir une chaîne avec `for`

```python
for char in text:
```

Une chaîne est **itérable** : on peut parcourir ses caractères un par un. Chaque tour de boucle, `char` prend la valeur du caractère suivant.

---

## 6. Les docstrings

```python
def count_characters(text: str) -> dict:
    """Compte les différents types de caractères dans une chaîne."""
```

La chaîne entre `"""` juste après la définition est une **docstring**. Elle documente la fonction et est accessible via `fonction.__doc__`.

C'est une exigence du sujet : toutes les fonctions doivent avoir une documentation.

---

## 7. Lecture de l'entrée standard avec `sys.stdin`

```python
text = sys.stdin.readline()
```

`sys.stdin.readline()` lit une ligne depuis l'entrée standard (le clavier par défaut).

**Différence avec `input()` :**

- `input()` retire automatiquement le `\n` final
- `readline()` conserve le `\n` (d'où le comptage du retour chariot comme espace)

---

## 8. Séparation en fonctions

Le code est divisé en plusieurs fonctions avec des rôles distincts :

| Fonction | Rôle |
|----------|------|
| `count_characters()` | Logique de comptage |
| `display_counts()` | Affichage des résultats |
| `main()` | Gestion des arguments et orchestration |

C'est une bonne pratique : chaque fonction fait **une seule chose**.