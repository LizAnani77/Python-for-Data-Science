# Exercise 08: Loading...

import os


def ft_tqdm(lst: range) -> None:
    """Affiche une barre de progression similaire à tqdm."""
    total = len(lst)

    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80

    # Calcul de la largeur disponible pour la barre
    # Format: "100%|[====>]| 333/333"
    prefix_len = 5  # "100%|"
    suffix_template = f"| {total}/{total}"
    suffix_len = len(suffix_template) + 2

    bar_width = terminal_width - prefix_len - suffix_len - 2

    for i, item in enumerate(lst, 1):
        # Calcul du pourcentage
        percent = i / total
        percent_str = f"{int(percent * 100):3d}%"

        # Calcul de la barre de progression
        filled_len = int(bar_width * percent)
        if filled_len > 0:
            bar = "=" * (filled_len - 1) + ">" + " " * (bar_width - filled_len)
        else:
            bar = " " * bar_width

        # Formatage de la sortie
        suffix = f"| {i}/{total}"

        # Affichage avec retour chariot
        print(f"\r{percent_str}|[{bar}]{suffix}", end="", flush=True)

        yield item

    print()
