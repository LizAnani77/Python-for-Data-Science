# Explications des notions de l'exercice 00

## 1. Qu'est-ce qu'un fichier CSV ?

**CSV** signifie "Comma-Separated Values" (valeurs séparées par des virgules). C'est un format texte simple pour stocker des données tabulaires.

```
country,1800,1801,1802,1803
Afghanistan,28.2,28.2,28.2,28.2
Albania,35.4,35.4,35.4,35.4
```

| Élément | Description |
|---------|-------------|
| Première ligne | En-têtes des colonnes |
| Lignes suivantes | Données (une entrée par ligne) |
| Virgule `,` | Séparateur de colonnes |

### Avantages du CSV

| Avantage | Explication |
|----------|-------------|
| Universel | Lisible par Excel, LibreOffice, Python, etc. |
| Léger | Simple fichier texte, pas de formatage |
| Humainement lisible | Ouvrable avec un éditeur de texte |

---

## 2. La bibliothèque Pandas

**Pandas** est LA bibliothèque de référence en Python pour manipuler des données tabulaires.

```python
import pandas as pd
```

### Installation

```bash
pip install pandas
```

**Note :** On importe conventionnellement pandas avec l'alias `pd` pour raccourcir l'écriture.

### Pourquoi Pandas ?

| Fonctionnalité | Description |
|----------------|-------------|
| Lecture de fichiers | CSV, Excel, JSON, SQL, etc. |
| Manipulation | Filtrer, trier, grouper, fusionner |
| Analyse | Statistiques, agrégations |
| Performance | Optimisé pour de grandes quantités de données |

---

## 3. Le DataFrame : structure centrale de Pandas

Un **DataFrame** est un tableau à deux dimensions avec des lignes et des colonnes étiquetées.

```python
df = pd.read_csv("life_expectancy_years.csv")
```

### Visualisation de la structure

```
DataFrame life_expectancy_years.csv :

              ┌─────────┬──────┬──────┬──────┬─────┬──────┐
              │ country │ 1800 │ 1801 │ 1802 │ ... │ 2100 │
              ├─────────┼──────┼──────┼──────┼─────┼──────┤
        Index │         │      │      │      │     │      │
          0   │Afghan...│ 28.2 │ 28.2 │ 28.2 │ ... │ 76.8 │
          1   │Albania  │ 35.4 │ 35.4 │ 35.4 │ ... │ 82.4 │
          2   │Algeria  │ 28.8 │ 28.8 │ 28.8 │ ... │ 83.5 │
         ...  │  ...    │ ...  │ ...  │ ...  │ ... │ ...  │
         194  │Zimbabwe │ 33.0 │ 33.0 │ 33.0 │ ... │ 71.2 │
              └─────────┴──────┴──────┴──────┴─────┴──────┘
```

| Composant | Description |
|-----------|-------------|
| Index | Numéros de ligne (0, 1, 2, ...) |
| Colonnes | Noms des colonnes (country, 1800, 1801, ...) |
| Cellules | Valeurs individuelles (28.2, 35.4, ...) |

---

## 4. Charger un CSV avec `pd.read_csv()`

La fonction `read_csv()` lit un fichier CSV et retourne un DataFrame.

```python
df = pd.read_csv("life_expectancy_years.csv")
```

### Paramètres utiles

| Paramètre | Description | Exemple |
|-----------|-------------|---------|
| `filepath` | Chemin du fichier | `"data/file.csv"` |
| `sep` | Séparateur personnalisé | `sep=";"` |
| `header` | Ligne des en-têtes | `header=0` (défaut) |
| `index_col` | Colonne à utiliser comme index | `index_col=0` |
| `encoding` | Encodage du fichier | `encoding="utf-8"` |

---

## 5. Les dimensions d'un DataFrame : `shape`

L'attribut `shape` retourne un **tuple** avec le nombre de lignes et de colonnes.

```python
print(df.shape)  # (195, 302)
```

| Élément | Position | Valeur | Signification |
|---------|----------|--------|---------------|
| Lignes | `shape[0]` | 195 | Nombre de pays |
| Colonnes | `shape[1]` | 302 | Nombre de colonnes |

### Détail des colonnes

```
302 colonnes = 1 (country) + 301 (années de 1800 à 2100)
```

### Autres attributs utiles

| Attribut | Description | Exemple de sortie |
|----------|-------------|-------------------|
| `df.shape` | Dimensions (lignes, colonnes) | `(195, 302)` |
| `df.columns` | Liste des noms de colonnes | `Index(['country', '1800', ...])` |
| `df.index` | Index des lignes | `RangeIndex(start=0, stop=195)` |
| `df.dtypes` | Types de chaque colonne | `country: object, 1800: float64` |
| `len(df)` | Nombre de lignes | `195` |

---

## 6. Afficher un DataFrame

### Affichage par défaut

```python
print(df)
```

Pandas tronque automatiquement l'affichage pour les grands DataFrames :

```
        country  1800  1801  1802  ...  2097  2098  2099  2100
0   Afghanistan  28.2  28.2  28.2  ...  76.4  76.5  76.6  76.8
1       Albania  35.4  35.4  35.4  ...  81.8  81.9  82.1  82.4
..          ...   ...   ...   ...  ...   ...   ...   ...   ...
194    Zimbabwe  33.0  33.0  33.0  ...  70.6  70.8  71.0  71.2

[195 rows x 302 columns]
```

### Contrôler l'affichage

| Méthode | Description |
|---------|-------------|
| `df.head(n)` | Affiche les n premières lignes |
| `df.tail(n)` | Affiche les n dernières lignes |
| `df.sample(n)` | Affiche n lignes aléatoires |

```python
pd.set_option('display.max_rows', 100)     # Max lignes affichées
pd.set_option('display.max_columns', 50)   # Max colonnes affichées
```

---

## 7. La gestion des erreurs avec try/except

Python utilise le mécanisme **try/except** pour gérer les erreurs sans faire planter le programme.

```python
try:
    # Code qui peut échouer
    df = pd.read_csv(path)
except SomeError:
    # Que faire si l'erreur survient
    print("Une erreur s'est produite")
```

### Structure complète

```
┌─────────────────────────────────────────────┐
│                    try:                     │
│         Code potentiellement risqué         │
├─────────────────────────────────────────────┤
│  except ErrorType1:                         │
│         Gestion de l'erreur type 1          │
├─────────────────────────────────────────────┤
│  except ErrorType2:                         │
│         Gestion de l'erreur type 2          │
├─────────────────────────────────────────────┤
│  except Exception as e:                     │
│         Gestion de toute autre erreur       │
└─────────────────────────────────────────────┘
```

---

## 8. Les exceptions spécifiques à gérer

### FileNotFoundError

Levée quand le fichier n'existe pas.

```python
except FileNotFoundError:
    print(f"Error: File not found: {path}")
    return None
```

| Cause possible | Exemple |
|----------------|---------|
| Mauvais chemin | `"data/file.csv"` au lieu de `"file.csv"` |
| Faute de frappe | `"life_expectency.csv"` |
| Fichier supprimé | Le fichier n'existe plus |

### pd.errors.EmptyDataError

Levée quand le fichier CSV est vide.

```python
except pd.errors.EmptyDataError:
    print("Error: Empty CSV file")
    return None
```

### pd.errors.ParserError

Levée quand le format CSV est invalide.

```python
except pd.errors.ParserError:
    print("Error: Invalid CSV format")
    return None
```

| Cause possible | Exemple |
|----------------|---------|
| Colonnes incohérentes | Ligne avec plus/moins de colonnes |
| Mauvais séparateur | Fichier utilisant `;` au lieu de `,` |
| Fichier corrompu | Données mal formées |

### Exception générique

Attrape toute erreur non prévue.

```python
except Exception as e:
    print(f"Error: {e}")
    return None
```

---

## 9. Vérification du type avec isinstance()

La fonction `isinstance()` vérifie si une variable est d'un type donné.

```python
if not isinstance(path, str):
    raise TypeError("Path must be a string")
```

| Vérification | Résultat |
|--------------|----------|
| `isinstance("file.csv", str)` | `True` |
| `isinstance(123, str)` | `False` |
| `isinstance(None, str)` | `False` |

### Pourquoi vérifier le type ?

| Entrée invalide | Problème potentiel |
|-----------------|-------------------|
| `load(123)` | `read_csv` attend une chaîne |
| `load(None)` | Erreur non explicite |
| `load(["file.csv"])` | Liste au lieu de chaîne |

---

## 10. Retourner None en cas d'erreur

```python
except SomeError:
    print("Error message")
    return None
```

| Situation | Retour |
|-----------|--------|
| Succès | `pd.DataFrame` (le tableau de données) |
| Erreur | `None` |

### Utilisation côté appelant

```python
df = load("life_expectancy_years.csv")
if df is not None:
    # Le chargement a réussi, on peut travailler
    print(df.head())
else:
    # Échec du chargement
    print("Impossible de charger les données")
```

---

## 11. Les docstrings (documentation)

L'exercice exige que chaque fonction ait une **docstring** (chaîne de documentation).

```python
def load(path: str) -> pd.DataFrame:
    """Charge un fichier CSV et affiche ses dimensions."""
    # code...
```

### Accéder à la documentation

```python
print(load.__doc__)
# Affiche: "Charge un fichier CSV et affiche ses dimensions."
```

### Styles de docstrings

| Style | Exemple |
|-------|---------|
| Simple | `"""Description courte."""` |
| Google | Description + Args + Returns |
| NumPy | Description + Parameters + Returns |

---

## 12. Les type hints (annotations de type)

Les **type hints** indiquent les types attendus et retournés.

```python
def load(path: str) -> pd.DataFrame:
```

| Élément | Signification |
|---------|---------------|
| `path: str` | Le paramètre `path` doit être une chaîne |
| `-> pd.DataFrame` | La fonction retourne un DataFrame |

**Note :** Les type hints sont indicatifs. Python ne les vérifie pas à l'exécution.

### Avec retour optionnel

```python
from typing import Optional

def load(path: str) -> Optional[pd.DataFrame]:
```

`Optional[pd.DataFrame]` signifie : retourne un DataFrame **ou** `None`.

---

## 13. Structure attendue du fichier

```
ex00/
└── load_csv.py
```

Le fichier doit contenir :

- Import explicite : `import pandas as pd`
- La fonction `load` avec sa docstring
- Type hints sur les paramètres et le retour
- Gestion complète des erreurs
- Affichage des dimensions avant de retourner

---

## 14. Récapitulatif du flux d'exécution

```
                    load("file.csv")
                          │
                          ▼
              ┌───────────────────────┐
              │  Vérifier type path   │
              └───────────┬───────────┘
                          │
            ┌─────────────┴─────────────┐
            │                           │
         Invalide                    Valide
            │                           │
            ▼                           ▼
    TypeError + None         ┌─────────────────────┐
                             │   pd.read_csv()     │
                             └──────────┬──────────┘
                                        │
                    ┌───────────────────┼───────────────────┐
                    │                   │                   │
               FileNotFound        EmptyData           Succès
                    │                   │                   │
                    ▼                   ▼                   ▼
               None              None              ┌─────────────────┐
                                                   │ print(shape)    │
                                                   │ return df       │
                                                   └─────────────────┘
```

---

## 15. Exemple complet d'utilisation

### Fichier tester.py

```python
from load_csv import load

print(load("life_expectancy_years.csv"))
```

### Sortie attendue

```
Loading dataset of dimensions (195, 302)
        country  1800  1801  1802  1803  ...  2096  2097  2098  2099  2100
0   Afghanistan  28.2  28.2  28.2  28.2  ...  76.2  76.4  76.5  76.6  76.8
1       Albania  35.4  35.4  35.4  35.4  ...  81.4  81.8  81.9  82.1  82.4
..          ...   ...   ...   ...   ...  ...   ...   ...   ...   ...   ...
```

### Tests d'erreurs

```python
load("fichier_inexistant.csv")  # Error: File not found
load(123)                        # Error: Path must be a string
load("fichier_vide.csv")         # Error: Empty CSV file
```