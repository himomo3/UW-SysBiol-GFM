# niche.py

import numpy as np

class Niche:
    """
    Klasa niszy przechowuje optymalny fenotyp alpha
    oraz reguły jego zmiany w czasie.
    """
    def __init__(self, alpha_init, c, delta, idx, color, habitat):
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
        self.individual_amount = 0
        self.occupancy = 0
        self.color = color
        self.gained = 0
        self.habitat = habitat

    def update(self):
        """
        Zmiana środowiska w każdym pokoleniu:
        alpha(t) = alpha(t-1) + N(c, delta^2 I)
        """
        n = len(self.alpha)
        random_shift = np.random.normal(loc=self.c, scale=self.delta, size=n)
        self.alpha = self.alpha + random_shift

    def set_individual_amount(self, amount):
        self.individual_amount = amount

    def get_individual_amount(self):
        return self.individual_amount

    def get_optimal_phenotype(self):
        return self.alpha

    def get_niche_id(self):
        return self.idx

    def set_occupancy(self, occupancy):
        self.occupancy = occupancy

    def get_occupancy(self):
        return self.occupancy

    def get_color(self):
        return self.color

    def gained_individual(self):
        self.gained += 1

    def get_gained_individual(self):
        return self.gained

    def get_habitat(self):
        return self.habitat