# Exercise 01: Draw my country

import matplotlib.pyplot as plt
from load_csv import load


def main():
    """Affiche l'espérance de vie de la France au fil des années."""
    try:
        df = load("life_expectancy_years.csv")
        if df is None:
            return

        # Sélectionner les données de la France
        country = "France"
        country_data = df[df['country'] == country]

        if country_data.empty:
            print(f"Error: Country '{country}' not found")
            return

        # Extraire les années et les valeurs d'espérance de vie
        years = country_data.columns[1:].astype(int)
        life_expectancy = country_data.iloc[0, 1:].values

        # Créer le graphique
        plt.figure(figsize=(12, 6))
        plt.plot(years, life_expectancy)
        plt.title(f"{country} Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")

        # Configurer les ticks de l'axe X
        plt.xticks(range(1800, 2101, 40))

        plt.tight_layout()
        plt.savefig("life_expectancy_france.png")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
