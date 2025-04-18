# main.py

import numpy as np
import os
import config
from environment import Environment
from population import Population
from niche import Niche
from mutation import mutate_population
from selection import proportional_selection, threshold_selection
from reproduction import asexual_reproduction
from visualization import plot_population

def main():
    niches_init = []
    for i in range(config.niche_count):
        niches_init.append(Niche(alpha_init=config.alpha0[i], c=config.c[i], delta=config.delta, idx=i, color=config.niche_color[i], habitat=config.habitat[i]))

    env = Environment(niches=niches_init)
    pop = Population(size=config.N, n_dim=config.n)

    #tworzymy katalog do kolenych framsów
    frames_dir = "frames"
    try:
        for filename in os.listdir(frames_dir):
            file_path = os.path.join(frames_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
    except:
        pass
    os.makedirs(frames_dir, exist_ok=True)  # tworzy folder, jeśli nie istnieje

    counter = 0
    for generation in range(config.max_generations):
        print(round(counter/config.max_generations*100, 1), "% gotowe")
        counter += 1
        # 1. Mutacja
        mutate_population(pop, mu=config.mu, mu_c=config.mu_c, xi=config.xi)

        # 2. Selekcja
        survivors = threshold_selection(pop, env, config.sigma, config.threshold)
        pop.set_individuals(survivors)

        # Zapis aktualnego stanu populacji do pliku PNG
        frame_filename = os.path.join(frames_dir, f"frame_{generation:03d}.png")
        plot_population(pop, env, generation, config.scatter_alpha, save_path=frame_filename, show_plot=False)

        env.update_niches_occupancy()

        if len(survivors) > 0:
            proportional_selection(pop, env, config.sigma, config.N)
        else:
            print(f"Wszyscy wymarli w pokoleniu {generation}. Kończę symulację.")
            break

        # 3. Reprodukcja (w przykładzie jest już wbudowana w selekcję)
        # 4. Zmiana środowiska
        env.update()



    print("Symulacja zakończona. Tworzenie GIF-a...")

    # Tutaj wywołujemy funkcję, która połączy zapisane klatki w animację
    create_gif_from_frames(frames_dir, "simulation.gif")
    print("GIF zapisany jako simulation.gif")

def create_gif_from_frames(frames_dir, gif_filename, duration=0.2):
    """
    Łączy wszystkie obrazki z katalogu `frames_dir` w jeden plik GIF.
    Wymaga biblioteki imageio (pip install imageio).
    :param frames_dir: folder z plikami .png
    :param gif_filename: nazwa pliku wyjściowego GIF
    :param duration: czas wyświetlania jednej klatki w sekundach
    """
    import imageio
    import os

    # Sortujemy pliki po nazwach, żeby zachować kolejność generacji
    filenames = sorted([f for f in os.listdir(frames_dir) if f.endswith(".png")])
    
    with imageio.get_writer(gif_filename, mode='I', duration=duration) as writer:
        for file_name in filenames:
            path = os.path.join(frames_dir, file_name)
            image = imageio.imread(path)
            writer.append_data(image)


if __name__ == "__main__":
    main()
