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

#    gla_data = create_data_set(filenames[2], False) #Import Glass Dataset
#    hou_data = create_data_set(filenames[3], False) #Import House Vote Dataset
    seg_data = create_data_set(filenames[5], False) #Import Image Segmentation Dataset
    aba_data = create_data_set(filenames[0], True) #Import Abalone Dataset 
#    mac_data = create_data_set(filenames[4], True) #Import Computer Hardware / Machine Dataset
#    for_data = create_data_set(filenames[1], True) #Import Forest Fire Dataset
    print("All Dataset Objects Created")
    
#    seg_knn = k_near_neighbor(10, seg_data)
#    zeroOneLoss(seg_knn.run_knn())
#    zeroOneLoss(seg_knn.run_edited_knn())
#    zeroOneLoss(seg_knn.run_condensed_knn())
    
    aba_knn = k_near_neighbor(10, aba_data)
    zeroOneLoss(aba_knn.run_knn())
    zeroOneLoss(aba_knn.run_edited_knn())
    zeroOneLoss(aba_knn.run_condensed_knn())
    
    
#    gla_knn = k_near_neighbor(9, gla_data)
#    gla_k = gla_knn.tune_k_set()
#    for k in gla_k:
#        print("GLASS DATA - K = ",k)
#        gla_knn = k_near_neighbor(k, gla_data)
#        precisionLoss(gla_knn.run_knn())
#        precisionLoss(gla_knn.run_edited_knn())
#        precisionLoss(gla_knn.run_condensed_knn())
     
#    hou_knn = k_near_neighbor(9, hou_data)
#    for k in hou_k:
#        print("GLASS DATA - K = ",k)
#        hou_knn = k_near_neighbor(k, hou_data)
#        precisionLoss(hou_knn.run_knn())
#        precisionLoss(hou_knn.run_edited_knn())
#        precisionLoss(hou_knn.run_condensed_knn())  

#    seg_knn = k_near_neighbor(9, seg_data)
#    for k in hou_k:
#        print("SEGMENTATION DATA - K = ",k)
#        seg_knn = k_near_neighbor(k, seg_data)
#        precisionLoss(seg_knn.run_knn())
#        precisionLoss(seg_knn.run_edited_knn())
#        precisionLoss(seg_knn.run_condensed_knn()) 
    
#    aba_knn = k_near_neighbor(9, aba_data)
#    aba_k = aba_knn.tune_k_set()
#    print(aba_k)
##    for k in aba_k:
##        print("Abalone Data - K =,", k)
##        aba_knn = k_near_neighbor(k, aba_data)
##        zeroOneLoss(aba_knn.run_knn())
##        zeroOneLoss(aba_knn.run_edited_knn())
##        zeroOneLoss(aba_knn.run_condensed_knn())
#    
#    mac_knn = k_near_neighbor(9, mac_data)
#    mac_k = mac_knn.tune_k_set()
#    print(mac_k)
#    for k in mac_k:
#        print("Machine Data - K =,", k)
#        mac_knn = k_near_neighbor(k, mac_data)
#        zeroOneLoss(mac_knn.run_knn())
#        zeroOneLoss(mac_knn.run_edited_knn())
#        zeroOneLoss(mac_knn.run_condensed_knn())
#    
#    for_knn = k_near_neighbor(9, for_data)
#    for_k = for_knn.tune_k_set()
#    print(for_k)
#    for k in for_k:
#        print("Forest Fire Data - K =,", k)
#        for_knn = k_near_neighbor(k, for_data)
#        zeroOneLoss(for_knn.run_knn())
#        zeroOneLoss(for_knn.run_edited_knn())
#        zeroOneLoss(for_knn.run_condensed_knn())

    
    
    
  
# ----
#  RUN MAIN FUNCTION
# ----   
main()
    
