# environment.py

import numpy as np

class Environment:
    """
    Klasa środowiska przechowuje zawarte w nim nisze ewolucyjne.
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
