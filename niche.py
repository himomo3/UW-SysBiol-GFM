# niche.py

import numpy as np

class Niche:
    """
    Klasa niszy przechowuje optymalny fenotyp alpha
    oraz reguły jego zmiany w czasie.
    """
    def __init__(self, alpha_init, c, delta, idx):
        """
        :param alpha_init: początkowy wektor alpha
        :param c: wektor kierunkowy zmiany
        :param delta: odchylenie std w losowej fluktuacji
        :param idx: indeks niszy (identyfikator)
        """
        self.alpha = alpha_init
        self.c = c
        self.delta = delta
        self.idx = idx

    def update(self):
        """
        Zmiana środowiska w każdym pokoleniu:
        alpha(t) = alpha(t-1) + N(c, delta^2 I)
        """
        n = len(self.alpha)
        random_shift = np.random.normal(loc=self.c, scale=self.delta, size=n)
        self.alpha = self.alpha + random_shift

    def get_optimal_phenotype(self):
        return self.alpha
