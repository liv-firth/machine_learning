# -*- coding: utf-8 -*-
"""
CSCI 447 - Machine Learning
Project Two

@author: Claire Richards, Olivia Firth
"""

# Include the Following Packages
import pandas as pd
from math import sqrt

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
 
    
# ----
# DEFINE TEN FOLD FUNCTION
# ----
def tenFold(datas):   
    print("--- Ten Fold Cross Validation ---")
 
# ----
#  DEFINE CLASSIFICATION FUNCTIONS
# ----       
def k_near_neighbor(datas):
    print("--- K Nearest Neighbor ---")
    df = datas.dataArr
    row0 = df.iloc[[0]]
    
    for i in range(datas.numObsv):
        distance = euclidean_distance(row0, df.iloc[i])
        print(distance)
    
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += (row1[i]-row2[i])**2
    return(sqrt(distance))

def edited_k(datas):
    print("--- Edited K Nearest Neighbor ---")

def partitioning_k(datas):
    print("--- Partitioning K ---")
    
# ----
#  BUILD MAIN FUNCTION
# ----
def main():
    filenames = ["abalone.csv", "forestfires.csv", "glass.csv", "house-votes-84-fixed.csv", "machine.csv", "segmentation.csv"]
    
    aba_data = create_data_set(filenames[0])  
    for_data = create_data_set(filenames[1])
    gla_data = create_data_set(filenames[2])
    hou_data = create_data_set(filenames[3])
    mac_data = create_data_set(filenames[4])
    seg_data = create_data_set(filenames[5])
    print("All Dataset Objects Created")
    
    k_near_neighbor(for_data)
  
# ----
#  RUN MAIN FUNCTION
# ----   
main()
    
