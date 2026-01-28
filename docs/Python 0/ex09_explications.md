# Explications des notions de l'exercice 09

## 1. Qu'est-ce qu'un package Python ?

Un **package** est un moyen de distribuer et réutiliser du code Python. Une fois installé, il apparaît dans `pip list` et peut être importé depuis n'importe quel script.

**Structure minimale d'un package :**

```
ex09/
├── ft_package/
│   └── __init__.py
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## 2. Le fichier `__init__.py`

Ce fichier spécial indique à Python que le dossier est un **package importable**.

```python
def count_in_list(lst: list, item) -> int:
    """Compte le nombre d'occurrences d'un élément dans une liste."""
    return lst.count(item)
```

Le code dans `__init__.py` est exécuté lors de l'import. Les fonctions définies ici sont directement accessibles :

```python
from ft_package import count_in_list
```

---

## 3. Le fichier `pyproject.toml`

C'est le fichier de **configuration principal** du package. Format TOML (Tom's Obvious Minimal Language).

### Section `[build-system]`

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"
```

Définit les outils nécessaires pour construire le package.

### Section `[project]`

```toml
[project]
name = "ft_package"
version = "0.0.1"
description = "A sample test package"
...
```

| Champ | Description |
|-------|-------------|
| `name` | Nom du package (pour `pip install`) |
| `version` | Version au format X.Y.Z |
| `description` | Description courte |
| `authors` | Auteur(s) et email(s) |
| `license` | Type de licence |
| `requires-python` | Version Python minimale |

---

## 4. La méthode `count()` des listes

```python
return lst.count(item)
```

Méthode intégrée qui compte les occurrences d'un élément dans une liste.

| Appel | Résultat |
|-------|----------|
| `["a", "b", "a"].count("a")` | `2` |
| `["a", "b", "a"].count("c")` | `0` |

---

## 5. Les formats de distribution

Deux fichiers sont générés dans le dossier `dist/` :

| Format | Fichier | Description |
|--------|---------|-------------|
| **Source** | `.tar.gz` | Archive du code source |
| **Wheel** | `.whl` | Format binaire précompilé (plus rapide à installer) |

---

## 6. Commandes pour créer le package

```bash
# Installer les outils de build
pip install build

# Construire le package (crée dist/)
python -m build
```

---

## 7. Commandes pour installer le package

```bash
# Depuis l'archive source
pip install ./dist/ft_package-0.0.1.tar.gz

# Depuis le wheel
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

---

## 8. Vérifier l'installation

```bash
# Voir si le package est installé
pip list | grep ft_package

# Afficher les informations détaillées
pip show -v ft_package
```