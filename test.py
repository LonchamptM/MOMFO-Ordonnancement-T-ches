from heuristic import MOMFO_algorithm
import json

# Chargement des paramètres à partir du fichier config.json
with open('config.json', 'r') as f:
    config = json.load(f)

# Extraction des paramètres
num_moths = config['num_moths']
num_tasks = config['num_tasks']
num_vms = config['num_vms']
tasks_lengths = config['tasks_lengths']
vm_processing_powers = config['vm_processing_powers']
exe_times = config['exe_times']
vm_active_powers = config['vm_active_powers']
vm_idle_powers = config['vm_idle_powers']
max_iterations = config['max_iterations']
b = config['b']

# Affichage des paramètres de l'expérience
print("Parametres de l'experience:")
print(f"Nombre de Moths: {num_moths}")
print(f"Nombre de taches: {num_tasks}")
print(f"Nombre de machines virtuelles: {num_vms}")
print(f"Longueurs des taches: {tasks_lengths}")
print(f"Puissances de traitement des machines virtuelles: {vm_processing_powers}")
print(f"Temps d execution des taches: {exe_times}")
print(f"Consommations actives des machines virtuelles: {vm_active_powers}")
print(f"Consommations au repos des machines virtuelles: {vm_idle_powers}")
print(f"Nombre maximal d'iterations: {max_iterations}")
print(f"Constante pour la forme de la spirale logarithmique (b): {b}\n")

# Appel de l'algorithme avec les paramètres chargés
best_config = MOMFO_algorithm(num_moths, num_tasks, num_vms, tasks_lengths, vm_processing_powers, exe_times, vm_active_powers, vm_idle_powers, max_iterations, b)

print("Affichage de l'assignation optimale des taches parmi les VMs", best_config.position)
