# visualization.py

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

def plot_population(population, env, generation, save_path=None, show_plot=False):
    """
    Rysuje populację w 2D wraz z optymalnym fenotypem alpha.
    Można zarówno wyświetlać (show_plot=True),
    jak i zapisywać obraz (save_path != None).
    """
    alpha = env.get_optimal_phenotype()
    colors_optimum = env.get_color_optimum()
    colors_individuals = env.get_color_individual()
    x = [ind.get_phenotype()[0] for ind in population.get_individuals()]
    y = [ind.get_phenotype()[1] for ind in population.get_individuals()]
    color_pairs = []

    plt.figure(figsize=(5, 5))
    plt.scatter(x, y, label="Populacja", alpha=0.7)
    for i in range(len(alpha)):
        plt.scatter([alpha[i][0]], [alpha[i][1]], color=colors_optimum[i], label="Optimum", marker='X')
        circle = Circle((alpha[i][0], alpha[i][1]), 1, edgecolor=colors_optimum[i], fill=True, facecolor=colors_optimum[i], linewidth=1.5, alpha=0.25)
        plt.gca().add_patch(circle)

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