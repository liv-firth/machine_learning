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

# ----
# DEFINE TEN FOLD FUNCTION
# ----

 
# ----
#  DEFINE CLASSIFICATION FUNCTIONS
# ----       


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
    
