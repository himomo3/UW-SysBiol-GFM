import os
import streamlit as st
import numpy as np
import config
from environment import Environment
from population import Population
from niche import Niche
from mutation import mutate_population
from selection import proportional_selection, threshold_selection
from reproduction import asexual_reproduction
from visualization import plot_population
#let's push

def main():
    st.header("Nasza reprezentacja danych")
    st.markdown("Aplikacja działa na podstawie genetycznego Modelu Fishera")
    st.sidebar.header("Simulation Parameters")
    #params for simulation
    N = st.sidebar.number_input("Population size (N)", min_value=1, value=500, step=1)
    max_generations = st.sidebar.number_input("Generations amount", min_value=1, value=50, step=1)
    if st.sidebar.button("Run Simulation"):
        niches_init = []
        for i in range(config.niche_count):
            niches_init.append(Niche(alpha_init=config.alpha0[i], c=config.c[i], delta=config.delta, idx=i))
        env = Environment(niches=niches_init)
        pop = Population(size=N, n_dim=config.n)

        # Katalog, w którym zapisujemy obrazki (możesz nazwać np. "frames/")
        frames_dir = "frames"
        os.makedirs(frames_dir, exist_ok=True)  # tworzy folder, jeśli nie istnieje

        for generation in range(max_generations):
            # 1. Mutacja
            mutate_population(pop, mu=config.mu, mu_c=config.mu_c, xi=config.xi)

            # 2. Selekcja
            survivors = threshold_selection(pop, env.get_optimal_phenotype(), config.sigma, config.threshold)
            pop.set_individuals(survivors)
            if len(survivors) > 0:
                proportional_selection(pop, env.get_optimal_phenotype(), config.sigma, config.N)
            else:
                print(f"Wszyscy wymarli w pokoleniu {generation}. Kończę symulację.")
                break

            # 3. Reprodukcja (w przykładzie jest już wbudowana w selekcję)
            # 4. Zmiana środowiska
            env.update()

            # Zapis aktualnego stanu populacji do pliku PNG
            frame_filename = os.path.join(frames_dir, f"frame_{generation:03d}.png")
            plot_population(pop, env, generation, save_path=frame_filename, show_plot=False)

        print("Symulacja zakończona. Tworzenie GIF-a...")

        # Tutaj wywołujemy funkcję, która połączy zapisane klatki w animację
        create_gif_from_frames(frames_dir, "simulation.gif")
        print("GIF zapisany jako simulation.gif")
        st.markdown("essa poszło")
        st.image("simulation.gif")

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





