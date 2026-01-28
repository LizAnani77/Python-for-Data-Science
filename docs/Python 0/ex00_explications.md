# Explications des notions de l'exercice 00

## Les 4 structures de données Python

---

### 1. La liste (`list`)

Une liste est une collection **ordonnée** et **modifiable** d'éléments. On la reconnaît aux crochets `[]`.

**Caractéristiques :**

- Tu peux accéder à un élément par son index (position), qui commence à 0
- Tu peux modifier directement un élément existant
- L'ordre des éléments est préservé

**Exemple :**

```python
ft_list = ["Hello", "tata!"]
ft_list[1] = "World!"  # Remplace l'élément à la position 1
```

C'est pourquoi `ft_list[1] = "World!"` fonctionne : on remplace simplement l'élément à la position 1.

---

### 2. Le tuple (`tuple`)

Un tuple est une collection **ordonnée** mais **immuable** (non modifiable). On le reconnaît aux parenthèses `()`.

**Caractéristiques :**

- Une fois créé, tu ne peux pas modifier ses éléments
- Pour "modifier" un tuple, tu dois en créer un nouveau
- Utile pour des données qui ne doivent pas changer

**Exemple :**

```python
ft_tuple = ("Hello", "toto!")
ft_tuple = (ft_tuple[0], "France!")  # Création d'un nouveau tuple
```

C'est pourquoi on recrée entièrement le tuple : on garde le premier élément avec `ft_tuple[0]` et on remplace le second dans un nouveau tuple.

---

### 3. L'ensemble (`set`)

Un set est une collection **non ordonnée** de valeurs **uniques**. On le reconnaît aux accolades `{}`.

**Caractéristiques :**

- Pas d'index (pas d'ordre garanti)
- Chaque élément ne peut apparaître qu'une seule fois
- On ajoute avec `.add()` et on retire avec `.discard()`

**Exemple :**

```python
ft_set = {"Hello", "tutu!"}
ft_set.discard("tutu!")  # Supprime "tutu!"
ft_set.add("Paris!")     # Ajoute "Paris!"
```

C'est pourquoi on utilise `discard()` puis `add()` : on ne peut pas remplacer directement, on supprime et on ajoute.

> **Note :** L'ordre d'affichage d'un set peut varier d'une exécution à l'autre.

---

### 4. Le dictionnaire (`dict`)

Un dictionnaire associe des **clés** à des **valeurs**. On le reconnaît aux accolades avec le format `{clé: valeur}`.

**Caractéristiques :**

- Accès par clé (pas par index numérique)
- Les clés doivent être uniques
- Les valeurs sont modifiables

**Exemple :**

```python
ft_dict = {"Hello": "titi!"}
ft_dict["Hello"] = "42Paris!"  # Modifie la valeur associée à la clé "Hello"
```

C'est pourquoi `ft_dict["Hello"] = "42Paris!"` fonctionne : on accède à la valeur via sa clé "Hello" et on la remplace.

---

## Résumé visuel

| Structure | Syntaxe | Ordonnée | Modifiable | Accès |
|-----------|---------|----------|------------|-------|
| Liste     |   `[]`  |    Oui   |     Oui    | Index |
| Tuple     |   `()`  |    Oui   |     Non    | Index |
| Set       |   `{}`  |    Non   |     Oui    | Aucun |
| Dict      | `{k:v}` |    Oui*  |     Oui    | Clé   |

*Depuis Python 3.7, les dictionnaires conservent l'ordre d'insertion.

---

## Méthodes utiles à retenir

### Pour les listes

- `list.append(x)` : ajoute un élément à la fin
- `list.insert(i, x)` : insère un élément à la position i
- `list.remove(x)` : supprime la première occurrence de x
- `list[i]` : accède à l'élément à la position i

### Pour les sets

- `set.add(x)` : ajoute un élément
- `set.discard(x)` : supprime un élément (sans erreur si absent)
- `set.remove(x)` : supprime un élément (erreur si absent)

### Pour les dictionnaires

- `dict[key] = value` : ajoute ou modifie une paire clé-valeur
- `dict.get(key)` : récupère une valeur (retourne None si absente)
- `dict.keys()` : retourne toutes les clés
- `dict.values()` : retourne toutes les valeurs

### Commandes
- `python Hello.py
- `python Hello.py | cat -e