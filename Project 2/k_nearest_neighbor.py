# -*- coding: utf-8 -*-
"""
CSCI 447 - Machine Learning 
Project 2

K-Nearest Neighbor Implementation
"""
## IMPORT THE FOLLOWING PACKAGES
import pandas as pd
import math as m

## IMPORT DATA SET CLASS FILE
import dataset_class


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