# Explications des notions de l'exercice 02

## 1. Objectif de l'exercice

Comparer la population de **deux pays** sur un même graphique, avec :
- Deux courbes distinctes
- Une légende identifiant chaque pays
- Un formatage personnalisé de l'axe Y (20M, 40M, etc.)
- Filtrage des années (1800 à 2050)

---

## 2. Le fichier population_total.csv

Ce fichier contient des données de population avec des **suffixes** pour les grands nombres.

```csv
country,1800,1801,...,2050
France,29.4M,29.5M,...,67.3M
Belgium,3.25M,3.27M,...,11.8M
```

| Suffixe | Signification | Multiplicateur |
|---------|---------------|----------------|
| `k` | Kilo (milliers) | × 1 000 |
| `M` | Million | × 1 000 000 |
| `B` | Billion (milliards) | × 1 000 000 000 |

**Problème :** Ces valeurs sont des **chaînes de caractères**, pas des nombres. Il faut les convertir !

---

## 3. Fonction de conversion des populations

```python
def convert_population(value):
    """Convertit les valeurs de population (ex: 10M, 1.5B) en nombres."""
    if isinstance(value, (int, float)):
        return value
    if isinstance(value, str):
        value = value.strip()
        if value.endswith('M'):
            return float(value[:-1]) * 1_000_000
        elif value.endswith('B'):
            return float(value[:-1]) * 1_000_000_000
        elif value.endswith('k'):
            return float(value[:-1]) * 1_000
        else:
            return float(value)
    return np.nan
```

### Décomposition étape par étape

| Étape | Code | Exemple |
|-------|------|---------|
| Vérifier si déjà nombre | `isinstance(value, (int, float))` | `29400000` → retourné tel quel |
| Nettoyer les espaces | `value.strip()` | `" 29.4M "` → `"29.4M"` |
| Détecter le suffixe | `value.endswith('M')` | `"29.4M"` → `True` |
| Extraire le nombre | `value[:-1]` | `"29.4M"` → `"29.4"` |
| Convertir et multiplier | `float(...) * 1_000_000` | `29.4 * 1000000` → `29400000.0` |

### Le slicing `[:-1]`

```python
value = "29.4M"
value[:-1]  # Tout sauf le dernier caractère → "29.4"
```

| Slicing | Signification | Exemple avec `"29.4M"` |
|---------|---------------|------------------------|
| `[:-1]` | Tout sauf le dernier | `"29.4"` |
| `[-1]` | Dernier caractère | `"M"` |
| `[0:4]` | Index 0 à 3 | `"29.4"` |

### Le séparateur `_` dans les nombres

```python
1_000_000  # Équivalent à 1000000
```

Python permet d'utiliser `_` comme séparateur visuel dans les nombres. C'est plus lisible !

---

## 4. Fonction de formatage pour l'affichage

```python
def format_population(value, pos):
    """Formate les valeurs de population pour l'affichage (ex: 20M, 40M)."""
    if value >= 1_000_000:
        return f'{int(value / 1_000_000)}M'
    elif value >= 1_000:
        return f'{int(value / 1_000)}k'
    return str(int(value))
```

### Pourquoi deux paramètres ?

| Paramètre | Description | Fourni par |
|-----------|-------------|------------|
| `value` | La valeur numérique à formater | Matplotlib |
| `pos` | La position sur l'axe | Matplotlib (non utilisé ici) |

Matplotlib appelle cette fonction pour **chaque graduation** de l'axe.

### Exemples de conversion

| Entrée | Sortie |
|--------|--------|
| `29400000` | `"29M"` |
| `67300000` | `"67M"` |
| `1500000` | `"1M"` |
| `50000` | `"50k"` |

---

## 5. Filtrer les années (1800 à 2050)

```python
all_years = df.columns[1:]
years = [y for y in all_years if 1800 <= int(y) <= 2050]
```

### List comprehension avec condition

```python
[expression for item in iterable if condition]
```

| Partie | Code | Signification |
|--------|------|---------------|
| Expression | `y` | Ce qu'on garde |
| Iterable | `all_years` | D'où on prend |
| Condition | `1800 <= int(y) <= 2050` | Filtre |

### Visualisation du filtrage

```
Colonnes originales:
['country', '1800', '1801', ..., '2050', '2051', ..., '2100']
           ↓
df.columns[1:] (sans 'country'):
['1800', '1801', ..., '2050', '2051', ..., '2100']
           ↓
Filtrage 1800-2050:
['1800', '1801', ..., '2049', '2050']
```

### Comparaison chaînée en Python

```python
1800 <= int(y) <= 2050
```

C'est équivalent à :
```python
int(y) >= 1800 and int(y) <= 2050
```

---

## 6. Extraire les données avec list comprehension

```python
pop1 = [convert_population(data1[y].values[0]) for y in years]
pop2 = [convert_population(data2[y].values[0]) for y in years]
years_int = [int(y) for y in years]
```

### Décomposition de `data1[y].values[0]`

| Étape | Code | Résultat |
|-------|------|----------|
| Colonne année | `data1[y]` | Series avec une seule valeur |
| En array NumPy | `.values` | `array(['29.4M'])` |
| Premier élément | `[0]` | `'29.4M'` |

### Pourquoi trois listes ?

```
years_int = [1800, 1801, 1802, ...]     ← Axe X
pop1 =      [29400000, 29500000, ...]   ← Axe Y (France)
pop2 =      [3250000, 3270000, ...]     ← Axe Y (Belgium)
```

---

## 7. Tracer plusieurs courbes

```python
plt.plot(years_int, pop1, label=country1, color='green')
plt.plot(years_int, pop2, label=country2, color='blue')
```

### Nouveaux paramètres

| Paramètre | Description | Exemple |
|-----------|-------------|---------|
| `label` | Nom pour la légende | `label="France"` |
| `color` | Couleur de la courbe | `color='green'` |

### Couleurs disponibles

| Code court | Nom complet | Hex |
|------------|-------------|-----|
| `'b'` | `'blue'` | `'#0000FF'` |
| `'g'` | `'green'` | `'#008000'` |
| `'r'` | `'red'` | `'#FF0000'` |
| `'c'` | `'cyan'` | `'#00FFFF'` |
| `'m'` | `'magenta'` | `'#FF00FF'` |
| `'y'` | `'yellow'` | `'#FFFF00'` |
| `'k'` | `'black'` | `'#000000'` |
| `'w'` | `'white'` | `'#FFFFFF'` |

---

## 8. Ajouter une légende avec `plt.legend()`

```python
plt.legend(loc='lower right')
```

### Positions possibles

| Code | Position |
|------|----------|
| `'upper right'` | Haut droite |
| `'upper left'` | Haut gauche |
| `'lower right'` | Bas droite |
| `'lower left'` | Bas gauche |
| `'center'` | Centre |
| `'best'` | Automatique (évite les données) |

### Visualisation

```
┌─────────────────────────────────────┐
│ upper left    upper center    upper │
│               center         right  │
│                                     │
│ center left     center    center    │
│                           right     │
│                                     │
│ lower left   lower center   lower   │
│                             right   │
└─────────────────────────────────────┘
```

### Personnalisation

```python
plt.legend(
    loc='lower right',
    fontsize=10,
    frameon=True,       # Cadre autour de la légende
    shadow=True,        # Ombre
    title='Countries'   # Titre de la légende
)
```

---

## 9. Formater l'axe Y avec FuncFormatter

```python
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(format_population))
```

### Décomposition

| Code | Description |
|------|-------------|
| `plt.gca()` | **G**et **C**urrent **A**xes (récupère les axes actuels) |
| `ax.yaxis` | L'axe Y de ces axes |
| `.set_major_formatter()` | Définit le formateur des graduations principales |
| `plt.FuncFormatter(func)` | Crée un formateur à partir d'une fonction |

### Avant vs Après formatage

```
Sans FuncFormatter:          Avec FuncFormatter:
     │                            │
70000000 ─                    70M ─
     │                            │
60000000 ─                    60M ─
     │                            │
50000000 ─                    50M ─
     │                            │
```

### Autres formateurs disponibles

| Formateur | Description |
|-----------|-------------|
| `FuncFormatter(func)` | Fonction personnalisée |
| `PercentFormatter()` | Affiche en pourcentage |
| `ScalarFormatter()` | Notation scientifique |
| `StrMethodFormatter('{x:.2f}')` | Format string |

---

## 10. Comprendre `plt.gca()` et les Axes

Matplotlib a une hiérarchie d'objets :

```
Figure
└── Axes (zone de tracé)
    ├── XAxis (axe X)
    │   └── Ticks (graduations)
    └── YAxis (axe Y)
        └── Ticks (graduations)
```

### Deux approches

| Approche | Style | Exemple |
|----------|-------|---------|
| Implicite | `plt.xxx()` | `plt.plot()`, `plt.xlabel()` |
| Explicite | `ax.xxx()` | `ax.plot()`, `ax.set_xlabel()` |

```python
# Style implicite (utilisé principalement)
plt.plot(x, y)
plt.xlabel("X")

# Style explicite (plus de contrôle)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("X")
```

---

## 11. Gestion des valeurs manquantes avec `np.nan`

```python
import numpy as np
return np.nan
```

### Qu'est-ce que NaN ?

**NaN** = **N**ot **a** **N**umber. C'est une valeur spéciale pour représenter des données manquantes.

| Opération | Résultat |
|-----------|----------|
| `np.nan + 5` | `nan` |
| `np.nan == np.nan` | `False` (!) |
| `np.isnan(np.nan)` | `True` |

### Pourquoi retourner NaN ?

Si la conversion échoue, retourner `NaN` permet à Matplotlib de **sauter** ce point au lieu de planter.

---

## 12. Vérifier plusieurs conditions

```python
if data1.empty or data2.empty:
    print("Error: Country not found")
    return
```

### Opérateurs logiques

| Opérateur | Description | Exemple |
|-----------|-------------|---------|
| `or` | Au moins un True | `True or False` → `True` |
| `and` | Les deux True | `True and False` → `False` |
| `not` | Inverse | `not True` → `False` |

### Table de vérité `or`

| A | B | A or B |
|---|---|--------|
| False | False | False |
| False | True | True |
| True | False | True |
| True | True | True |

---

## 13. Le tuple `isinstance(value, (int, float))`

```python
if isinstance(value, (int, float)):
    return value
```

### Vérifier plusieurs types

| Syntaxe | Vérifie |
|---------|---------|
| `isinstance(x, int)` | x est un int |
| `isinstance(x, (int, float))` | x est int **ou** float |
| `isinstance(x, (int, float, str))` | x est int, float **ou** str |

### Exemples

| Expression | Résultat |
|------------|----------|
| `isinstance(42, (int, float))` | `True` |
| `isinstance(3.14, (int, float))` | `True` |
| `isinstance("42", (int, float))` | `False` |

---

## 14. Comprendre le graphique résultant

### Lecture du graphique France vs Belgium

```
                    Population Projections
    70M ─┤                                    ╭── France
        │                               ╭────╯
    60M ─┤                          ╭───╯
        │                      ╭────╯
    50M ─┤                 ╭───╯
        │            ╭─────╯
    40M ─┤    ╭──────╯  ← Baisse WWI/WWII
        │────╯
    30M ─┤
        │
    20M ─┤
        │
    10M ─┤────────────────────────────────────── Belgium
        └──────┬────────┬────────┬────────┬────────┬───
             1800    1880    1920    1960    2000    2040
```

### Observations

| Période | France | Belgium |
|---------|--------|---------|
| 1800 | ~29M | ~3M |
| 1914-1918 | Stagnation/baisse | Légère baisse |
| 1939-1945 | Stagnation | Stagnation |
| 2050 | ~67M | ~12M |

**Ratio constant :** La France a toujours environ **5-6× plus** d'habitants que la Belgique.

---

## 15. Structure attendue du fichier

```
ex02/
├── load_csv.py      # Copié depuis ex00
└── aff_pop.py       # Nouveau fichier
```

Le fichier `aff_pop.py` doit contenir :

- Imports explicites (`matplotlib.pyplot as plt`, `numpy as np`)
- Import de `load` depuis `load_csv`
- Fonction `convert_population()` avec docstring
- Fonction `format_population()` avec docstring
- Fonction `main()` avec docstring
- Filtrage des années 1800-2050
- Deux courbes avec légende
- Formatage personnalisé de l'axe Y
- Bloc `if __name__ == "__main__"`

---

## 16. Récapitulatif du flux d'exécution

```
                      python aff_pop.py
                             │
                             ▼
                    ┌─────────────────┐
                    │  load(csv)      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Filtrer pays 1  │
                    │ Filtrer pays 2  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Filtrer années  │
                    │ (1800-2050)     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Convertir       │
                    │ populations     │
                    │ (M → nombres)   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ plt.figure()    │
                    │ plt.plot() × 2  │
                    │ plt.legend()    │
                    │ FuncFormatter() │
                    │ plt.savefig()   │
                    │ plt.show()      │
                    └─────────────────┘
```

---

## 17. Résumé des nouvelles notions

| Notion | Description |
|--------|-------------|
| Conversion de suffixes | `"29.4M"` → `29400000` |
| `str.endswith()` | Vérifie la fin d'une chaîne |
| `str[:-1]` | Slicing sans le dernier caractère |
| List comprehension avec `if` | `[x for x in lst if cond]` |
| `plt.legend()` | Ajouter une légende |
| `plt.gca()` | Récupérer les axes courants |
| `FuncFormatter` | Formateur personnalisé |
| `np.nan` | Valeur manquante |
| Comparaison chaînée | `a <= x <= b` |