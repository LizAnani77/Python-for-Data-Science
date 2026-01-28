# Exercise 02: Compare my country 

import matplotlib.pyplot as plt
import numpy as np
from load_csv import load


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


def format_population(value, pos):
    """Formate les valeurs de population pour l'affichage (ex: 20M, 40M)."""
    if value >= 1_000_000:
        return f'{int(value / 1_000_000)}M'
    elif value >= 1_000:
        return f'{int(value / 1_000)}k'
    return str(int(value))


def main():
    """Compare la population de la France et de la Belgique."""
    try:
        df = load("population_total.csv")
        if df is None:
            return

        # Pays à comparer
        country1 = "France"
        country2 = "Belgium"

        # Sélectionner les données des pays
        data1 = df[df['country'] == country1]
        data2 = df[df['country'] == country2]

        if data1.empty or data2.empty:
            print("Error: Country not found")
            return

        # Filtrer les années de 1800 à 2050
        all_years = df.columns[1:]
        years = [y for y in all_years if 1800 <= int(y) <= 2050]

        # Extraire et convertir les valeurs de population
        pop1 = [convert_population(data1[y].values[0]) for y in years]
        pop2 = [convert_population(data2[y].values[0]) for y in years]
        years_int = [int(y) for y in years]

        # Créer le graphique
        plt.figure(figsize=(12, 6))
        plt.plot(years_int, pop1, label=country1, color='green')
        plt.plot(years_int, pop2, label=country2, color='blue')

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend(loc='lower right')

        # Configurer les ticks
        plt.xticks(range(1800, 2051, 40))
        ax = plt.gca()
        ax.yaxis.set_major_formatter(plt.FuncFormatter(format_population))

        plt.tight_layout()
        plt.savefig("population_comparison.png")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
