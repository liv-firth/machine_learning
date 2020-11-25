# -*- coding: utf-8 -*-
"""
CSCI 447 - Machine Learning
Project Three

Genetic Algorithm Class

@author: Claire Richards, Olivia Firth, Hannah Cebulla
"""

# IMPORT THE FOLLOWING PACKAGES AND FILES
import copy
import numpy as np
import pandas as pd 
from random import seed
from random import random
from math import exp

import dataset_obj
from misc import logRessObj
from mlp_obj import mlp

# ----
# MLP OBJECT CLASS
# ----
class ga:
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
    def __init__(self, mlp_object, size, n_parents):
        self.dataset = mlp_object.dataset #Grab dataset from MLP object
        self.regression = mlp_object.isRegression #Grab regression boolean from MLP object
        self.mutation_rate = mlp_object.l_rate #Grab learning rate from mlp 
        self.n_gen = mlp_object.n_epoch
        self.network = mlp_object.network
        self.size = int(mlp_object.dataset.numObsv/10)
        self.n_parents = n_parents
        self.n_feat = mlp_object.dataset.numClass
        self.logmodel = logRessObj(self.dataset).logRess

    
        # ----------------------------------------- #
        # --- BUILD BASE NETWORK AND ACTIVATION --- #  
        # ----------------------------------------- #
    # ----
    # INITALIZE POPULATION
    # ----
    def init_pop(self, size, n_feat):
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
    def fitness_score(self,population, X_train, X_test, y_train, y_test):
        scores = []
        for chromosome in range(self.dataset.numAttr):
            self.logmodel.fit(X_train[:,chromosome], y_train)
            predictions = self.logmodel.predict(X_test[:,chromosome])
            scores.append(self.accuracy_score(y_test,predictions))
        scores, population = np.array(scores), np.array(population) 
        inds = np.argsort(scores)
        return list(scores[inds][::-1]), list(population[inds,:][::-1])
    
    def selection(self, pop_after_fit, n_parents):
        population_nextgen = []
        for i in range(n_parents):
            population_nextgen.append(pop_after_fit[i])
        return population_nextgen
    
    def crossover(self, pop_after_sel):
        population_nextgen=pop_after_sel
        for i in range(len(pop_after_sel)):
            child=pop_after_sel[i]
            child[3:7]=pop_after_sel[(i+1)%len(pop_after_sel)][3:7]
            population_nextgen.append(child)
        return population_nextgen
    
    def mutation(self, pop_after_cross,mutation_rate):
        population_nextgen = []
        for i in range(0,len(pop_after_cross)):
            chromosome = pop_after_cross[i]
            for j in range(len(chromosome)):
                if random.random() < mutation_rate:
                    chromosome[j]= not chromosome[j]
            population_nextgen.append(chromosome)
        #print(population_nextgen)
        return population_nextgen

    
    def generations(self, X_train, X_test, y_train, y_test):
        best_chromo= []
        best_score= []
        population_nextgen = self.init_pop(self.size,self.n_feat)
        for i in range(self.n_gen):
            scores, pop_after_fit = self.fitness_score(population_nextgen, X_train, X_test, y_train, y_test)
            print(scores[:2])
            pop_after_sel = self.selection(pop_after_fit,self.n_parents)
            pop_after_cross = self.crossover(pop_after_sel)
            population_nextgen = self.mutation(pop_after_cross,self.mutation_rate)
            best_chromo.append(pop_after_fit[0])
            best_score.append(scores[0])
        return best_chromo,best_score    

            
                

# ----------------------------------------- #
# ------ FUNCTIONS OUTSIDE THE CLASS ------ #  
# ----------------------------------------- #   
        
def run_ga(data_object, n_hidden, l_rate, n_epoch, size, n_parents): 
    print("--- RUN GENETIC ALGORITHM ---")
    temp_mlp = mlp(data_object, l_rate, n_epoch) #Initalize MLP object
    temp_mlp.initalizeNetwork(n_hidden)
    #temp_mlp.evaluate()
    
    temp_ga = ga(temp_mlp, size, n_parents)
    numCorr = 0
    
    for i in range(10):
        temp_train = temp_ga.dataset.tenTrainArr[i]
        print("Temp Training Set")
        print(temp_train)
        print("Temp Testing Set")
        temp_test = temp_ga.dataset.tenTestArr[i]
        print(temp_test)
        
        X_train = temp_train[:,:-1] #Separate predictors and class, train
        print(X_train)
        y_train = temp_train[:,:-1] #Separate predictors and class, train
        
        X_test = temp_test[:, -1] #Separate predictors and class, test
        y_test = temp_test[:, -1] #Separate predictors and class, test
        
        
        chromo,score= temp_ga.generations(X_train,X_test,y_train,y_test)
        temp_ga.logmodel.fit(X_train[:,chromo[-1]],y_train)
        predictions = temp_ga.logmodel.predict(X_test[:,chromo[-1]])
        for k in range(len(predictions)):
            if predictions[k] == y_test[k]:
                numCorr += 1
    
    accuracy = numCorr / temp_ga.dataset.numObsv
    print("0/1 Loss Score: "+str(accuracy))
        
        

    