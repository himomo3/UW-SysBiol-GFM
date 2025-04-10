# individual.py

import numpy as np

class Individual:
    """
    Klasa opisująca pojedynczego osobnika.
    Przechowuje wektor fenotypu w n-wymiarowej przestrzeni.
    """
    def __init__(self, phenotype):
        self.phenotype = phenotype
        self.color = "Grey"

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def get_phenotype(self):
        return self.phenotype

    def set_phenotype(self, new_phenotype):
        self.phenotype = new_phenotype
