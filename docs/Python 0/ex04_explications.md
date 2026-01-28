# Explications des notions de l'exercice 04

## 1. Le module `sys` et `sys.argv`

`sys.argv` est une liste contenant les arguments passés au script en ligne de commande.

**Structure de `sys.argv` :**

| Index | Contenu |
|-------|---------|
| `argv[0]` | Nom du script |
| `argv[1]` | Premier argument |
| `argv[2]` | Deuxième argument |
| ... | ... |

Exemple : `python whatis.py 14` donne `sys.argv = ["whatis.py", "14"]`

---

## 2. Le slicing `[1:]`

`sys.argv[1:]` récupère tous les éléments **à partir de l'index 1** (donc sans le nom du script).

**Syntaxe du slicing :** `liste[début:fin]`

- `[1:]` → de l'index 1 jusqu'à la fin
- `[:3]` → du début jusqu'à l'index 3 (exclu)
- `[1:3]` → de l'index 1 à 3 (exclu)

---

## 3. Le bloc `try/except`

Permet de **capturer les erreurs** sans que le programme ne plante.

```python
try:
    # Code qui peut échouer
except TypeErreur:
    # Code exécuté si cette erreur survient
```

On peut avoir plusieurs `except` pour gérer différents types d'erreurs.

---

## 4. L'instruction `assert`

`assert` vérifie qu'une condition est vraie. Si elle est fausse, elle lève une `AssertionError`.

```python
assert len(args) == 1, "more than one argument is provided"
```

Équivaut à :

```python
if not (len(args) == 1):
    raise AssertionError("more than one argument is provided")
```

Le message après la virgule est optionnel mais recommandé.

---

## 5. Conversion de type et `ValueError`

`int(args[0])` tente de convertir une chaîne en entier.

- `int("14")` → `14` ✓
- `int("-5")` → `-5` ✓
- `int("Hi!")` → lève `ValueError` ✗

---

## 6. L'opérateur modulo `%`

`%` renvoie le **reste** de la division entière.

| Expression | Résultat | Explication                 |
|------------|----------|-----------------------------|
| `14 % 2`   |   `0`    | 14 ÷ 2 = 7, reste 0 → pair  |
| `5 % 2`    |   `1`    | 5 ÷ 2 = 2, reste 1 → impair |
| `0 % 2`    |   `0`    | 0 ÷ 2 = 0, reste 0 → pair   |

**Règle :** Si `n % 2 == 0`, le nombre est pair.

---

## 7. Le pattern `if __name__ == "__main__":`

Ce bloc ne s'exécute **que si le fichier est lancé directement** (pas importé).

- `python whatis.py 14` → `__name__` vaut `"__main__"` → `main()` s'exécute
- `from whatis import main` → `__name__` vaut `"whatis"` → `main()` ne s'exécute pas