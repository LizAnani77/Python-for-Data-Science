# Explications des notions de l'exercice 01

## 1. Les imports de modules

Python dispose d'une bibliothèque standard avec de nombreux modules prêts à l'emploi. Pour les utiliser, on les **importe**.

**Deux syntaxes :**

- `import time` → importe tout le module, on utilise ensuite `time.fonction()`
- `from datetime import datetime` → importe directement une classe/fonction spécifique

Le module `time` gère le temps "brut" (secondes, pauses...), tandis que `datetime` permet de manipuler des dates de façon plus humaine.

---

## 2. Le timestamp Unix (Epoch)

`time.time()` renvoie le nombre de **secondes écoulées depuis le 1er janvier 1970 à minuit UTC**.

Cette date de référence s'appelle l'**Epoch Unix**. C'est une convention universelle en informatique pour représenter le temps comme un simple nombre.

Par exemple : `1666355857.3622` signifie qu'environ 1,6 milliard de secondes se sont écoulées depuis 1970.

---

## 3. Les f-strings (formatted string literals)

Les f-strings permettent d'insérer des variables et d'appliquer un formatage directement dans une chaîne de caractères. On les reconnaît au `f` devant les guillemets.

**Syntaxe de formatage après les deux-points :**

| Format | Signification | Exemple |
|--------|---------------|---------|
| `,.4f` | Virgule comme séparateur de milliers, 4 décimales | `1,666,355,857.3622` |
| `.2e` | Notation scientifique avec 2 décimales | `1.67e+09` |

Le `:` introduit les options de formatage, c'est une mini-syntaxe à l'intérieur de l'accolade.

---

## 4. La notation scientifique

C'est une façon d'écrire les très grands (ou très petits) nombres de manière compacte.

`1.67e+09` signifie `1.67 × 10⁹` soit `1 670 000 000`

Le `e+09` indique "décale la virgule de 9 positions vers la droite".

---

## 5. Le formatage de date avec strftime

`strftime` signifie "**str**ing **f**ormat **time**". Cette méthode convertit un objet datetime en chaîne de caractères selon un modèle.

**Codes de formatage utilisés :**

| Code | Signification | Exemple |
|------|---------------|---------|
| `%b` | Mois abrégé | `Oct` |
| `%d` | Jour du mois (01-31) | `21` |
| `%Y` | Année sur 4 chiffres | `2022` |

Donc `"%b %d %Y"` produit `Oct 21 2022`.

Il existe beaucoup d'autres codes (`%H` pour l'heure, `%M` pour les minutes, etc.).

---

## 6. Résumé du flux de l'exercice

```
time.time() → nombre brut de secondes
     ↓
Formatage f-string → affichage lisible avec séparateurs
     ↓
datetime.now() → objet date/heure actuelle
     ↓
strftime() → chaîne formatée "Mois Jour Année"
```