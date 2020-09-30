# -*- coding: utf-8 -*-
"""
CSCI 447 - Machine Learning
Project Two

@author: Claire Richards, Olivia Firth
"""
# ----
# IMPORT FILES AND PACKAGES
# ----

import pandas as pd
from math import sqrt

import dataset_class
import k_nearest_neighbor
import edited_knn
import partitioning_knn
  
# ----
#  BUILD MAIN FUNCTION
# ----
def main():
    filenames = ["Datasets/abalone.csv", "Datasets/forestfires.csv", "Datasets/glass.csv", "Datasets/house-votes-84-fixed.csv", "Datasets/machine.csv", "Datasets/segmentation.csv"]

    gla_data = create_data_set(filenames[2], False) #Import Glass Dataset
    hou_data = create_data_set(filenames[3], False) #Import House Vote Dataset
    seg_data = create_data_set(filenames[5], False) #Import Image Segmentation Dataset
    aba_data = create_data_set(filenames[0], True) #Import Abalone Dataset 
    mac_data = create_data_set(filenames[4], True) #Import Computer Hardware / Machine Dataset
    for_data = create_data_set(filenames[1], True) #Import Forest Fire Dataset
    print("All Dataset Objects Created")
    
    gla_knn = k_near_neighbor(3, gla_data)
    
    
  
# ----
#  RUN MAIN FUNCTION
# ----   
main()
    
