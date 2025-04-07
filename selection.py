# selection.py

import numpy as np

def fitness_function(phenotype, env, sigma, ind):
    """
    Funkcja fitness: phi_alpha(p) = exp( -||p - alpha||^2 / (2*sigma^2) )
    :param phenotype: fenotyp osobnika (np.array)
    :param alpha: optymalny fenotyp (np.array)
    :param sigma: odchylenie (float) kontrolujące siłę selekcji
    """
    min_dist = np.inf
    for niche in env.get_niches():
        alpha = niche.get_optimal_phenotype()
        diff = phenotype - alpha
        dist_sq = np.sum(diff ** 2)
        if dist_sq < min_dist:
            min_dist = dist_sq
            color_individual = niche.get_color_optimum()
        ind.set_color(color_individual)
    return np.exp(-min_dist / (2 * sigma ** 2))

def proportional_selection(population, env, sigma, N):
    """
    Model proporcjonalny:
      - P(rozmnożenia) = fitness / suma fitnessów
      - Generujemy nową populację wielkości N.
    """
    individuals = population.get_individuals()
    fitnesses = [fitness_function(ind.get_phenotype(), env, sigma, ind) for ind in individuals]
    total_fitness = sum(fitnesses)
    if total_fitness == 0:
        # Jeśli całkowite fitness jest 0, to każdy osobnik dostaje równą szansę
        probabilities = [1.0 / len(individuals)] * len(individuals)
    else:
        probabilities = [f / total_fitness for f in fitnesses]

    new_individuals = []
    for _ in range(N):
        chosen_idx = np.random.choice(range(len(individuals)), p=probabilities)
        new_individuals.append(individuals[chosen_idx])

    population.set_individuals(new_individuals)

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
        f = fitness_function(ind.get_phenotype(), env, sigma, ind)
        if f >= threshold:
            survivors.append(ind)
    return survivors
