# -*- coding: utf-8 -*-
"""
CSCI 447 - Machine Learning
Project Three

@author: Claire Richards, Olivia Firth, Hannah Cebulla
"""
# ----
# IMPORT FILES AND PACKAGES
# ----
import dataset_obj #Interal File, Data Set Object Class File
from dataset_obj import create_data_set
import mlp_obj


# ----
#  BUILD MAIN FUNCTION
# ----
def main():
    filenames = ["Datasets/breast-cancer-wisconsin.csv", "Datasets/glass.csv", "Datasets/soybean-small - Copy.csv", "Datasets/abalone.csv", "Datasets/machine.csv", "Datasets/forestfires.csv"]

    ## IMPORT CLASSIFICATION DATA SETS: BREAST CANCER, GLASS, SOYBEAN
    brc_data = create_data_set(filenames[0], False)
    gla_data = create_data_set(filenames[1], False)
    soy_data = create_data_set(filenames[2], False)
    
    ## IMPORT REGRESSION DATA SETS: ABALONE, COMPUTER HARDWARE, FOREST FIRES
    aba_data = create_data_set(filenames[3], True)
    mac_data = create_data_set(filenames[4], True)
    fof_data = create_data_set(filenames[5], True)
    
    mlp_obj.run_mlp(brc_data, [0,1,2], [0.1, 0.01, 0.001, 0.0001, 0.00001], 200)
    # mlp_obj.run_mlp(gla_data, [0,1,2], [0.1, 0.01, 0.001, 0.0001, 0.00001], 200)
    # mlp_obj.run_mlp(soy_data, [0,1,2], [0.1, 0.01, 0.001, 0.0001, 0.00001], 200)
    
    #mlp_obj.run_mlp(aba_data, [0,1,2], [0.1, 0.01, 0.001, 0.0001, 0.00001], 200)
    # mlp_obj.run_mlp(mac_data, [0,1,2], [0.1, 0.01, 0.001, 0.0001, 0.00001], 200)
    # mlp_obj.run_mlp(fof_data, [0,1,2], [0.1, 0.01, 0.001, 0.0001, 0.00001], 200)
    
# ----
#  RUN MAIN FUNCTION
# ----
main()