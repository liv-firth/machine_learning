# -*- coding: utf-8 -*-
"""
CSCI 447 - Machine Learning 
Project 2

Data Set Class File and Related Functions
"""

# ----
# Dataset class and creation function
# ----
class data_set:
    # Initalize Class Variables
    def __init__(self, dataArr, numAttr, numObsv, classArr):
        self.dataArr = dataArr
        self.numAttr = numAttr
        self.numObsv = numObsv
        self.classArr = classArr
  
def create_data_set(filename):
    dataArr = pd.read_csv(filename) #Read CSV File into pandas data frame
    numObsv = len(dataArr) # Grab Length of data frame
    numAttr = len(dataArr.columns) - 1 #
    classArr = pd.unique(dataArr.iloc[:, numAttr])

    temp_test_set = data_set(dataArr, numAttr, numObsv, classArr)
    return(temp_test_set)
    

def tenFold(datas):   
    print("--- Ten Fold Cross Validation ---")