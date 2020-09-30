# -*- coding: utf-8 -*-
"""
CSCI 447 - Machine Learning 
Project 2

K-Nearest Neighbor Implementation
"""
## IMPORT THE FOLLOWING PACKAGES
import pandas as pd
import math as m
import copy

## IMPORT DATA SET CLASS FILE
import dataset_class


class k_near_neighbor:
    def __init__(self, k, data_obj):
        self.k = k
        self.regression = data_obj.regression
        self.trainArr = data_obj.trainArr
        self.testArr = data_obj.testArr
        
    
    def fit(self, train, test):
        self.train = train
        self.test = test
        
    def predict(self, testRow):
        print("--- Predict Class by KNN ---")
        distances = []
        # Calculate Distances For All Neighbors
        for i in range(len(self.train)): #For all training set values
            tempDist = euclidean_distance(testRow, train.iloc) #Return euclidean distance
            distances.append(tempDist) #Append distances list with temp distance calculated
        print(distances)
        
        # Sort dataset by ascending distances
        newTrain = copy.deepcopy(train) #Create deepcopy of train (not connected with original)
        newTrain['Distances'] = distances #Add Distances column to data frame
        newTrain.sort_values(by = 'Distances', ascending = True) #Order by distances column
        
        # Grab top k neighbors
        topNeighbors = head(self.k) #Grab top k rows
        
        # Predict Class
        topNeighbors['Class'].value_counts()

    
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += (row1[i]-row2[i])**2
    return(sqrt(distance))