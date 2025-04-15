# selection.py

import numpy as np
import copy
from config import xo
from config import n

from mutation import mutate_offspring
from individual import Individual


def fitness_function(ind, env, sigma):
    """
    Funkcja fitness: phi_alpha(p) = exp( -||p - alpha||^2 / (2*sigma^2) )
    :param phenotype: fenotyp osobnika (np.array)
    :param alpha: optymalny fenotyp (np.array)
    :param sigma: odchylenie (float) kontrolujące siłę selekcji
    """
    max_fitness = 0
    for niche in env.get_niches():
        diff = ind.get_phenotype() - niche.get_optimal_phenotype()
        dist_sq = np.sum(diff**2)
        temp_fitness = np.exp(-dist_sq / (2 * sigma ** 2))*(max(1-niche.get_occupancy(),0.1))
        if temp_fitness >= max_fitness:
            max_fitness = temp_fitness
            id = niche.idx
            fav_niche = niche
            dist = dist_sq
    ind.set_diff_dist(dist)
    ind.set_niche_membership(id, fav_niche)
    ind.set_fitness(max_fitness)
    return max_fitness

def proportional_selection(population, env, sigma, N):
    """
    Model proporcjonalny: 
      - P(rozmnożenia) = fitness / suma fitnessów
      - Generujemy nową populację wielkości N.
    """
    individuals = population.get_individuals()
    fitnesses = [ind.get_fitness() for ind in individuals]
    total_fitness = sum(fitnesses)
    if total_fitness == 0:
        # Jeśli całkowite fitness jest 0, to każdy osobnik dostaje równą szansę
        probabilities = [1.0 / len(individuals)] * len(individuals)
    else:
        probabilities = [f / total_fitness for f in fitnesses]

    new_individuals = []
    for _ in range(N):
        chosen_idx = np.random.choice(range(len(individuals)), p=probabilities)
        if chosen_idx not in new_individuals:
            new_individuals.append(copy.deepcopy(individuals[chosen_idx]))
    while len(new_individuals) < N:
        #offspring = copy.deepcopy(np.random.choice(new_individuals))
        phenotype = np.random.choice(copy(new_individuals)).get_phenotype + np.random.normal(loc=0.0, scale=xo, size = n)
        new_individuals.append(Individual(phenotype))
        fitness_function(new_individuals[-1])
    population.set_individuals(new_individuals)
    population.set_new_size(len(new_individuals))

def threshold_selection(population, env, sigma, threshold):
    """
    Model progowy:
      - Eliminujemy osobniki, których fitness < threshold.
      - Pozostałe przechodzą do kolejnej fazy (o ile nie przekroczymy N).
      - Jeśli liczba ocalałych > N, wtedy dodatkowa redukcja.
    """
    individuals = population.get_individuals()
    survivors = []
    for ind in individuals:
        f = fitness_function(ind, env, sigma)
        if f >= threshold:
            survivors.append(ind)
    return survivors
