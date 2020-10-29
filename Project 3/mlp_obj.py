# -*- coding: utf-8 -*-
"""
CSCI 447 - Machine Learning
Project Three

MLP Object Class

@author: Claire Richards, Olivia Firth, Hannah Cebulla
"""

# IMPORT THE FOLLOWING PACKAGES AND FILES
import copy
import pandas as pd 
from random import seed
from random import random

import dataset_obj

# ----
# MLP OBJECT CLASS
# ----
class mlp:
    # -----------------------------------------
    # ORDER OF FUNCTIONS WITHIN THE CLASS 
        # UNIVERSAL INTERNAL FUNCTIONS
            # INITALIZER FOR MLP OBJECT
            # INITALIZE / BUILD BASE NETWORK
            # FUNCTION TO RUN THE MLP
    # FUNCTIONS IN THE DOCUMENT, OUTSIDE THE CLASS
        # ##
    # -----------------------------------------

    # ----------------------------------------- #
    # ------ UNIVERSL INTERNAL FUNCTIONS ------ #  
    # ----------------------------------------- #
    
    # ----
    # INITALIZER FUNCTION
    # ----
    def __init__(self, data_object):
        self.dataset = data_object
        self.isRegression = data_object.regression #Indicates if dataset being imported into
    
    # ----
    # BUILD BASE NETWORK
    # ----   
    def initalizeNetwork(self, n_hidden, n_outputs):
        print("Initalize Network")
        n_inputs = self.dataset.numAttr
        network = list()
        hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
        network.append(hidden_layer) #Append Hidden Layer to the Network
        output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
        network.append(output_layer) #Append Output Layer to Append List
        
        self.network = network #Create and Add Network to the MLP Object
    
    # ----
    # ACTIVATE NURONS
    # ----         
    def activate(self, weights, inputs):
        activation = weights[-1]
        for i in range(len(weights)-1):
            activation += weights[i] * inputs[i]
        return(activation)
    
    # ----
    # TRANSFER NUERON ACTIVATION FOR OUTPUT NURONS
    # ----
    def transfer(activation):
        return(1.0 / (1.0 + exp(-activation)))
    
    # ----
    # FORWARD PROPOGATE INPUT TO A NETWORK OUTPUT
    # ----
    def forwardPropogate(self, row):
        inputs = row #assign inputs as a copy of row
        for layer in self.network:
            new_inputs = [] #Blank list of imputs to append to
                for neuron in layer:
                    activation = activate(neuron['weights'], inputs)
                    neuron['output'] = transfer(activation)
                    new_inputs.append(neuron['output'])
                inputs = new_inputs
        return(inputs)
    
    def transfer_derivative(self, output):
        return(output*(1.0-output))
    
    def backward_propogate_error(self, network, expected):
        for i in reversed(range(len(network))):
            layer = network[i]
            errors = list()
            if i != len(network)-1:
                for j in range(len(layer)):
                    error = 0.0
                    for neuron in network[i+1]
        
    # ----
    # RUN FUNCTION
    # ----
    def run(self):
        print("MLP: Run")

# ----------------------------------------- #
# ------ FUNCTIONS OUTSIDE THE CLASS ------ #  
# ----------------------------------------- #   
        
# ----
# DEFINE TO CREATE, TRAIN, AND RUN THE MLP
# ---- 
def run_mlp(data_object, n_inputs, n_hidden, n_outputs):
    temp_mlp = mlp(data_object) #Initalize MLP
    temp_mlp.initalizeNetwork(n_hidden, n_outputs) #Initalize the Base Network
    