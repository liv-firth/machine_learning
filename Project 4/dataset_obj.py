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
            # BUILDER FOR TRAINING AND TESTING OBJECTS (Ten Folds)
    # FUNCTIONS IN THE DOCUMENT, OUTSIDE THE CLASS
        # CREATE DATA OBJECT: BUILDS DATA SET OBJECT FROM A FILE NAME
    # -----------------------------------------

    # ----------------------------------------- #
    # ------ UNIVERSL INTERNAL FUNCTIONS ------ #  
    # ----------------------------------------- #
    
    # ----
    # INITALIZER FUNCTION
    # ----
    def __init__(self, dataArr, numAttr, numObsv, classArr, regression, numClass):
        self.dataArr = dataArr
        self.numAttr = numAttr
        self.numObsv = numObsv
        self.classArr = classArr
        self.regression = regression
        self.numClass = numClass
    
    # ----
    # MAKE TRAINING AND TESTING SET (10 Fold)
    # ----
    def makeTrainTest(self):
        #print("Making Training and Test Sets: 10 Fold")
        tenPer = int(self.numObsv) #Find value for 10% of dataset
        
        df = self.dataArr #define data frame as data array
        
        ## Create 10 segments of data array
        n = 0 #Define / Initalize a Row iterative
        tenDFList = [] #Create empty list to append each data frame into
        for i in range (9): #Run nine times
            #print("Fold Number: ",i+1)
            m = n + tenPer #find final row to grab into data frame
            tempdf = df[n:m,:] #Grab Rows within n-m range
            n = m + 1 #update n to equal end row plus one
            tenDFList.append(tempdf) #Append list with new temp df
        tenDFList.append(df[n:self.numObsv-1,:]) #Append data frame list with final dataframe
        
        ## Create Train and Test Folds
        train = [] #Blank List for Training
        test = [] #Blank List for Testing
        
        for x in range(10): #For all 10 datasets
            #print("Making Training and Testing Set -",x)
            tempList = copy.deepcopy(tenDFList) #Create a temporary copy of the tenDFList to reference
            test.append(tempList[x]) #Append Test Array with data frame at x in list
            del tempList[x] #Delete test data frame from list
            train.append(np.concatenate(tempList)) #Append train list with the remaining dataframes in the list
        
        self.tenTrainArr = train
        self.tenTestArr = test
        #print("--- 10 FOLD TEST AND TRAIN SETS CREATED ---")        

# ----------------------------------------- #
# ------ FUNCTIONS OUTSIDE THE CLASS ------ #  
# ----------------------------------------- #   
        
# ----
# DEFINE FUNCTION TO READ CSV AND CREATE A DATA SET OBJECT (WITH TEST AND TRAINING 10 FOLD CREATED)
# ----  
def create_data_set(filename, regression):
    ## Basic Data Reading
    dataArr = np.genfromtxt(filename, delimiter=',') #Read CSV File into Numpy Array
    #print(dataArr)
    numObsv, numAttr = dataArr.shape #Grab number of rows and number of columns
    numAttr = numAttr - 1 # Subtract Class Column
    classArr = np.unique(dataArr[:,numAttr]).tolist() #Pull Unique Values from Class Column
    numClass = len(classArr)
    
    temp_test_set = data_set(dataArr, numAttr, numObsv, classArr, regression, numClass) #Create test set object
    
    ## Build Additional data set variables
    temp_test_set.makeTrainTest() #Build Training and Test Objects, Build 10-cross folds
    return(temp_test_set)