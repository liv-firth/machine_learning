# -*- coding: utf-8 -*-
"""
CSCI 447 - Machine Learning 
Project 2

Data Set Class File and Related Functions
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
            # FUNCTION TO CREATE TRAIN AND TEST SETS FOR 10 FOLDS
            # FUNCTION TO CREATE A TUNING SET
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
    # FUNCTION TO INTERNALLY CREATE A TEN FOLD TEST AND TRAIN ARRAYS
    # ----

    # note - stratification not necessarry for regression data sets 

    def make10Fold(self):
        ## Find int for 10% of Rows
        tenPer = int(self.numObsv*0.1)
        
        df = self.dataArr #define data frame as data array
        df = df.sample(frac=1) #shuffle data frame rows
        
        ## Create 10 segments of data array
        n = 0 #Define / Initalize a Row iterative
        tenDFList = [] #Create empty list to append each data frame into
        for i in range (9): #Run nine times
            m = n + tenPer #find final row to grab into data frame
            tempdf = df.iloc[n:m] #Grab Rows within n-m range
            n = m + 1 #update n to equal end row plus one
            tenDFList.append(tempdf) #Append list with new temp df
        tenDFList.append(df.iloc[n:self.numObsv-1]) #Append data frame list with final dataframe
        
        ## Create Train and Test Folds
        train = [] #Blank List for Training
        test = [] #Blank List for Testing
        
        for x in range(10): #For all 10 datasets
            tempList = copy.deepcopy(tenDFList) #Create a temporary copy of the tenDFList to reference
            test.append(tempList[x]) #Append Test Array with data frame at x in list
            del tempList[x] #Delete test data frame from list
            train.append(pd.concat(tempList)) #Append train list with the remaining dataframes in the list
        
        self.trainArr = train
        self.testArr = test
        print("--- 10 FOLD TEST AND TRAIN SETS CREATED ---")
        
    # ----
    # FUNCTION TO INTERNALLY CREATE A TEN FOLD TEST AND TRAIN ARRAYS
    # ----
    def makeTuneSet(self):
        tenPer = int(self.numObsv*0.1)
        
        df = self.dataArr #define data frame as data array
        df = df.sample(frac=1) #shuffle data frame rows
        
        self.tuneArr = df.head(tenPer) #grab top 10% of rows and assign as a tuning set
        tuneDataRemoved = df.iloc[tenPer:self.numObsv-1] #Create separate data set that has the tuning set removed
        self.dataArr = tuneDataRemoved #Reassign base data set to the new base data with the tuning set remvoed
        
    
    # ----
    # FUNCTION TO PICK K MEDIODS RANDOMLY AND REMOVE FROM DATASET
    # ----
    def makeMediodsCentroids(self, k):
        print("Make Mediods")
        #Shuffle the dataset
        df = self.dataArr #define data frame as data array
        df = df.sample(frac=1) #shuffle the dataset
        
        #Grab Medoids from top k rows of shuffled dataset
        mediodsArray = []
        for i in range(k):
            mediodsArray.append(df.iloc[0]) #grab the top row from the shuffled dataframe
            df.drop(df.index[0]) #drop the row from the current dataframe
        
        self.dataArr = df #Update the base data array with modified df
        self.mediods = pd.concat(mediodsArray)
        
        #Add Centroids to centroid Array
        centroidsArray = [] #Make blank centroids array to append to 
        for i in range(k):
            tempcentroidRow = mediodsArray[i]
            tempcentroidRow['Centroid'] = tempCentroidRow.iloc[[0]].index
            print(tempcentroidRow)
            centroidsArray.append(tempcentroidRow)
        self.centroids = pd.concat(centroidsArray)
        print(self.mediods)

        
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

    #create tuning set 
    #remove obs used for tuning 
    temp_test_set = data_set(dataArr, numAttr, numObsv, classArr, regression) #Create test set object
    temp_test_set.makeTuneSet() #Make and Assign Tuning Set
    temp_test_set.make10Fold() #Make 10 Fold Test and Train set arrays
    return(temp_test_set)
  