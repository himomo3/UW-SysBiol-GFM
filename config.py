# config.py

import numpy as np

# -------------------
# PARAMETRY POPULACJI
# -------------------
N = 1000           # liczba osobników w populacji
n = 2            # wymiar przestrzeni fenotypowej

# --------------------
# PARAMETRY MUTACJI
# --------------------
mu = 0.1         # prawdopodobieństwo mutacji dla osobnika
mu_c = 0.5       # prawdopodobieństwo mutacji konkretnej cechy, jeśli osobnik mutuje
xi = 0.2         # odchylenie standardowe w rozkładzie normalnym mutacji
xo = 0.1         # odchylenie standardowe w rozkładzie normalnym mutacji potomstwa

# --------------------
# PARAMETRY SELEKCJI
# --------------------
sigma = 0.2      # parametr w funkcji fitness (kontroluje siłę selekcji)
threshold = 0.1  # przykładowy próg do selekcji progowej (do ewentualnego użycia)

# --------------------
# PARAMETRY ŚRODOWISKA
# --------------------

# Liczba nisz
niche_count = 2
niche_color = ['dodgerblue', 'darkorange', 'limegreen']
habitat = [800,800,500]

# Początkowe alpha(t)
alpha0 = [np.array([0.0, -0.3]), np.array([0.0, 0.3]), np.array([0.0, 0.6])]
# Wektor kierunkowej zmiany c
#c = [np.array([0.00, 0.05]), np.array([0.00, 0.05]), np.array([0.00, 0.05])]
c = [np.array([0.15, 0.00]), np.array([0.15, 0.00]), np.array([0.05, 0.00])]
delta = 0.01    # odchylenie standardowe dla fluktuacji
max_generations = 100  # liczba pokoleń do zasymulowania

# ----------------------
# PARAMETRY REPRODUKCJI
# ----------------------
# W wersji bezpłciowej zakładamy klonowanie z uwzględnieniem mutacji.
# Jeśli chcemy modelować płciowo, trzeba dodać odpowiednie parametry.

# -----------------------
# PARAMETRY WIZUALIZACJI
# -----------------------
scatter_alpha = 0.4
