"""
CSCI 447 - Machine Learning
Project Four

Differential Evolution Algorithm Class

@author: Claire Richards, Olivia Firth, Hannah Cebulla
"""

#IMPORT THE FOLLOWING PACKAGES AND FILES
import copy
from random import seed
from random import random
from math import exp

import dataset_obj
import mlp_obj

# ----
# DIFFERENTIAL EVOLUTION OBJECT CLASS
# ----

class differential_evolution:
    # -----------------------------------------
    # ORDER OF FUNCTIONS IN THE CLASS
        #
    # -----------------------------------------

    def ensure_bounds(vector, bounds):  # determine where the variable is in the boundaries
        new_vector = []
        for i in range(len(vector)):  # cycle through each variable in the vector
            if vector[i] < bounds[i][0]:  # if variable exceeds the min boundary
                new_vector.append(bounds[i][0])
            if vector[i] > bounds[i][0]:  # if variable exceeds the max boundary
                new_vector.append(bounds[i][1])
            if bounds[i][0] <= vector[i] <= bounds[i][0]:  # if variable lies within the boundaries
                new_vector.append(vector[i])
        return new_vector

    def main(bounds, popsize):
        population = []
        for i in range(0, popsize):
            indv = []
            for j in range(len(bounds)):
                indv.append(random.uniform(bounds[j][0],bounds[j][1]))
            population.append(indv)
        return best_individual
