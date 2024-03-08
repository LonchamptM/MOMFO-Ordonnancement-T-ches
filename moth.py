import random
import numpy as np

class Moth:
    def __init__(self, num_tasks, num_vms):
        """Initialisation des Moths conformément au papier"""
        # Lower and upper bound definition
        LB = 1
        UB = num_vms

        # Mite position initialisation
        self.position = [random.randint(LB, UB) for _ in range(num_tasks)]
        self.fitness = None
    
    def update_position(self, flame_j, t, b=0.1):
        """Fonction qui à partir d'une flame j modifie la position d'une moth"""
        t = random.uniform(-1, 1)

        # Calcul de vector_Di
        vector_di = np.linalg.norm(np.array(flame_j.position) - np.array(self.position))
        
        # Mise à jour de la position du moth selon la formule
        updated_position = vector_di * np.exp(b * t) * np.cos(2 * np.pi * t) + np.array(flame_j.position)
        
        # Affectation de la nouvelle position au moth
        self.position = list(updated_position)
