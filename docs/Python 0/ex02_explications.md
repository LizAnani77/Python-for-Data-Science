# Explications des notions de l'exercice 02

## 1. Définition d'une fonction

Une fonction est un bloc de code réutilisable. On la définit avec `def`, suivi du nom, des paramètres entre parenthèses, et de deux-points.

**Les type hints (annotations de type) :**

- `object: any` → le paramètre `object` peut être de n'importe quel type
- `-> int` → la fonction retourne un entier

Ces annotations sont **indicatives** (Python ne les impose pas), mais elles rendent le code plus lisible.

---

## 2. La fonction `type()`

`type()` est une fonction native qui renvoie le **type** d'un objet.

| Objet        | Résultat de `type()` |
|--------------|----------------------|
| `["a", "b"]` |   `<class 'list'>`   |
| `("a", "b")` |   `<class 'tuple'>`  |
| `{"a", "b"}` |   `<class 'set'>`    |
| `{"a": "b"}` |   `<class 'dict'>`   |
| `"texte"`    |   `<class 'str'>`    |
| `42`         |   `<class 'int'>`    |

---

## 3. Comparaison de types

On peut comparer directement le résultat de `type()` avec les noms de types Python : `list`, `tuple`, `set`, `dict`, `str`, `int`, etc.

Ces noms sont des **classes** intégrées à Python. L'opérateur `==` vérifie si le type correspond exactement.

---

## 4. Structure conditionnelle if/elif/else

- `if` → première condition testée
- `elif` → conditions alternatives (autant qu'on veut)
- `else` → si aucune condition précédente n'est vraie

Python exécute le premier bloc dont la condition est vraie, puis sort de la structure.

---

## 5. Le mot-clé `return`

`return` termine la fonction et renvoie une valeur à l'appelant. Ici, la fonction retourne toujours `42`, quelle que soit la branche conditionnelle empruntée.

---

## 6. Le pattern `if __name__ == "__main__":`

L'exercice exige que le script ne produise **aucune sortie** quand on l'exécute seul. C'est le rôle de ce pattern (même s'il n'est pas dans ton code actuel).

**Explication :**

- `__name__` est une variable spéciale
- Elle vaut `"__main__"` si le fichier est exécuté directement
- Elle vaut le nom du module si le fichier est importé

Cela permet de séparer le code de la fonction (toujours disponible) du code de test (exécuté seulement en mode direct).