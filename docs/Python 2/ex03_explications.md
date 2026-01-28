# Explications des notions de l'exercice 03

## 1. Objectif de l'exercice

Créer un **scatter plot** (nuage de points) montrant la relation entre :
- **Axe X :** PIB par habitant (GDP per capita)
- **Axe Y :** Espérance de vie

Pour l'année **1900**, afin d'observer la **corrélation** entre richesse et longévité.

---

## 2. Les deux fichiers de données

### income_per_person_gdppercapita_ppp_inflation_adjusted.csv

```csv
country,1800,1801,...,1900,...
France,1780,1790,...,4520,...
Germany,1640,1650,...,4790,...
```

**Contenu :** PIB par habitant en dollars (ajusté pour l'inflation et la parité de pouvoir d'achat).

### life_expectancy_years.csv

```csv
country,1800,1801,...,1900,...
France,34.0,34.2,...,46.5,...
Germany,38.4,38.5,...,44.8,...
```

**Contenu :** Espérance de vie en années.

### Le défi

| Fichier | Colonnes | Lignes |
|---------|----------|--------|
| Income | country + années | ~195 pays |
| Life expectancy | country + années | ~195 pays |

Il faut **fusionner** ces deux fichiers pour avoir GDP et Life Expectancy **pour chaque pays**.

---

## 3. Fusionner deux DataFrames avec `merge()`

```python
merged = income_df[['country', year]].merge(
    life_df[['country', year]],
    on='country',
    suffixes=('_income', '_life')
)
```

### Qu'est-ce qu'un merge ?

C'est l'équivalent d'un **JOIN** en SQL : combiner deux tableaux sur une colonne commune.

### Visualisation du merge

```
income_df[['country', '1900']]:       life_df[['country', '1900']]:
┌─────────────┬──────┐               ┌─────────────┬──────┐
│   country   │ 1900 │               │   country   │ 1900 │
├─────────────┼──────┤               ├─────────────┼──────┤
│ France      │ 4520 │               │ France      │ 46.5 │
│ Germany     │ 4790 │               │ Germany     │ 44.8 │
│ Spain       │ 2800 │               │ Spain       │ 35.7 │
└─────────────┴──────┘               └─────────────┴──────┘
              │                                   │
              └──────────────┬────────────────────┘
                             │ merge on='country'
                             ▼
              ┌─────────────┬─────────────┬────────────┐
              │   country   │ 1900_income │ 1900_life  │
              ├─────────────┼─────────────┼────────────┤
              │ France      │    4520     │    46.5    │
              │ Germany     │    4790     │    44.8    │
              │ Spain       │    2800     │    35.7    │
              └─────────────┴─────────────┴────────────┘
```

### Paramètres du merge

| Paramètre | Description | Valeur |
|-----------|-------------|--------|
| `on` | Colonne de jointure | `'country'` |
| `suffixes` | Suffixes pour colonnes dupliquées | `('_income', '_life')` |
| `how` | Type de jointure (défaut: inner) | Non spécifié |

### Types de jointures

| Type | Description | Résultat |
|------|-------------|----------|
| `'inner'` | Seulement les pays présents dans les deux | Défaut |
| `'left'` | Tous les pays du premier DataFrame | |
| `'right'` | Tous les pays du second DataFrame | |
| `'outer'` | Tous les pays des deux DataFrames | |

```python
# Exemple avec type explicite
merged = df1.merge(df2, on='country', how='inner')
```

---

## 4. Sélectionner des colonnes spécifiques

```python
income_df[['country', year]]
```

### Syntaxe avec double crochets

| Syntaxe | Retourne | Type |
|---------|----------|------|
| `df['country']` | Une colonne | Series |
| `df[['country']]` | Une colonne | DataFrame |
| `df[['country', '1900']]` | Plusieurs colonnes | DataFrame |

### Pourquoi extraire seulement ces colonnes ?

```python
# Au lieu de fusionner 302 colonnes × 2...
income_df.merge(life_df)  # ❌ Trop de données

# On ne prend que ce qu'on utilise
income_df[['country', '1900']].merge(...)  # ✅ Efficace
```

---

## 5. Appliquer une fonction avec `apply()`

```python
gdp = merged[f'{year}_income'].apply(convert_income)
```

### Qu'est-ce que `apply()` ?

`apply()` applique une fonction à **chaque élément** d'une Series.

```
Series:                    Après apply(convert_income):
┌───────┐                  ┌───────────┐
│ "4.5k"│  ──────────────► │   4500    │
│ "2.8k"│  convert_income  │   2800    │
│ "10k" │  ──────────────► │  10000    │
└───────┘                  └───────────┘
```

### Équivalent avec list comprehension

```python
# Avec apply (recommandé pour pandas)
gdp = merged['1900_income'].apply(convert_income)

# Équivalent avec list comprehension
gdp = [convert_income(x) for x in merged['1900_income']]
```

### Avantages de `apply()`

| Avantage | Description |
|----------|-------------|
| Optimisé | Plus rapide sur grandes données |
| Chaînable | `df['col'].apply(f).apply(g)` |
| Intégré | Retourne une Series pandas |

---

## 6. Convertir le type avec `astype()`

```python
life_exp = merged[f'{year}_life'].astype(float)
```

### Types de données courants

| Type | Description | Exemple |
|------|-------------|---------|
| `int` | Entier | `42` |
| `float` | Décimal | `42.5` |
| `str` | Chaîne | `"42"` |
| `bool` | Booléen | `True` |

### Conversions courantes

```python
series.astype(float)   # Convertir en float
series.astype(int)     # Convertir en int
series.astype(str)     # Convertir en string
```

### Différence entre `apply()` et `astype()`

| Méthode | Utilisation |
|---------|-------------|
| `apply(func)` | Transformation complexe avec logique |
| `astype(type)` | Conversion de type simple |

```python
# astype : conversion simple
df['col'].astype(float)  # "42.5" → 42.5

# apply : logique complexe nécessaire
df['col'].apply(convert_income)  # "4.5k" → 4500
```

---

## 7. Gérer les valeurs manquantes

```python
valid_mask = ~(gdp.isna() | life_exp.isna())
gdp = gdp[valid_mask]
life_exp = life_exp[valid_mask]
```

### Décomposition de l'expression

| Étape | Code | Description |
|-------|------|-------------|
| Valeurs NaN dans GDP | `gdp.isna()` | Series de booléens |
| Valeurs NaN dans Life | `life_exp.isna()` | Series de booléens |
| Au moins un NaN | `gdp.isna() \| life_exp.isna()` | True si NaN quelque part |
| Inverse (valides) | `~(...)` | True si les deux sont valides |

### L'opérateur `~` (NOT bit à bit)

```python
mask = pd.Series([True, False, True])
~mask  # [False, True, False]
```

### L'opérateur `|` (OR bit à bit)

```python
a = pd.Series([True, False, True])
b = pd.Series([False, False, True])
a | b  # [True, False, True]
```

**⚠️ Note :** Avec pandas, utiliser `|` et `&` au lieu de `or` et `and`.

### Visualisation du filtrage

```
gdp:      life_exp:    isna(gdp):  isna(life):   |        ~(|)      Filtré:
┌──────┐  ┌──────┐     ┌───────┐   ┌───────┐   ┌───────┐  ┌───────┐  ┌──────┐
│ 4500 │  │ 46.5 │     │ False │   │ False │   │ False │  │ True  │  │ 4500 │
│  NaN │  │ 44.8 │     │ True  │   │ False │   │ True  │  │ False │  │      │
│ 2800 │  │  NaN │     │ False │   │ True  │   │ True  │  │ False │  │      │
│ 3200 │  │ 35.7 │     │ False │   │ False │   │ False │  │ True  │  │ 3200 │
└──────┘  └──────┘     └───────┘   └───────┘   └───────┘  └───────┘  └──────┘
```

---

## 8. Créer un scatter plot avec `plt.scatter()`

```python
plt.scatter(gdp, life_exp, alpha=0.7, edgecolors='black', linewidth=0.5)
```

### Différence entre `plot()` et `scatter()`

| Fonction | Type | Usage |
|----------|------|-------|
| `plt.plot()` | Ligne | Données continues, séries temporelles |
| `plt.scatter()` | Points | Corrélation, distribution, comparaison |

### Visualisation

```
plt.plot():                    plt.scatter():
     │                              │
   ──┼──╮                         ──┼──  ·  ·
     │   ╲                          │    ·
     │    ╲──╮                      │  ·   ·
     │       ╲──                    │    ·
     └────────────                  └────────────
```

### Paramètres de `scatter()`

| Paramètre | Description | Exemple |
|-----------|-------------|---------|
| `x` | Coordonnées X | `gdp` |
| `y` | Coordonnées Y | `life_exp` |
| `alpha` | Transparence (0-1) | `0.7` |
| `s` | Taille des points | `50` |
| `c` | Couleur | `'blue'` ou array |
| `edgecolors` | Couleur du contour | `'black'` |
| `linewidth` | Épaisseur du contour | `0.5` |
| `marker` | Forme du point | `'o'`, `'s'`, `'^'` |

### Exemples de markers

| Marker | Forme |
|--------|-------|
| `'o'` | Cercle (défaut) |
| `'s'` | Carré |
| `'^'` | Triangle haut |
| `'v'` | Triangle bas |
| `'*'` | Étoile |
| `'+'` | Plus |
| `'x'` | Croix |

---

## 9. L'échelle logarithmique avec `plt.xscale('log')`

```python
plt.xscale('log')
```

### Pourquoi une échelle logarithmique ?

Les données de PIB ont une **grande amplitude** (de ~300 à ~10000). L'échelle log permet de mieux visualiser.

### Comparaison linéaire vs logarithmique

```
Échelle linéaire:               Échelle logarithmique:
     │                               │
     │                 ·             │        ·  · ·
     │              ·                │      ·  ·
     │            ·                  │    ·  ·
     │         ·                     │  · ·
     │·· ·                           │· ·
     └──────────────────             └──────────────────
     0    2500   5000  10000         300   1k    10k
```

### Types d'échelles disponibles

| Échelle | Code | Description |
|---------|------|-------------|
| Linéaire | `'linear'` | Défaut |
| Logarithmique | `'log'` | Base 10 |
| Symétrique log | `'symlog'` | Log avec valeurs négatives |
| Logit | `'logit'` | Pour probabilités (0-1) |

```python
plt.xscale('log')   # Axe X en log
plt.yscale('log')   # Axe Y en log
```

---

## 10. Personnaliser les graduations avec `plt.xticks()`

```python
plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
```

### Signature complète

```python
plt.xticks(positions, labels)
```

| Paramètre | Description | Exemple |
|-----------|-------------|---------|
| `positions` | Où placer les ticks | `[300, 1000, 10000]` |
| `labels` | Texte à afficher | `['300', '1k', '10k']` |

### Visualisation

```
Positions:  [300,     1000,      10000]
Labels:     ['300',   '1k',      '10k']

     │
     │                              ·  ·
     │                         ·  ·
     │                    · ·
     │              · ·
     │        · ·
     └────────┼───────────┼────────────┼───
            300          1k           10k
```

### Sans labels personnalisés

```python
plt.xticks([300, 1000, 10000])
# Afficherait: 300, 1000, 10000 (nombres bruts)
```

---

## 11. Les f-strings avec variables

```python
f'{year}_income'  # Avec year = "1900" → "1900_income"
```

### Syntaxe des f-strings

```python
f'texte {variable} texte'
```

| Expression | Résultat (year="1900") |
|------------|------------------------|
| `f'{year}'` | `"1900"` |
| `f'{year}_income'` | `"1900_income"` |
| `f'Year: {year}'` | `"Year: 1900"` |

### Pourquoi utiliser une f-string ici ?

```python
year = "1900"

# Sans f-string (concaténation)
merged[year + '_income']  # Fonctionne mais moins lisible

# Avec f-string
merged[f'{year}_income']  # Plus clair
```

---

## 12. Vérifier l'existence d'une colonne

```python
if year not in income_df.columns or year not in life_df.columns:
    print(f"Error: Year {year} not found in datasets")
    return
```

### L'opérateur `in`

| Expression | Description |
|------------|-------------|
| `x in list` | x est dans la liste |
| `x not in list` | x n'est pas dans la liste |
| `x in df.columns` | x est un nom de colonne |

### Exemple

```python
df.columns  # Index(['country', '1800', '1801', ..., '2100'])

'1900' in df.columns      # True
'3000' in df.columns      # False
'country' in df.columns   # True
```

---

## 13. Comprendre le graphique résultant

### Lecture du scatter plot

```
                           1900
    55 ─┤                              · ·
        │                            · · ·
    50 ─┤                          · · ·
        │                         ·  ·
    45 ─┤                      · ·
        │                   · · ·
    40 ─┤                · · · ·
        │             · · · · ·
    35 ─┤          · · · · ·
        │       · · · · ·
    30 ─┤    · · · ·
        │  · · ·
    25 ─┤· ·
        │
    20 ─┤ ·
        └────────┬─────────────┬────────────┬───
               300            1k           10k
                    Gross domestic product
```

### La corrélation

**Observation :** Les points forment une tendance **ascendante** de gauche à droite.

| GDP | Life Expectancy | Interprétation |
|-----|-----------------|----------------|
| Faible (~300-500) | ~20-30 ans | Pays pauvres |
| Moyen (~1000-2000) | ~30-40 ans | Pays intermédiaires |
| Élevé (~5000-10000) | ~45-55 ans | Pays riches |

### Corrélation positive

```
Corrélation positive:      Corrélation négative:     Pas de corrélation:
        │    · ·                  │· ·                      │  ·    ·
        │  · ·                    │  · ·                    │    ·
        │· ·                      │    · ·                  │ ·   ·
        │·                        │      · ·                │   ·  ·
        └────────                 └────────                 └────────
```

**Conclusion :** En 1900, il existait une **corrélation positive** entre la richesse d'un pays et l'espérance de vie de ses habitants.

---

## 14. La transparence avec `alpha`

```python
plt.scatter(gdp, life_exp, alpha=0.7)
```

### Échelle de transparence

| Valeur | Effet |
|--------|-------|
| `0.0` | Totalement transparent |
| `0.5` | Semi-transparent |
| `1.0` | Totalement opaque |

### Pourquoi utiliser la transparence ?

```
Sans alpha (alpha=1.0):        Avec alpha (alpha=0.7):
Points superposés invisibles   Superpositions visibles

        │    ●                        │    ◐
        │  ●                          │  ◐◐
        │●●                           │◐◐◐
        └────────                     └────────
```

Avec `alpha < 1`, les zones avec beaucoup de points apparaissent **plus foncées**.

---

## 15. Structure attendue du fichier

```
ex03/
├── load_csv.py           # Copié depuis ex00
└── projection_life.py    # Nouveau fichier
```

Le fichier `projection_life.py` doit contenir :

- Imports explicites (`matplotlib.pyplot as plt`, `numpy as np`)
- Import de `load` depuis `load_csv`
- Fonction `convert_income()` avec docstring
- Fonction `main()` avec docstring
- Chargement des deux CSV
- Fusion avec `merge()`
- Gestion des valeurs manquantes
- Scatter plot avec échelle log
- Bloc `if __name__ == "__main__"`

---

## 16. Récapitulatif du flux d'exécution

```
                    python projection_life.py
                             │
                             ▼
              ┌──────────────────────────────┐
              │  load(income.csv)            │
              │  load(life_expectancy.csv)   │
              └──────────────┬───────────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │  Vérifier année existe       │
              └──────────────┬───────────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │  merge() sur 'country'       │
              │  Suffixes: _income, _life    │
              └──────────────┬───────────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │  apply(convert_income)       │
              │  astype(float)               │
              └──────────────┬───────────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │  Filtrer valeurs NaN         │
              └──────────────┬───────────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │  plt.scatter()               │
              │  plt.xscale('log')           │
              │  plt.xticks()                │
              │  plt.savefig()               │
              │  plt.show()                  │
              └──────────────────────────────┘
```

---

## 17. Résumé des nouvelles notions

| Notion | Description |
|--------|-------------|
| `df.merge()` | Fusionner deux DataFrames |
| `on='column'` | Colonne de jointure |
| `suffixes` | Renommer colonnes dupliquées |
| `series.apply(func)` | Appliquer fonction à chaque élément |
| `series.astype(type)` | Convertir le type |
| `series.isna()` | Détecter les NaN |
| `~` (tilde) | Opérateur NOT bit à bit |
| `\|` (pipe) | Opérateur OR bit à bit |
| `plt.scatter()` | Nuage de points |
| `alpha` | Transparence |
| `plt.xscale('log')` | Échelle logarithmique |
| `f'{var}_suffix'` | f-string avec variable |

---

## 18. Question de réflexion

> **"Do you see a correlation between life span and gross domestic product?"**

**Réponse attendue :** Oui, le graphique montre une **corrélation positive** entre le PIB par habitant et l'espérance de vie en 1900. Les pays plus riches avaient généralement une espérance de vie plus élevée.

**Nuances à mentionner :**
- Corrélation ≠ Causalité
- D'autres facteurs interviennent (système de santé, climat, guerres...)
- La relation n'est pas parfaitement linéaire
- Certains pays pauvres avaient une bonne espérance de vie (et vice versa)