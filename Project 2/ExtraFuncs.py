# -*- coding: utf-8 -*-
"""
CSCI 447 - Machine Learning 
Project 2

Extra Functions Not Attatched to a Class
"""
## IMPORT THE FOLLOWING PACKAGES
import pandas as pd
from math import sqrt
# -----------------------------------------
# ORDER OF FUNCTIONS WITHIN THE FILE
    # KNN REFERENCE FUNCTIONS
        # EUCLIDEAN DISTANCE FUNCTION
    # LOSS FUNCTIONS
        # 0/1 LOSS
        # PRECISION
# -----------------------------------------

# ----------------------------------------- #
# -------- KNN REFERENCE FUNCTIONS -------- #  
# ----------------------------------------- #

# ----
# FUNCTION TO FIND THE EUCLIDEAN DISTANCE BETWEEN ALL VALUES BETWEEN TWO ROWS 
#   Used in knn class functions
# ---- 
def euclidean_distance(row1, row2, numAttr):
    distance = 0.0
    row1Val = row1.values.tolist()
    row2Val = row2.values.tolist()
    for i in range(numAttr):
        distance += (row1Val[0][i]-row2Val[0][i])**2
    return(sqrt(distance))
 
# ----------------------------------------- #
# ------------ LOSS FUNCTIONS ------------- #  
# ----------------------------------------- #
    
# ----
# LOSS FUNCTION: 0/1 LOSS
#   Used in main to find accuracy of knn class functions
# ---- 
def zeroOneLoss(dataFrame):
    is_correct = dataFrame['Correct'] == True
    correct_dataFrame = dataFrame[is_correct]
    
    numCorrect = len(correct_dataFrame) #Count number correct (in filtered dataframe)
    numTotal = len(dataFrame) #Count total number of rows
    
    loss = numCorrect / numTotal #Find loss, i.e. the percent correct
    print("0/1 Loss", loss)
    return(loss)
    
# ----
# LOSS FUNCTION: PRECISION
#   Used in main to find accuracy of knn class functions
# ---- 
def precisionLoss(dataFrame):
    classArr = pd.unique(dataFrame['Class']) #Find Class Values and create a list to reference
    
    precisionArray = [] #Create blank list to write to with precision values
    for n in range(len(classArr)): #For every class in the class List
        print(classArr[n])
        is_class = dataFrame['Class'] == classArr[n] #Determine if the rows match the current class
        cArr = dataFrame[is_class] #Filter for rows that match the current class
        numTotal = len(cArr) #Count the number of rows to determine the max correct value
        
        is_correct = cArr['Correct'] == True #Find all rows with correct classes assigned
        correctArr = cArr[is_correct] #Filter for rows that have been classified correctly
        numCorrect = len(correctArr) #Count the number of rows to determine how many rows were identified correctly
        
        precision = numCorrect / numTotal #Determine Precision for that class
        precisionArray.append([classArr[n], precision]) #Add the value to the precision list for reference
        print("Class: ",classArr[n],"\t Precision: ",precision)
    return(precisionArray)
        
