# -*- coding: utf-8 -*-
"""
CSCI 447 - Machine Learning 
Project 2

Data Set Class File and Related Functions
"""
# IMPORT THE FOLLOWING PACKAGES
import copy

# ----
# Dataset class and creation function
# ----
class data_set:
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
            train.append(tempList) #Append train list with the remaining dataframes in the list
        
        self.trainArr = train
        self.testArr = test
        print("--- 10 FOLD TEST AND TRAIN SETS CREATED ---")
        
# ----
# DEFINE FUNCTION TO READ CSV AND CREATE A DATA SET OBJECT (WITH TEST AND TRAINING 10 FOLD CREATED)
# ----  
def create_data_set(filename, regression):
    dataArr = pd.read_csv(filename) #Read CSV File into pandas data frame
    numObsv = len(dataArr) # Grab Length of data frame
    numAttr = len(dataArr.columns) - 1 #
    classArr = pd.unique(dataArr.iloc[:, numAttr])

    temp_test_set = data_set(dataArr, numAttr, numObsv, classArr, regression) #Create test set object
    temp_test_set.make10Fold() #Make 10 Fold Test and Train set arrays
    return(temp_test_set)
  