# -*- coding: utf-8 -*-
"""
CSCI 447 - Machine Learning
Project Four

@author: Claire Richards, Olivia Firth, Hannah Cebulla
"""
# ----
# IMPORT FILES AND PACKAGES
# ----

#Dataset Object
import dataset_obj #Interal File, Data Set Object Class File
from dataset_obj import create_data_set

#Genetic Algorithm
from ga import run_ga


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
    
    ## RUN GENETIC ALGORITHM
    ### run_ga(data_object, n_hidden, l_rate, n_epoch, size, n_parents)
    run_ga(aba_data, 1, 0.1, 50, 200, 100)
    
    

    
# ----
#  RUN MAIN FUNCTION
# ----
main()