# -*- coding: utf-8 -*-
"""
CSCI 447 - Machine Learning
Project Three

Genetic Algorithm Class

@author: Claire Richards, Olivia Firth, Hannah Cebulla
"""

# IMPORT THE FOLLOWING PACKAGES AND FILES
import copy
import pandas as pd 
from random import seed
from random import random
from math import exp
from sklearn.linear_model import LogisticRegression

import dataset_obj

# -----------------------------------------
# ORDER OF FUNCTIONS WITHIN THE CLASS 
    # INITALIZER FOR LOGARITHMIC REGRESSION OBJECT
    
# FUNCTIONS IN THE DOCUMENT, OUTSIDE THE CLASS
    # 
    # 
# -----------------------------------------

# ----
# LOGISTIC REGRESSION
# ----
class logRessObj:
    def __init__(self, dataset):
        self.logRess = LogisticRegression()
        self.dataset = dataset
        
      
    