# Exercise 01: First use of package

import time
from datetime import datetime

# Récupération du timestamp actuel
current_time = time.time()

# Formatage du timestamp avec séparateurs de milliers
formatted_time = f"{current_time:,.4f}"

# Notation scientifique
scientific_notation = f"{current_time:.2e}"

# Formatage de la date
current_date = datetime.now()
formatted_date = current_date.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {formatted_time} or "
      f"{scientific_notation} in scientific notation")
print(formatted_date)
