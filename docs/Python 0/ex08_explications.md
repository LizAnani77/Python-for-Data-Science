# Explications des notions de l'exercice 08

## 1. Le mot-clé `yield` et les générateurs

`yield` transforme une fonction en **générateur**. Au lieu de retourner une valeur unique et terminer, la fonction "met en pause" et peut reprendre.

```python
def mon_generateur():
    yield 1
    yield 2
    yield 3

for x in mon_generateur():
    print(x)  # Affiche 1, puis 2, puis 3
```

**Différence `return` vs `yield` :**

| `return` | `yield` |
|----------|---------|
| Termine la fonction | Met en pause la fonction |
| Renvoie une seule valeur | Peut renvoyer plusieurs valeurs |
| Exécution unique | Exécution à la demande |

---

## 2. La fonction `enumerate()`

```python
for i, item in enumerate(lst, 1):
```

`enumerate()` ajoute un compteur à un itérable. Le second argument (`1`) est la valeur de départ.

| Code | `i` | `item` |
|------|-----|--------|
| `enumerate(['a', 'b'], 1)` | 1, 2 | 'a', 'b' |
| `enumerate(['a', 'b'], 0)` | 0, 1 | 'a', 'b' |

---

## 3. La fonction `os.get_terminal_size()`

```python
terminal_width = os.get_terminal_size().columns
```

Récupère les dimensions du terminal. `.columns` donne la largeur en caractères.

Le `try/except OSError` gère le cas où il n'y a pas de terminal (ex: redirection vers un fichier).

---

## 4. Le retour chariot `\r`

```python
print(f"\r{...}", end="")
```

`\r` (carriage return) ramène le curseur **au début de la ligne** sans passer à la ligne suivante. Cela permet de **réécrire** la même ligne.

**Différence :**

| Caractère | Effet |
|-----------|-------|
| `\n` | Nouvelle ligne |
| `\r` | Retour au début de la ligne |

---

## 5. Les paramètres de `print()`

```python
print(..., end="", flush=True)
```

| Paramètre | Effet |
|-----------|-------|
| `end=""` | Ne pas ajouter de saut de ligne à la fin |
| `flush=True` | Force l'affichage immédiat (vide le buffer) |

Sans `flush=True`, l'affichage pourrait être retardé.

---

## 6. Formatage avec largeur fixe

```python
f"{int(percent * 100):3d}"
```

`:3d` formate un entier sur **3 caractères minimum**, aligné à droite.

| Valeur | Résultat |
|--------|----------|
| `5` | `"  5"` |
| `50` | `" 50"` |
| `100` | `"100"` |

---

## 7. Construction de la barre de progression

```python
bar = "=" * (filled_len - 1) + ">" + " " * (bar_width - filled_len)
```

**Opérateur `*` avec les chaînes :** répète la chaîne.

| Expression | Résultat |
|------------|----------|
| `"=" * 3` | `"==="` |
| `" " * 5` | `"     "` |

**Construction visuelle :**

```
[====>     ]
 ^^^^  ^^^^
 rempli  vide
```

---

## 8. Flux de l'exercice

```
for elem in ft_tqdm(range(333)):
    sleep(0.005)
        ↓
Itération 1:   "  1%|[>                    ]| 1/333"
Itération 50:  " 15%|[===>                 ]| 50/333"
Itération 333: "100%|[===================>]| 333/333"
        ↓
    yield item (renvoie l'élément au for externe)
```