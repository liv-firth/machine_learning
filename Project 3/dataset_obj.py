# -*- coding: utf-8 -*-
"""
CSCI 447 - Machine Learning
Project Three

dataset object creation

@author: Claire Richards, Olivia Firth, Hannah C
"""

# IMPORT THE FOLLOWING PACKAGES
import copy
import pandas as pd 

# ----
# Dataset class and creation function
# ----
class data_set:
    # -----------------------------------------
    # ORDER OF FUNCTIONS WITHIN THE CLASS 
        # UNIVERSAL INTERNAL FUNCTIONS
            # INITALIZER FOR DATA OBJECT
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
        

# ----------------------------------------- #
# ------ FUNCTIONS OUTSIDE THE CLASS ------ #  
# ----------------------------------------- #   
        
# ----
# DEFINE FUNCTION TO READ CSV AND CREATE A DATA SET OBJECT (WITH TEST AND TRAINING 10 FOLD CREATED)
# ----  
def create_data_set(filename, regression):
    dataArr = pd.read_csv(filename) #Read CSV File into pandas data frame
    numObsv = len(dataArr) # Grab Length of data frame
    numAttr = len(dataArr.columns) - 1 #
    classArr = pd.unique(dataArr.iloc[:, numAttr])

    temp_test_set = data_set(dataArr, numAttr, numObsv, classArr, regression) #Create test set object
    return(temp_test_set)