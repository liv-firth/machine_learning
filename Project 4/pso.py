# -*- coding: utf-8 -*-
"""
CSCI 447 - Machine Learning
Project Three

Particle Swarm Optimization

@author: Claire Richards, Olivia Firth, Hannah Cebulla
"""

# IMPORT THE FOLLOWING PACKAGES AND FILES
import copy
import pandas as pd 
from random import seed
from random import random
from math import exp

import dataset_obj

# ----
# Particle Swarm Optimization Class
# ----
class pso:
    # -----------------------------------------
    # ORDER OF FUNCTIONS WITHIN THE CLASS 
        # UNIVERSAL INTERNAL FUNCTIONS
            # INITALIZER FOR MLP OBJECT
            # 
    # FUNCTIONS IN THE DOCUMENT, OUTSIDE THE CLASS
        # 
        # 
    # -----------------------------------------

    # ----------------------------------------- #
    # ------ UNIVERSL INTERNAL FUNCTIONS ------ #  
    # ----------------------------------------- #
    
    # ----
    # INITALIZER FUNCTION
    # ----
    def __init__(self, data_object, l_rate, n_epoch):
        self.dataset = data_object #Pulls dataset object for easy reference
        self.isRegression = data_object.regression #Indicates if dataset being imported into
        self.l_rate = l_rate #Learning Rate is given
        self.n_epoch = n_epoch #Specify Number of Epochs for Training
        self.c = 1 #For regression Activations
    
        # ----------------------------------------- #
        # --- BUILD BASE NETWORK AND ACTIVATION --- #  
        # ----------------------------------------- #
    # ----
    # INITALIZE POPULATION
    # ----
    def initalization_of_pop(size, n_feat):
        population = []
        for i in range(size):
            chromosome = np.ones(n_feat, dtype=np.bool)
            chromosome[:int(0.3*n_feat)]=False
            np.random.shuffle(chromosome)
            population.append(chromosome)
        return population
    
    # ----
    # GET FITNESS SCORE OF POPULATION
    # ----
    def fitness_score(population):
        scores = []
        for chromosome in population:
            logmodel.fit(X_train.iloc[:,chromosome],y_train)
            predictions = logmodel.predict(X_test.iloc[:,chromosome])
            scores.append(accuracy_score(y_test,predictions))
        scores, population = np.array(scores), np.array(population) 
        inds = np.argsort(scores)
        return list(scores[inds][::-1]), list(population[inds,:][::-1])
    
    def selection(pop_after_fit, n_parents):
        population_nextgen = []
        for i in range(n_parents):
            population_nextgen.append(pop_after_fit[i])
        return population_nextgen
    
    def crossover(pop_after_sel):
        population_nextgen=pop_after_sel
        for i in range(len(pop_after_sel)):
            child=pop_after_sel[i]
            child[3:7]=pop_after_sel[(i+1)%len(pop_after_sel)][3:7]
            population_nextgen.append(child)
        return population_nextgen
    
    def mutation(pop_after_cross,mutation_rate):
        population_nextgen = []
        for i in range(0,len(pop_after_cross)):
            chromosome = pop_after_cross[i]
            for j in range(len(chromosome)):
                if random.random() < mutation_rate:
                    chromosome[j]= not chromosome[j]
            population_nextgen.append(chromosome)
        #print(population_nextgen)
        return population_nextgen
    
    def generations(size,n_feat,n_parents,mutation_rate,n_gen,X_train,
                                       X_test, y_train, y_test):
        best_chromo= []
        best_score= []
        population_nextgen=initilization_of_population(size,n_feat)
        for i in range(n_gen):
            scores, pop_after_fit = fitness_score(population_nextgen)
            print(scores[:2])
            pop_after_sel = selection(pop_after_fit,n_parents)
            pop_after_cross = crossover(pop_after_sel)
            population_nextgen = mutation(pop_after_cross,mutation_rate)
            best_chromo.append(pop_after_fit[0])
            best_score.append(scores[0])
        return best_chromo,best_score    

            
                

# ----------------------------------------- #
# ------ FUNCTIONS OUTSIDE THE CLASS ------ #  
# ----------------------------------------- #   
        
# ----
# DEFINE TO CREATE, TRAIN, AND RUN THE MLP
# ---- 
def run_ga(data_object, n_hiddenList, l_rate, n_epoch):   
    
    #Tune the Hidden Layers Using Learning Rate of 0.1
    hiddenLayerAccuracy = list() #Blank List to Append To
    for i in n_hiddenList:
        temp_mlp = mlp(data_object, 0.1, n_epoch) #Initalize MLP
        temp_mlp.initalizeNetwork(i) #Initalize the Base Network
        temp_mlp.evaluate()
        hiddenLayerAccuracy.append(temp_mlp.accuracy)
    
    #Find best hidden layer
    n_hidden = n_hiddenList[hiddenLayerAccuracy.index(max(hiddenLayerAccuracy))]
    
    #Tune the Learning Rate
    l_Accuracy = list()
    for i in l_rate:
        temp_mlp = mlp(data_object, i, n_epoch) #Initalize MLP
        temp_mlp.initalizeNetwork(n_hidden) #Initalize the Base Network
        temp_mlp.evaluate()
        l_Accuracy.append(temp_mlp.accuracy)
    #Find the best l_rate
    convergence = l_rate[l_Accuracy.index(max(l_Accuracy))]    
    
        
    # #Run with best settings
    temp_mlp = mlp(data_object, convergence, n_epoch) #Initalize MLP
    temp_mlp.initalizeNetwork(n_hidden) #Initalize the Base Network
    print("FINAL EVALUATION WITH BEST SETTINGS")
    print("Convergence Rate: ", convergence)
    print("Number of Hidden Layers: ", n_hidden)
    temp_mlp.evaluate() #Run The Algorithm


# ----
# SIMPLE RUN OF MLP
# ---- 
def run_mlp_simple(data_object, n_hidden, l_rate, n_epoch): 
    temp_mlp = mlp(data_object, l_rate, n_epoch) #Initalize MLP
    temp_mlp.initalizeNetwork(n_hidden)
    temp_mlp.evaluate()
    