# visualization.py

import matplotlib.pyplot as plt
import numpy as np

def plot_population(population, env, generation, scatter_alpha, save_path=None, show_plot=False):
    """
    Rysuje populację w 2D wraz z optymalnym fenotypem alpha.
    Można zarówno wyświetlać (show_plot=True),
    jak i zapisywać obraz (save_path != None).
    """
    pop = population.get_individuals()
    niches = env.get_niches()
    plt.figure(figsize=(10, 10))

    for niche in niches:
        population_to_plot = []
        for ind in pop:
            if ind.get_niche_membership() == niche.get_niche_id():
                population_to_plot.append(ind)
        x = [ind.get_phenotype()[0] for ind in population_to_plot]
        y = [ind.get_phenotype()[1] for ind in population_to_plot]
        amount = len(x)
        color = niche.get_color()
        niche.set_individual_amount(amount)
        plt.scatter(x, y, label=f"ilość osobników: {amount}", color=color, alpha=scatter_alpha)
        alpha = niche.get_optimal_phenotype()
        changed = niche.get_gained_individual()
        plt.scatter(alpha[0], alpha[1], color=color, edgecolor="black", label=f"Optimum, zmieniło: {changed}", marker='X', s=100)

    alpha = env.get_optimal_phenotype()

    plt.title(f"Pokolenie: {generation}")
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.legend()
    plt.tight_layout()
    
    if save_path is not None:
        plt.savefig(save_path)  # Zapis do pliku
    if show_plot:
        plt.show()
    else:
        # Jeśli nie chcesz pokazywać, to zamykaj figurę, 
        # żeby nie zapełniać pamięci
        plt.close()
