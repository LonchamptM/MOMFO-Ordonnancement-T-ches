import random
import numpy as np
from moth import Moth
from utils import initialize_population, Makespan, Throughput_time, Energy_consumption, calculate_objective_value, update_number_flames

def MOMFO_algorithm(num_moths, num_tasks, num_vms, tasks_lengths, vm_processing_powers, exe_times, vm_active_powers, vm_idle_powers, max_iterations=100, b=0.1):
    iter = 0
    num_flames = update_number_flames(num_moths, iter, max_iterations)
    
    # Étape 1 : Initialisation de la population de moths et de flames
    population = initialize_population(num_moths, num_tasks, num_vms)

    # Etape 2 à 4 : Boucle principale de l'algorithme MOMFO
    while iter < max_iterations:
        # Calcul des scores des moths
        for moth in population:
            makespan = Makespan(moth.position, tasks_lengths, vm_processing_powers)
            throughput_time = Throughput_time(moth.position, exe_times)
            energy_consumption = Energy_consumption(exe_times, vm_active_powers, vm_idle_powers, makespan)
            moth.fitness = calculate_objective_value(makespan, throughput_time, energy_consumption)
        
        # Sélection des flames
        best_flames = sorted(population, key=lambda x: x.fitness)[:num_flames]

        for moth in population:
            # Sélection aléatoire d'une "flame" parmi les meilleures "flames"
            random_flame = random.choice(best_flames)
            
            # Modification de la position de la moth en suivant cette direction
            t = np.random.uniform(-1, 1)
            moth.update_position(random_flame, b, t)

        iter += 1
        num_flames = update_number_flames(num_moths, iter, max_iterations)

    return best_flames[-1]