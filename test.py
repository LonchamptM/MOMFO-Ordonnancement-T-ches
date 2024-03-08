from heuristic import MOMFO_algorithm

# Paramètres de test
num_moths = 50        # Nombre de moths dans la population
num_tasks = 10        # Nombre de tâches à attribuer
num_vms = 5           # Nombre de machines virtuelles disponibles
tasks_lengths = [5, 8, 3, 7, 2, 6, 4, 9, 1, 5]  # Liste des longueurs de tâches
vm_processing_powers =  [10, 8, 12, 9, 11]   # Liste des puissances de traitement des machines virtuelles
exe_times = [2, 3, 1, 4, 2, 3, 2, 5, 1, 3]      # Liste des temps d'exécution de chaque tâche
vm_active_powers = [15, 13, 17, 14, 16]   # Liste des consommations actives de chaque machine virtuelle
vm_idle_powers = [5, 4, 6, 5, 5]      # Liste des consommations au repos de chaque machine virtuelle
max_iterations = 100  # Nombre maximal d'itérations
b = 0.1               # Constante pour la forme de la spirale logarithmique

best_config = MOMFO_algorithm(num_moths, num_tasks, num_vms, tasks_lengths, vm_processing_powers, exe_times, vm_active_powers, vm_idle_powers, max_iterations, b)

print(best_config.position)
