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
import math
#from math import sqrt


import dataset_class
from dataset_class import create_data_set
import k_nearest_neighbor
from k_nearest_neighbor import k_near_neighbor
from ExtraFuncs import zeroOneLoss, precisionLoss

  
# ----
#  BUILD MAIN FUNCTION
# ----
def main():
    filenames = ["abalone.csv", "forestfires.csv", "glass.csv", "house-votes-84-fixed.csv", "machine.csv", "segmentation.csv"]

    gla_data = create_data_set(filenames[2], False) #Import Glass Dataset
    hou_data = create_data_set(filenames[3], False) #Import House Vote Dataset
    seg_data = create_data_set(filenames[5], False) #Import Image Segmentation Dataset
    aba_data = create_data_set(filenames[0], True) #Import Abalone Dataset 
    mac_data = create_data_set(filenames[4], True) #Import Computer Hardware / Machine Dataset
    for_data = create_data_set(filenames[1], True) #Import Forest Fire Dataset
    print("All Dataset Objects Created")
    
#    gla_knn = k_near_neighbor(9, gla_data)
#    gla_knn.tune()
#    precisionLoss(gla_knn.run_knn())
    
#    hou_knn = k_near_neighbor(5, hou_data)
#    hou_knn.tune()
#    precisionLoss(hou_knn.run_knn())
    
    seg_knn = k_near_neighbor(15, seg_data)
    #seg_knn.tune()
    precisionLoss(seg_knn.run_knn())
    precisionLoss(seg_knn.run_edited_knn())
    precisionLoss(seg_knn.run_condensed_knn())
    
    
    
  
# ----
#  RUN MAIN FUNCTION
# ----   
main()
    
