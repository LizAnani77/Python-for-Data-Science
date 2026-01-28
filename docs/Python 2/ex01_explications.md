# Explications des notions de l'exercice 01

## 1. La bibliothèque Matplotlib

**Matplotlib** est la bibliothèque de référence en Python pour créer des graphiques et visualisations.

```python
import matplotlib.pyplot as plt
```

### Installation

```bash
pip install matplotlib
```

**Note :** On importe le sous-module `pyplot` avec l'alias `plt` par convention.

### Pourquoi Matplotlib ?

| Fonctionnalité | Description |
|----------------|-------------|
| Graphiques variés | Lignes, barres, scatter, histogrammes, etc. |
| Personnalisation | Couleurs, styles, annotations, légendes |
| Export | PNG, PDF, SVG, etc. |
| Intégration | Fonctionne avec NumPy, Pandas, Jupyter |

---

## 2. Importer depuis un autre module

L'exercice réutilise la fonction `load` de l'exercice 00.

```python
from load_csv import load
```

### Structure des fichiers

```
ex01/
├── load_csv.py      # Contient la fonction load()
└── aff_life.py      # Importe et utilise load()
```

| Syntaxe | Description |
|---------|-------------|
| `from module import fonction` | Importe une fonction spécifique |
| `import module` | Importe le module entier |
| `from module import *` | ⚠️ Interdit dans ce projet |

---

## 3. Filtrer un DataFrame

Pour extraire les données d'un pays spécifique, on utilise le **filtrage conditionnel**.

```python
country_data = df[df['country'] == country]
```

### Décomposition de l'expression

```
df['country']              → Colonne 'country' (Series)
df['country'] == 'France'  → Series de booléens (True/False)
df[...]                    → Lignes où la condition est True
```

### Visualisation

```
DataFrame original (df):
┌─────────────┬──────┬──────┬─────┐
│   country   │ 1800 │ 1801 │ ... │
├─────────────┼──────┼──────┼─────┤
│ Afghanistan │ 28.2 │ 28.2 │ ... │
│ Albania     │ 35.4 │ 35.4 │ ... │
│ France      │ 34.0 │ 34.0 │ ... │  ← On veut cette ligne
│ Germany     │ 38.4 │ 38.4 │ ... │
└─────────────┴──────┴──────┴─────┘

Après filtrage (country_data):
┌─────────────┬──────┬──────┬─────┐
│   country   │ 1800 │ 1801 │ ... │
├─────────────┼──────┼──────┼─────┤
│ France      │ 34.0 │ 34.0 │ ... │
└─────────────┴──────┴──────┴─────┘
```

### Vérifier si le résultat est vide

```python
if country_data.empty:
    print(f"Error: Country '{country}' not found")
    return
```

| Attribut | Description |
|----------|-------------|
| `df.empty` | `True` si le DataFrame est vide |

---

## 4. Extraire les données pour le graphique

### Extraire les années (axe X)

```python
years = country_data.columns[1:].astype(int)
```

| Étape | Code | Résultat |
|-------|------|----------|
| Toutes les colonnes | `country_data.columns` | `['country', '1800', '1801', ...]` |
| Sans 'country' | `columns[1:]` | `['1800', '1801', '1802', ...]` |
| Convertir en entiers | `.astype(int)` | `[1800, 1801, 1802, ...]` |

### Extraire l'espérance de vie (axe Y)

```python
life_expectancy = country_data.iloc[0, 1:].values
```

| Étape | Code | Description |
|-------|------|-------------|
| `iloc[0, 1:]` | Première ligne, colonnes à partir de l'index 1 | Sélection par position |
| `.values` | Convertit en array NumPy | Format attendu par Matplotlib |

### Différence entre `loc` et `iloc`

| Méthode | Sélection par | Exemple |
|---------|---------------|---------|
| `loc` | Étiquettes (noms) | `df.loc[0, 'country']` |
| `iloc` | Position (indices) | `df.iloc[0, 0]` |

---

## 5. Créer une figure avec `plt.figure()`

```python
plt.figure(figsize=(12, 6))
```

### Le paramètre `figsize`

```
figsize=(largeur, hauteur) en pouces

        ┌────────────────────────────────────┐
        │                                    │
        │                                    │  6 pouces
        │            Figure                  │
        │                                    │
        └────────────────────────────────────┘
                    12 pouces
```

| Paramètre | Description | Défaut |
|-----------|-------------|--------|
| `figsize` | Dimensions (largeur, hauteur) | `(6.4, 4.8)` |
| `dpi` | Résolution en points par pouce | `100` |
| `facecolor` | Couleur de fond | `'white'` |

---

## 6. Tracer une courbe avec `plt.plot()`

```python
plt.plot(years, life_expectancy)
```

### Signature de base

```python
plt.plot(x, y, format, **kwargs)
```

| Argument | Description | Exemple |
|----------|-------------|---------|
| `x` | Valeurs axe horizontal | `[1800, 1801, ...]` |
| `y` | Valeurs axe vertical | `[34.0, 34.2, ...]` |
| `format` | Style de ligne (optionnel) | `'b-'`, `'ro'` |

### Codes de format

| Code | Couleur | | Code | Style |
|------|---------|---|------|-------|
| `'b'` | Bleu | | `'-'` | Ligne continue |
| `'g'` | Vert | | `'--'` | Tirets |
| `'r'` | Rouge | | `'-.'` | Tiret-point |
| `'k'` | Noir | | `':'` | Pointillés |
| `'c'` | Cyan | | `'o'` | Cercles (points) |

### Exemples

```python
plt.plot(x, y, 'r--')      # Rouge, tirets
plt.plot(x, y, 'go')       # Vert, points
plt.plot(x, y, 'b-', linewidth=2)  # Bleu, épaisseur 2
```

---

## 7. Ajouter titre et labels

```python
plt.title(f"{country} Life expectancy Projections")
plt.xlabel("Year")
plt.ylabel("Life expectancy")
```

### Fonctions de labélisation

| Fonction | Description |
|----------|-------------|
| `plt.title()` | Titre du graphique |
| `plt.xlabel()` | Label de l'axe X |
| `plt.ylabel()` | Label de l'axe Y |

### Personnalisation avancée

```python
plt.title("Titre", fontsize=16, fontweight='bold')
plt.xlabel("Année", fontsize=12, color='gray')
```

| Paramètre | Description |
|-----------|-------------|
| `fontsize` | Taille de la police |
| `fontweight` | `'normal'`, `'bold'`, `'light'` |
| `color` | Couleur du texte |
| `loc` | Position (`'left'`, `'center'`, `'right'`) |

---

## 8. Configurer les graduations avec `plt.xticks()`

```python
plt.xticks(range(1800, 2101, 40))
```

### Explication

```python
range(1800, 2101, 40)  →  [1800, 1840, 1880, 1920, 1960, 2000, 2040, 2080]
```

| Paramètre | Valeur | Signification |
|-----------|--------|---------------|
| Start | 1800 | Première valeur |
| Stop | 2101 | Fin (exclus) |
| Step | 40 | Intervalle entre les valeurs |

### Visualisation sur l'axe

```
    │                                              │
────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┼───
   1800    1840    1880    1920    1960    2000    2040    2080
```

### Fonctions similaires

| Fonction | Description |
|----------|-------------|
| `plt.xticks()` | Graduations axe X |
| `plt.yticks()` | Graduations axe Y |
| `plt.xlim(min, max)` | Limites axe X |
| `plt.ylim(min, max)` | Limites axe Y |

---

## 9. Ajuster la mise en page avec `plt.tight_layout()`

```python
plt.tight_layout()
```

### Sans vs Avec tight_layout

```
Sans tight_layout():              Avec tight_layout():
┌──────────────────────┐          ┌──────────────────────┐
│                      │          │  ┌────────────────┐  │
│    ┌────────────────┐│          │  │                │  │
│    │                ││          │  │   Graphique    │  │
│    │   Graphique    ││          │  │                │  │
│    │                ││          │  └────────────────┘  │
│    └────────────────┘│          │       Year           │
│Year (coupé!)         │          └──────────────────────┘
└──────────────────────┘
```

Cette fonction ajuste automatiquement les marges pour éviter que les labels soient coupés.

---

## 10. Sauvegarder et afficher le graphique

### Sauvegarder en fichier

```python
plt.savefig("life_expectancy_france.png")
```

| Paramètre | Description | Exemple |
|-----------|-------------|---------|
| `fname` | Nom du fichier | `"graph.png"` |
| `dpi` | Résolution | `dpi=300` |
| `bbox_inches` | Ajustement des marges | `bbox_inches='tight'` |
| `transparent` | Fond transparent | `transparent=True` |

### Formats supportés

| Extension | Format |
|-----------|--------|
| `.png` | PNG (recommandé pour le web) |
| `.pdf` | PDF (vectoriel, publications) |
| `.svg` | SVG (vectoriel, éditable) |
| `.jpg` | JPEG (photos) |

### Afficher à l'écran

```python
plt.show()
```

**⚠️ Ordre important :** `savefig()` AVANT `show()`, sinon le fichier sera vide !

```python
plt.savefig("graph.png")  # ✅ Correct
plt.show()

plt.show()
plt.savefig("graph.png")  # ❌ Fichier vide !
```

---

## 11. Le pattern main()

L'exercice exige une structure avec fonction `main()`.

```python
def main():
    """Description de la fonction."""
    # Code principal ici

if __name__ == "__main__":
    main()
```

### Pourquoi cette structure ?

| Situation | `__name__` vaut | `main()` exécuté ? |
|-----------|-----------------|-------------------|
| `python aff_life.py` | `"__main__"` | ✅ Oui |
| `from aff_life import main` | `"aff_life"` | ❌ Non |

### Avantages

| Avantage | Explication |
|----------|-------------|
| Réutilisabilité | Le module peut être importé sans exécution |
| Tests | Facilite les tests unitaires |
| Clarté | Sépare le code principal des définitions |

---

## 12. Gestion des erreurs dans main()

```python
def main():
    try:
        # Tout le code
    except Exception as e:
        print(f"Error: {e}")
```

### Points de contrôle

| Vérification | Action si échec |
|--------------|-----------------|
| `df is None` | `return` (arrêter) |
| `country_data.empty` | Message d'erreur + `return` |
| Exception inattendue | Catch-all avec message |

---

## 13. Comprendre le graphique résultant

### Lecture du graphique France

```
                France Life expectancy Projections
    90 ─┤                                          ╭───
       │                                      ╭────╯
    80 ─┤                                 ╭───╯
       │                             ╭────╯
    70 ─┤                        ╭───╯
       │                    ╭────╯
    60 ─┤               ╭───╯
       │           ╭────╯
    50 ─┤      ╭───╯
       │  ╭────╯
    40 ─┤──╯   ← Fluctuations (guerres, épidémies)
       │
    30 ─┤  ← Chute notable vers 1870 (guerre franco-prussienne)
       └──────┬────────┬────────┬────────┬────────┬────────┬───
            1800    1840    1880    1920    1960    2000    2040
                                  Year
```

### Événements historiques visibles

| Période | Observation | Cause probable |
|---------|-------------|----------------|
| ~1870 | Chute brutale | Guerre franco-prussienne |
| ~1914-1918 | Forte baisse | Première Guerre mondiale |
| ~1939-1945 | Baisse marquée | Seconde Guerre mondiale |
| Post-1945 | Croissance rapide | Progrès médicaux, paix |
| Post-2020 | Projection | Données estimées |

---

## 14. Structure attendue du fichier

```
ex01/
├── load_csv.py      # Copié depuis ex00
└── aff_life.py      # Nouveau fichier
```

Le fichier `aff_life.py` doit contenir :

- Imports explicites (`matplotlib.pyplot as plt`)
- Import de `load` depuis `load_csv`
- Fonction `main()` avec docstring
- Filtrage du DataFrame par pays
- Création du graphique avec titre et labels
- Bloc `if __name__ == "__main__"`

---

## 15. Récapitulatif du flux d'exécution

```
                      python aff_life.py
                             │
                             ▼
                    ┌─────────────────┐
                    │  load(csv)      │
                    └────────┬────────┘
                             │
                    ┌────────┴────────┐
                    │                 │
                  None            DataFrame
                    │                 │
                    ▼                 ▼
                 return      ┌─────────────────┐
                             │ Filtrer pays    │
                             └────────┬────────┘
                                      │
                             ┌────────┴────────┐
                             │                 │
                           Vide            Données
                             │                 │
                             ▼                 ▼
                          return      ┌─────────────────┐
                                      │ Extraire X, Y   │
                                      └────────┬────────┘
                                               │
                                               ▼
                                      ┌─────────────────┐
                                      │ plt.figure()    │
                                      │ plt.plot()      │
                                      │ plt.title()     │
                                      │ plt.xlabel()    │
                                      │ plt.ylabel()    │
                                      │ plt.xticks()    │
                                      │ plt.tight_layout│
                                      │ plt.savefig()   │
                                      │ plt.show()      │
                                      └─────────────────┘
```

---

## 16. Résumé des fonctions Matplotlib utilisées

| Fonction | Rôle |
|----------|------|
| `plt.figure()` | Créer une nouvelle figure |
| `plt.plot()` | Tracer une courbe |
| `plt.title()` | Ajouter un titre |
| `plt.xlabel()` | Label axe X |
| `plt.ylabel()` | Label axe Y |
| `plt.xticks()` | Définir les graduations X |
| `plt.tight_layout()` | Ajuster les marges |
| `plt.savefig()` | Sauvegarder en fichier |
| `plt.show()` | Afficher à l'écran |