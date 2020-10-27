# -*- coding: utf-8 -*-
"""
CSCI 447 - Machine Learning
Project Three

MLP Object Class

@author: Claire Richards, Olivia Firth, Hannah Cebulla
"""

# IMPORT THE FOLLOWING PACKAGES AND FILES
import copy
import pandas as pd 

import dataset_obj

# ----
# MLP OBJECT CLASS
# ----
class mlp:
    # -----------------------------------------
    # ORDER OF FUNCTIONS WITHIN THE CLASS 
        # UNIVERSAL INTERNAL FUNCTIONS
            # INITALIZER FOR MLP OBJECT
    # FUNCTIONS IN THE DOCUMENT, OUTSIDE THE CLASS
        # ##
    # -----------------------------------------

    # ----------------------------------------- #
    # ------ UNIVERSL INTERNAL FUNCTIONS ------ #  
    # ----------------------------------------- #
    
    # ----
    # INITALIZER FUNCTION
    # ----
    def __init__(self, data_object):
        self.isRegression = data_object.regression #Indicates if dataset being imported into
        
    # ----
    # RUN FUNCTION
    # ----
    def run(self):
        print("MLP: Run")