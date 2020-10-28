# -*- coding: utf-8 -*-
"""
CSCI 447 - Machine Learning
Project Three

dataset object creation

@author: Claire Richards, Olivia Firth, Hannah Cebulla
"""

# IMPORT THE FOLLOWING PACKAGES
import copy
import pandas as pd 
import numpy as np

# ----
# Dataset class and creation function
# ----
class data_set:
    # -----------------------------------------
    # ORDER OF FUNCTIONS WITHIN THE CLASS 
        # UNIVERSAL INTERNAL FUNCTIONS
            # INITALIZER FOR DATA OBJECT
            # BUILDER FOR TRAINING AND TESTING OBJECTS
    # FUNCTIONS IN THE DOCUMENT, OUTSIDE THE CLASS
        # CREATE DATA OBJECT: BUILDS DATA SET OBJECT FROM A FILE NAME
    # -----------------------------------------

    # ----------------------------------------- #
    # ------ UNIVERSL INTERNAL FUNCTIONS ------ #  
    # ----------------------------------------- #
    
    # ----
    # INITALIZER FUNCTION
    # ----
    def __init__(self, dataArr, numAttr, numObsv, classArr, regression):
        self.dataArr = dataArr
        self.numAttr = numAttr
        self.numObsv = numObsv
        self.classArr = classArr
        self.regression = regression
    
    # ----
    # MAKE TRAINING AND TESTING SET (10 Fold)
    # ----
    def makeTrainTest(self):
        print("Making Training and Test Sets: 10 Fold")
        

# ----------------------------------------- #
# ------ FUNCTIONS OUTSIDE THE CLASS ------ #  
# ----------------------------------------- #   
        
# ----
# DEFINE FUNCTION TO READ CSV AND CREATE A DATA SET OBJECT (WITH TEST AND TRAINING 10 FOLD CREATED)
# ----  
def create_data_set(filename, regression):
    ## Basic Data Reading
    dataArr = np.genfromtxt(filename, delimiter=',') #Read CSV File into Numpy Array
    numObsv, numAttr = dataArr.shape #Grab number of rows and number of columns
    numAttr = numAttr - 1 # Subtract Class Column
    classArr = np.unique(dataArr[:,numAttr]) #Pull Unique Values from Class Column

    temp_test_set = data_set(dataArr, numAttr, numObsv, classArr, regression) #Create test set object
    
    ## Build Additional data set variables
    temp_test_set.makeTrainTest() #Build Training and Test Objects, Build 10-cross folds
    return(temp_test_set)