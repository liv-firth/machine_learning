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
from math import exp

import dataset_obj

# ----
# MLP OBJECT CLASS
# ----
class mlp:
    # -----------------------------------------
    # ORDER OF FUNCTIONS WITHIN THE CLASS 
        # UNIVERSAL INTERNAL FUNCTIONS
            # INITALIZER FOR MLP OBJECT
            # BUILD BASE NETWORK AND ACTIVATION FUNCTIONS
                # INITALIZE NETWORK
                # ACTIVATION
                # TRANSFER ACTIVATION TO OUTPUT
            # FORWARD PROPOGATION 
            # BACK PROPOGATION AND FUNCTIONS
                # TRANSFER DERIVATIVE
                # BACK PROPOGATE ERROR
            # TRAIN NETWORK
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
    def __init__(self, data_object, l_rate, n_epoch):
        self.dataset = data_object
        self.isRegression = data_object.regression #Indicates if dataset being imported into
        self.l_rate = l_rate #Learning Rate is given
        self.n_epoch = n_epoch #Specify Number of Epochs for Training
    
        # ----------------------------------------- #
        # --- BUILD BASE NETWORK AND ACTIVATION --- #  
        # ----------------------------------------- #
    # ----
    # BUILD BASE NETWORK
    # ----   
    def initalizeNetwork(self, n_hidden):
        print("Initalize Network")
        n_inputs = self.dataset.numAttr #Number of inputs is equal to the number of attributes
        if(self.dataset.regression): n_outputs = 1
        else: n_outputs = self.dataset.numClass
        
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
    # TRANSFER NUERON ACTIVATION FOR OUTPUT NURONS (Activation)
    # ----
    def transfer(self, activation):
        if(self.dataset.regression): #If Regressive
            print("Oh shit its regressive")
        else: #If not regressive
            return(1.0 / (1.0 + exp(-activation))) #Sigmodal For Classifcation Functions
    
    # ----
    # FORWARD PROPOGATE INPUT TO A NETWORK OUTPUT
    # ----
    def forward_propagate(self, row):
        inputs = row #assign inputs as a copy of row
        for layer in self.network: #For each layer in the network 
            new_inputs = [] #Blank list of imputs to append to
            for neuron in layer:
                activation = self.activate(neuron['weights'], inputs)
                neuron['output'] = self.transfer(activation)
                new_inputs.append(neuron['output'])
            inputs = new_inputs
        return(inputs)
    
        # ----------------------------------------- #
        # -- BACK PROPOGATION OF ERROR FUNCTION --- #  
        # ----------------------------------------- # 
    # ----
    # BACK PROPOGATE ERROR: TRANSFER DERIVATIVE (REVERSE TRANSFER ACTIVATION)
    # ----
    def transfer_derivative(self, output):
        return(output*(1.0-output))
    
    # ----
    # BACK PROPOGATE ERROR
    # ----
    def backward_propogate_error(self, network, expected):
        for i in reversed(range(len(network))):
            layer = network[i]
            errors = list()
            if i != len(network)-1:
                for j in range(len(layer)):
                    error = 0.0
                    for neuron in network[i+1]:
                        error += (neuron['weights'][j]*neuron['delta'])
                    errors.append(error)
            else:
                for j in range(len(layer)):
                    neuron = layer[j]
                    errors.append(expected[j] - neuron['output'])
            for j in range(len(layer)):
                neuron = layer[j]
                neuron['delta'] = errors[j] * self.transfer_derivative(neuron['output'])
        
        # ----------------------------------------- #
        # ------ TRAIN THE NETWORK FUNCTIONS ------ #  
        # ----------------------------------------- # 
    
    # ----
    # TRAIN THE NETWORK: UPDATE WEIGHTS
    # ----
    def update_weights(self, network, row, l_rate):
        for i in range(len(network)):
            inputs = row[:-1]
            if i != 0:
                inputs = [neuron['output'] for neuron in network[i - 1]]
            for neuron in network[i]:
                for j in range(len(inputs)):
                    neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
                neuron['weights'][-1] += l_rate * neuron['delta']
     
    # ----
    # TRAIN THE NETWORK
    # ----
    def train_network(self, network, train, l_rate, n_epoch, n_outputs):
        for epoch in range(n_epoch):
            sum_error = 0
            for row in train:
                outputs = self.forward_propagate(row)
                expected = [0 for i in range(n_outputs)]
                expected[self.dataset.classArr.index(row[-1])] = 1
                sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
                self.backward_propogate_error(network, expected)
                self.update_weights(network, row, l_rate)
            #print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
    
        
        # ----------------------------------------- #
        # ------ TRAIN THE NETWORK FUNCTIONS ------ #  
        # ----------------------------------------- # 
    # ----
    # PREDICT FUNCTION
    # ----
    def predict(self, row):
        outputs = self.forward_propagate(row)
        print(outputs)
        return(self.dataset.classArr[outputs.index(max(outputs))]) #Returns top class option
    
    # ----
    # RUN FUNCTION
    # ----
    def evaluate(self):
        print("MLP: Run")
        
        cList = list() #Blank list to collect correct class
        pList = list() #Blank list to collect predicted class
        correct = list() #Blank list to collect T/F
        for i in range(10): #For Each Fold
            train = self.dataset.tenTrainArr[i] #Grab ith training set
            test = self.dataset.tenTestArr[i] #Grab ith testing set
            
            print("Train Network: ", i)
            self.train_network(self.network, train, self.l_rate, self.n_epoch, self.dataset.numClass)
            
            numRow, numCol = test.shape #Grab Shape for reference
            for k in range(numRow):
                predicted = self.predict(test[k])
                
                cList.append(test[k,numCol-1])
                pList.append(predicted)
                
                #print(predicted)
                #print(test[k, numCol-1])
                if(predicted == test[k, numCol-1]): 
                    #print("MATCHES")
                    correct.append(True)
                else:
                    #print("NOT CORRECT")
                    correct.append(False)

        print("ACCURACY OF CLASSIFICATIONS:")
        for c in self.dataset.classArr:
            countTrue = 0
            outOf = 0
            for x in range(len(correct)):
                if cList[x] == c:
                    outOf += 1
                    if correct[x] == True:
                        countTrue += 1
            print(c,": ",countTrue/outOf)
            
                

# ----------------------------------------- #
# ------ FUNCTIONS OUTSIDE THE CLASS ------ #  
# ----------------------------------------- #   
        
# ----
# DEFINE TO CREATE, TRAIN, AND RUN THE MLP
# ---- 
def run_mlp(data_object, n_hidden, l_rate, n_epoch):
    temp_mlp = mlp(data_object, l_rate, n_epoch) #Initalize MLP
    temp_mlp.initalizeNetwork(n_hidden) #Initalize the Base Network
    temp_mlp.evaluate() #Run The Algorithm
    