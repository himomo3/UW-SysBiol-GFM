# niche.py

import numpy as np

class Niche:
    """
    Klasa niszy przechowuje optymalny fenotyp alpha
    oraz reguły jego zmiany w czasie.
    """
    #funkcja losująca kolor dla optimum niszy
    def _random_color(self):
        return np.random.rand(3)
    #funkcja losująmy kolor dla osobników należących do tej niszy
    def _lighten_color(self, color, factor=0.25):
        return np.clip(color+(1-color)*factor,0,1)
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
        self.color_optimum = self._random_color()
        self.color_individual = self._lighten_color(self.color_optimum)
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
    def get_color_optimum(self):
        return self.color_optimum
    def get_color_individual(self):
        return self.color_individual