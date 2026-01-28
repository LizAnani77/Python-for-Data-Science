# Explications des notions de l'exercice 07

## 1. Les dictionnaires comme table de correspondance

Un dictionnaire permet d'associer une **clé** à une **valeur**. Ici, chaque caractère est associé à son équivalent Morse.

```python
NESTED_MORSE = {
    "A": ".-",
    "B": "-...",
    ...
}
```

L'accès est direct et rapide : `NESTED_MORSE["A"]` renvoie `".-"`.

---

## 2. Convention de nommage : MAJUSCULES

```python
NESTED_MORSE = {...}
```

En Python, les noms en **MAJUSCULES** indiquent une **constante** (une valeur qui ne doit pas changer). C'est une convention, Python ne l'empêche pas techniquement.

---

## 3. La méthode `upper()`

```python
text.upper()
```

Convertit toute la chaîne en majuscules. Cela permet de gérer les entrées en minuscules puisque le dictionnaire ne contient que des majuscules.

| Entrée | Résultat |
|--------|----------|
| `"sos"` | `"SOS"` |
| `"Hello"` | `"HELLO"` |

---

## 4. Vérifier l'existence d'une clé avec `in`

```python
if char in NESTED_MORSE:
```

L'opérateur `in` avec un dictionnaire vérifie si la **clé** existe (pas la valeur).

---

## 5. La méthode `append()`

```python
result.append(NESTED_MORSE[char])
```

`append()` ajoute un élément **à la fin** d'une liste. On construit ainsi la liste des codes Morse caractère par caractère.

---

## 6. La méthode `join()`

```python
" ".join(result)
```

`join()` assemble les éléments d'une liste en une seule chaîne, avec un séparateur.

| Code | Résultat |
|------|----------|
| `" ".join(["...", "---", "..."])` | `"... --- ..."` |
| `"-".join(["a", "b", "c"])` | `"a-b-c"` |
| `"".join(["a", "b", "c"])` | `"abc"` |

**Attention :** Le séparateur est **avant** le `.join()`, pas dedans.

---

## 7. Lever une exception avec `raise`

```python
raise ValueError("Invalid character")
```

`raise` permet de **déclencher** une exception volontairement. Le programme s'arrête (ou l'exception est capturée par un `try/except`).

---

## 8. Flux de l'exercice

```
"sos"
   ↓
upper() → "SOS"
   ↓
Pour chaque caractère:
  "S" → NESTED_MORSE["S"] → "..."
  "O" → NESTED_MORSE["O"] → "---"
  "S" → NESTED_MORSE["S"] → "..."
   ↓
result = ["...", "---", "..."]
   ↓
" ".join(result) → "... --- ..."
```