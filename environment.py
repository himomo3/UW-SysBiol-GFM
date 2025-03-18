# environment.py

import numpy as np

class Environment:
    """
    Klasa środowiska przechowuje optymalny fenotyp alpha
    oraz reguły jego zmiany w czasie.
    """
    def __init__(self, alpha_init, c, delta):
        """
        :param alpha_init: początkowy wektor alpha
        :param c: wektor kierunkowy zmiany
        :param delta: odchylenie std w losowej fluktuacji
        """
        self.alpha = alpha_init
        self.c = c
        self.delta = delta

    def update(self):
        """
        Zmiana środowiska w każdym pokoleniu:
        alpha(t) = alpha(t-1) + N(c, delta^2 I)
        """
        for i in range(len(self.alpha)):
            n = len(self.alpha[i])
            random_shift = np.random.normal(loc=self.c[i], scale=self.delta, size=n)
            self.alpha[i] = self.alpha[i] + random_shift

    def get_optimal_phenotype(self):
        return self.alpha
