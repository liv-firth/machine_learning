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
from random import sample
from random import uniform
from math import exp
import dataset_obj
import mlp_obj

# ----
# DIFFERENTIAL EVOLUTION OBJECT CLASS
# ----

class differential_evolution:
    # -----------------------------------------
    # ORDER OF FUNCTIONS IN THE CLASS
        #INITIALIZER FUNCTION
        #
    # -----------------------------------------

    #----
    # INITIALIZER FUNCTION
    #----

    def __init__(self, mlp_object, size, n_parents):
        self.dataset = mlp_object.dataset
        self.regression = mlp_object.isRegression
        self.mutation_rate = mlp_object.l_rate
        self.n_gen = mlp_object.n_epoch
        self.network = mlp_object.network
        self.size = int(mlp_object.dataset.numObsv/10)
        self.n_parents = n_parents
        self.n_feat = mlp_object.dataset.numClass
        self.logmodel = logRessObj(self.dataset).logRess



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

# -------------------------------------------------------------
# DE ALGORITHM
# -------------------------------------------------------------

    cost_func = func_1
    bounds = [(-1,1),(-1,1)]
    popsize = 10
    mutate = .5
    recombination = .7
    maxiter = 20

    # ---- INITIALIZE A POPULATION ----
    def de(cost_func, bounds, mutate, recombination, size, maxiter):
        population = []
        for i in range(0, size):
            individual = []
            for j in range(len(bounds)):
                individual.append(uniform(bounds[j][0], bounds[j][1]))
            population.append(individual)
    # ---- SOLVE ----
        for i in range(1, maxiter+1):
            print ("GENERATION: ", i)
            gen_scores = []
            for j in range(0, size):
                candidates = list(range(0, size))
                candidates.remove(j)
                random_index = sample(candidates, 3)

                x_1 = population[random_index[0]]
                x_2 = population[random_index[1]]
                x_3 = population[random_index[2]]
                x_t = population[j]     # target individual

                # subtract x3 from x2, and create a new vector (x_diff)
                x_diff = [x_2_i - x_3_i for x_2_i, x_3_i in zip(x_2, x_3)]

                # multiply x_diff by the mutation factor (F) and add to x_1
                v_donor = [x_1_i + mutate * x_diff_i for x_1_i, x_diff_i in zip(x_1, x_diff)]
                v_donor = ensure_bounds(v_donor, bounds)

                #---- RECOMBINATION ----

                v_trial = []
                for k in range(len(x_t)):
                    crossover = random()
                    if crossover <= recombination:
                        v_trial.append(v_donor[k])

                    else:
                        v_trial.append(x_t[k])

                #---- GREEDY SELECTION ----

                score_trial  = cost_func(v_trial)
                score_target = cost_func(x_t)

                if score_trial < score_target:
                    population[j] = v_trial
                    gen_scores.append(score_trial)
                    print( '   >',score_trial, v_trial)

                else:
                    print( '   >',score_target, x_t)
                    gen_scores.append(score_target)

    def run_de(self, expected):
       gen_avg = sum(gen_scores) / popsize
       gen_best = min(gen_scores)
       gen_solution = population[gen_scores.index(min(gen_scores))]

       print("GENERATION AVERAGE: ", gen_avg)
       print("GENERATION BEST: ", gen_best)
       print("BEST SOLUTION: ", gen_solution)

       return gen_solution


