from moth import Moth

def initialize_population(num_moths, num_tasks, num_vms):
    """
    Initialise une population de Moths pour l'algorithme MOMFO.

    Parameters:
    - num_moths (int): Le nombre de mites dans la population.
    - num_tasks (int): Le nombre de tâches dans le problème.
    - num_vms (int): Le nombre de machines virtuelles disponibles.

    Returns:
    - Une liste contenant des instances de la classe Moth, représentant la population initiale.
    """
    return [Moth(num_tasks, num_vms) for _ in range(num_moths)]

def Makespan(z, task_lenghts, vm_processing_powers):
    """
    Calcule le makespan pour une configuration donnée z.

    Parameters:
    - z: Affectation des machines virtuelles à chaque tâche.
    - task_lengths: Liste des longueurs de chaque tâche.
    - vm_processing_powers: Liste des puissances de traitement des machines virtuelles.

    Returns:
    - Le makespan pour la configuration Z.
    """
    M1 = len(vm_processing_powers) # Nombre de machines virtuelles

    makespan = 0
    for i in range(1, M1 + 1):
        # Sélection des tâches affectées à la machine virtuelle i
        tasks_on_vm_i = [k for k, vm_index in enumerate(z) if vm_index == i]

        # Calcul du temps d'achévement pour la machine i au total (somme sur toutes les tâches)
        completion_time_i = sum(task_lenghts[k] / vm_processing_powers[i - 1] for k in tasks_on_vm_i)

        # Mise à jour du Makespan global
        makespan = max(makespan, completion_time_i)

    return makespan

def Throughput_time(z, exe_times):
    """
    Calcule le temps de débit total pour une configuration Z donnée.

    Parameters:
    - Z (list): Liste des indices de machines virtuelles attribués à chaque tâche.
    - exe_times (list): Liste des temps d'exécution de chaque tâche.

    Returns:
    - Le temps de débit total pour la configuration Z.
    """
    return sum(exe_times[k] for k in range(len(z)))

def Energy_consumption(exe_times, vm_active_powers, vm_idle_powers, makespan):
    """
    Calcule la consommation d'énergie totale.

    Parameters:
    - z (list): Liste des indices de machines virtuelles attribués à chaque tâche dans la configuration Z.
    - exe_times (list): Liste des temps d'exécution de chaque tâche.
    - vm_active_powers (list): Liste des consommations actives de chaque machine virtuelle.
    - vm_idle_powers (list): Liste des consommations au repos de chaque machine virtuelle.
    - makespan (float): La durée totale nécessaire pour terminer toutes les tâches.

    Returns:
    - La consommation d'énergie totale.
    """
    total_energy_consumption = 0
    M1 = len(vm_active_powers)

    for i in range(1, M1 + 1):
        # Calculer la consommation d'énergie pour la machine virtuelle i
        ec_i = exe_times[-1] * vm_active_powers[i-1] + (makespan - exe_times[-1]) * vm_idle_powers[i-1]
        total_energy_consumption += ec_i

    return total_energy_consumption

def calculate_objective_value(makespan, throughput_time, energy_consumption):
    """
    Calcule la valeur de l'objectif à minimiser (F).

    Parameters:
    - makespan (float): Le makespan du système.
    - throughput_time (float): Le temps de débit total du système.
    - energy_consumption (float): La consommation d'énergie totale du système.

    Returns:
    - La valeur de l'objectif à minimiser (F).
    """
    return (makespan * throughput_time * energy_consumption) / 100

def update_number_flames(num_moths, iter, max_iterations):
    """
    Calcule le nombre de "flames" (meilleures solutions) à mettre à jour à chaque itération de l'algorithme MOMFO.

    Parameters:
    - num_moths (int): Le nombre total de "moths" (solutions potentielles) dans la population.
    - iter (int): Le numéro de l'itération actuelle de l'algorithme.
    - max_iterations (int): Le nombre maximal d'itérations prévu pour l'algorithme MOMFO.

    Returns:
    - int: Le nombre de "flames" à mettre à jour à l'itération actuelle.
    """
    return round(num_moths - (iter * (num_moths - 1)) / max_iterations)

def print_assignment(position, num_vms):
    """
    Affiche l'association des taches au machines virtuelles d'une façon plus organisée.

    Parameters:
    - position (list): Position d'une Moth ou autrement dit l'affectation des machines virtuelles à chaque tâche
    - num_vms (int): Le nombre total de machines virtuelles à disposition
    """
    # Création d'un dictionnaire pour stocker les tâches associées à chaque machine virtuelle
    assignment_dict = {f"VM{i + 1}": [] for i in range(num_vms)}

    # Remplissage du dictionnaire avec les tâches associées à chaque machine virtuelle
    for task, vm in enumerate(position, start=1):
        assignment_dict[f"VM{vm}"].append(f"Tâche {task}")

    # Affichage du résultat
    for vm, tasks in assignment_dict.items():
        print(f"{vm}: {', '.join(tasks)}")
