# Exercise 00: Load my Dataset

import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Charge un fichier CSV et affiche ses dimensions."""
    try:
        if not isinstance(path, str):
            raise TypeError("Path must be a string")

        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df

    except FileNotFoundError:
        print(f"Error: File not found: {path}")
        return None
    except pd.errors.EmptyDataError:
        print("Error: Empty CSV file")
        return None
    except pd.errors.ParserError:
        print("Error: Invalid CSV format")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
