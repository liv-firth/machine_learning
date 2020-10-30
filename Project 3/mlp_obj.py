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
            # EVALUATE THE NETWORK
    # FUNCTIONS IN THE DOCUMENT, OUTSIDE THE CLASS
        # FUNCTION TO BUILD, TRAIN CONVERGENCE AND NUMBER OF HIDDEN LAYERS, AND RUN THE MLP
        # SIMPLIFIED RUN - NO TUNING
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
    # BUILD BASE NETWORK
    # ----   
    def initalizeNetwork(self, n_hidden):
        print("Initalize Network")
        n_inputs = self.dataset.numAttr #Number of inputs is equal to the number of attributes
        if(self.dataset.regression): n_outputs = 1 #If regressive, number of outputs will be one
        else: n_outputs = self.dataset.numClass #Otherwise number of outputs equals the number of classes
        
        network = list() #Define Blank network
        self.hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)] #Create Random Weights for each hidden layer
        network.append(self.hidden_layer) #Append Hidden Layer to the Network
        self.output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)] #Create weights for each output layer
        network.append(self.output_layer) #Append Output Layer to Append List
        
        self.network = network #Create and Add Network to the MLP Object
    
    # ----
    # ACTIVATE NURONS (General, not divided by Regression and Classifcation, see Transfer)
    # ----         
    def activate(self, weights, inputs): 
        activation = weights[-1] #Grab output weights
        for i in range(len(weights)-1): #For all weights, minus one
            activation += weights[i] * inputs[i] #General activation, add weights multiplied by inputs
        return(activation)
    
    # ----
    # TRANSFER NUERON ACTIVATION FOR OUTPUT NURONS (Activation)
    # ----
    def transfer(self, activation):
        if(self.dataset.regression): #If Regressive
            print("REGRESSION ACTIVATION")
            return(sum(self.hidden_layer['weights'])*self.c) #Regressive Activation
        else: #If not regressive
            print("CLASSIFICATION ACTIVATION: SIGMODAL")
            print("Activation: ", 1.0 / (1.0 + exp(-activation)))
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
    def transfer_derivative(self, output): #For back propogation of error
        return(output*(1.0-output))
    
    # ----
    # BACK PROPOGATE ERROR
    # ----
    def backward_propogate_error(self, expected):
        print("Back Propogate Error")
        for i in reversed(range(len(self.network))): #Work from end of network (output)
            layer = self.network[i] #grab a layer from the network
            errors = list() #create blank list to append errors to
            if i != len(self.network)-1:
                for j in range(len(layer)): #for all but final layer (ie input layer)
                    error = 0.0
                    for neuron in self.network[i+1]:
                        error += (neuron['weights'][j]*neuron['delta'])#Find delta, multiply by weights and then add to error
                    errors.append(error)
            else: #For final layer
                for j in range(len(layer)):
                    neuron = layer[j] #set neuron equal to the layer weight
                    errors.append(expected[j] - neuron['output']) #subtract output from expected and append to error list for transfer
            for j in range(len(layer)):
                neuron = layer[j]
                neuron['delta'] = errors[j] * self.transfer_derivative(neuron['output']) #Transfer
                
            #Nothing is returned since actions are taken on the network internally
        
        # ----------------------------------------- #
        # ------ TRAIN THE NETWORK FUNCTIONS ------ #  
        # ----------------------------------------- # 
    
    # ----
    # TRAIN THE NETWORK: UPDATE WEIGHTS
    # ----
    def update_weights(self, network, row, l_rate):
        #print("Weights Updating")
        for i in range(len(network)):
            inputs = row[:-1]
            if i != 0:
                inputs = [neuron['output'] for neuron in network[i - 1]]
            for neuron in network[i]:
                for j in range(len(inputs)):
                    neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
                neuron['weights'][-1] += l_rate * neuron['delta']
                #print("Adjusted Weights: ", neuron['weights'])
     
    # ----
    # TRAIN THE NETWORK
    # ----
    def train_network(self, network, train, l_rate, n_epoch, n_outputs):
        for epoch in range(n_epoch):
            sum_error = 0
            for row in train:
                #print(row)
                outputs = self.forward_propagate(row)
                expected = [0 for i in range(n_outputs)]
                expected[self.dataset.classArr.index(row[-1])] = 1
                sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
                #print("Error: ", sum_error)
                self.backward_propogate_error(expected)
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
        print(row)
        print(outputs)
        return(self.dataset.classArr[outputs.index(max(outputs))]) #Returns top class option
    
    # ----
    # RUN FUNCTION
    # ----
    def evaluate(self):
        #print("MLP: Run")
        
        cList = list() #Blank list to collect correct class
        pList = list() #Blank list to collect predicted class
        correct = list() #Blank list to collect T/F
        for i in range(10): #For Each Fold
            train = self.dataset.tenTrainArr[i] #Grab ith training set
            test = self.dataset.tenTestArr[i] #Grab ith testing set
            
            #print("Train Network: ", i)
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

        #print("ACCURACY OF CLASSIFICATIONS:")
        self.accuracy = sum(correct)/len(correct)
        for c in self.dataset.classArr:
            countTrue = 0
            outOf = 0
            for x in range(len(correct)):
                if cList[x] == c:
                    outOf += 1
                    if correct[x] == True:
                        countTrue += 1
            #print(c,": ",countTrue/outOf)
            
                

# ----------------------------------------- #
# ------ FUNCTIONS OUTSIDE THE CLASS ------ #  
# ----------------------------------------- #   
        
# ----
# DEFINE TO CREATE, TRAIN, AND RUN THE MLP
# ---- 
def run_mlp(data_object, n_hiddenList, l_rate, n_epoch):   
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
    