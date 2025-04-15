# population.py

import numpy as np
from environment import Environment
from individual import Individual


class Population:
    """
    Klasa przechowuje listę osobników (Individual)
    oraz pomaga w obsłudze różnych operacji na populacji.
    """
    def __init__(self, size, n_dim):
        """
        Inicjalizuje populację losowymi fenotypami w n-wymiarach.
        :param size: liczba osobników (N)
        :param n_dim: wymiar fenotypu (n)
        """
        self.size = size
        self.individuals = []
        for _ in range(size):
            # przykładowo inicjalizujemy fenotypy w okolicach [0, 0, ..., 0]
            phenotype = np.random.normal(loc=0.0, scale=1.0, size=n_dim)
            self.individuals.append(Individual(phenotype))

    def get_individuals(self):
        return self.individuals

    def set_individuals(self, new_individuals):
        self.individuals = new_individuals

    def set_new_size(self, new_size):
        self.size = new_size

    def get_size(self):
        return self.size
