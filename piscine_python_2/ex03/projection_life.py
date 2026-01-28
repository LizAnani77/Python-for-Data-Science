# Exercise 03: Draw my year 

import matplotlib.pyplot as plt
import numpy as np
from load_csv import load


def convert_income(value):
    """Convertit les valeurs de revenu (ex: 10k, 1.5M) en nombres."""
    if isinstance(value, (int, float)):
        return value
    if isinstance(value, str):
        value = value.strip()
        if value.endswith('k'):
            return float(value[:-1]) * 1_000
        elif value.endswith('M'):
            return float(value[:-1]) * 1_000_000
        elif value.endswith('B'):
            return float(value[:-1]) * 1_000_000_000
        else:
            return float(value)
    return np.nan


def main():
    """Affiche la projection de l'espérance de vie vs GDP pour 1900."""
    try:
        # Charger les datasets
        income_df = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
        life_df = load("life_expectancy_years.csv")

        if income_df is None or life_df is None:
            return

        year = "1900"

        # Vérifier que l'année existe dans les deux datasets
        if year not in income_df.columns or year not in life_df.columns:
            print(f"Error: Year {year} not found in datasets")
            return

        # Fusionner les données sur le pays
        merged = income_df[['country', year]].merge(
            life_df[['country', year]],
            on='country',
            suffixes=('_income', '_life')
        )

        # Convertir les valeurs
        gdp = merged[f'{year}_income'].apply(convert_income)
        life_exp = merged[f'{year}_life'].astype(float)

        # Supprimer les valeurs manquantes
        valid_mask = ~(gdp.isna() | life_exp.isna())
        gdp = gdp[valid_mask]
        life_exp = life_exp[valid_mask]

        # Créer le scatter plot
        plt.figure(figsize=(10, 8))
        plt.scatter(gdp, life_exp, alpha=0.7, edgecolors='black', linewidth=0.5)

        plt.title(year)
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")

        # Échelle logarithmique pour l'axe X
        plt.xscale('log')
        plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])

        plt.tight_layout()
        plt.savefig("projection_life_1900.png")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
