# individual.py

import numpy as np

class Individual:
    """
    Klasa opisująca pojedynczego osobnika.
    Przechowuje wektor fenotypu w n-wymiarowej przestrzeni.
    """
    def __init__(self, phenotype):
        self.phenotype = phenotype
        self.dist = 0
        self.fitness = 0
        self.id_niche_membership = None
        self.niche_membership_history = []

    def set_phenotype(self, new_phenotype):
        self.phenotype = new_phenotype

    def get_phenotype(self):
        return self.phenotype

    def set_diff_dist(self, dist):
        self.dist = dist

    def get_diff_dist(self):
        return self.dist

    def set_fitness(self, fitness):
        self.fitness = fitness

    def get_fitness(self):
        return self.fitness

    def set_niche_membership(self, id, niche):
        self.id_niche_membership = id
        self.niche_membership_history.append(id)
        try:
            if self.niche_membership_history[-1]!=self.niche_membership_history[-2] :
                niche.gained_individual()
        except:
            pass


    def get_niche_membership(self):
        return self.id_niche_membership
