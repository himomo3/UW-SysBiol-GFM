# environment.py

import numpy as np

class Environment:
    """
    Klasa środowiska przechowuje optymalny fenotyp alpha
    oraz reguły jego zmiany w czasie.
    """
    def __init__(self, niches):
        """
        :niches: nisze zawarte w środowisku
        """
        self.niches = niches

    def update(self):
        """
        Zmiana środowiska poszczególnych nisz w każdym pokoleniu:
        alpha(t) = alpha(t-1) + N(c, delta^2 I)
        """
        for niche in self.niches:
            niche.update()

    def get_optimal_phenotype(self):
        return [niche.get_optimal_phenotype() for niche in self.niches]

    def get_niches(self):
        return self.niches

    def get_optimal_phenotype(self):
        return [niche.get_optimal_phenotype() for niche in self.niches]

    def update_niches_occupancy(self):
        for niche in self.get_niches():
            amount = niche.get_individual_amount()
            habitat = niche.get_habitat()
            occupancy = (amount - habitat)/habitat
            niche.set_occupancy(occupancy)
        pass