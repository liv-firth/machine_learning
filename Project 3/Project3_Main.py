# -*- coding: utf-8 -*-
"""
CSCI 447 - Machine Learning
Project Three

@author: Claire Richards, Olivia Firth, Hannah Cebulla
"""
# ----
# IMPORT FILES AND PACKAGES
# ----

import pandas as pd


# ----
#  BUILD MAIN FUNCTION
# ----
def main():
    filenames = ["/breast-cancer-wisconsin.csv", "glass.csv", "glass.csv", "house-votes-84-fixed.csv", "machine.csv", "segmentation.csv"]

    ## IMPORT CLASSIFICATION DATA SETS: BREAST CANCER, GLASS, SOYBEAN
    
    ## IMPORT REGRESSION DATA SETS: ABALONE, COMPUTER HARDWARE, FOREST FIRES