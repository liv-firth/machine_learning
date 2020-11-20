# -*- coding: utf-8 -*-
"""
CSCI 447 - Machine Learning
Project Three

Pre-Process Data Script

@author: Claire Richards, Olivia Firth, Hannah Cebulla
"""

import pandas as pd
import random

import numpy as np

# ## ABALONE DATA SPECIFIC ACTIONS
#     # CODIFY SEX COLUMN TO THE FOLLOWING: m = 1, w = 2, i = 3
# ab = pd.read_csv(r'abalone.csv')
# for i in range(len(ab)):
#     if ab.loc[ab.index[i], 'SEX'] == 'M': ab.loc[ab.index[i], 'SEX'] = 1
#     elif ab.loc[ab.index[i], 'SEX'] == 'F': ab.loc[ab.index[i], 'SEX'] = 2
#     elif ab.loc[ab.index[i], 'SEX'] == 'I': ab.loc[ab.index[i], 'SEX'] = 3
# ab.to_csv('abalone.csv', index = False)

# ## BREAST CANCER SPECIFIC ACTIONS
#     # 16 MISSING VALUES (DENOTED BY ?): RANDOMLY ASSIGN VALUES (1-10)
# bc = pd.read_csv(r'breast-cancer-wisconsin.csv')
# for i in range(len(bc)):
#     for j in range(len(bc.columns)):
#         tempval = bc.iat[i,j]
#         if tempval == "?":
#             newtemp = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            
#             bc.iat[i, j] = newtemp
# bc.to_csv('breast-cancer-wisconsin.csv', index = False)

# ## FOREST FIRE SPECIFIC ACTIONS
#     # MONTHS CODED TO 1-12 (JAN = 1, ETC.)
#     # DAYS CODED TO 1-7 (SUN = 1, ETC.)
# ff = pd.read_csv(r'forestfires.csv')
# for i in range(len(ff)):
#     if ff.loc[ff.index[i], 'month'] == 'jan': ff.loc[ff.index[i], 'month'] = 1
#     elif ff.loc[ff.index[i], 'month'] == 'feb': ff.loc[ff.index[i], 'month'] = 2
#     elif ff.loc[ff.index[i], 'month'] == 'mar': ff.loc[ff.index[i], 'month'] = 3
#     elif ff.loc[ff.index[i], 'month'] == 'apr': ff.loc[ff.index[i], 'month'] = 4
#     elif ff.loc[ff.index[i], 'month'] == 'may': ff.loc[ff.index[i], 'month'] = 5
#     elif ff.loc[ff.index[i], 'month'] == 'jun': ff.loc[ff.index[i], 'month'] = 6
#     elif ff.loc[ff.index[i], 'month'] == 'jul': ff.loc[ff.index[i], 'month'] = 7
#     elif ff.loc[ff.index[i], 'month'] == 'aug': ff.loc[ff.index[i], 'month'] = 8
#     elif ff.loc[ff.index[i], 'month'] == 'sep': ff.loc[ff.index[i], 'month'] = 9
#     elif ff.loc[ff.index[i], 'month'] == 'oct': ff.loc[ff.index[i], 'month'] = 10
#     elif ff.loc[ff.index[i], 'month'] == 'nov': ff.loc[ff.index[i], 'month'] = 11
#     elif ff.loc[ff.index[i], 'month'] == 'dec': ff.loc[ff.index[i], 'month'] = 12

#     if ff.loc[ff.index[i], 'day'] == 'sun': ff.loc[ff.index[i], 'day'] = 1
#     elif ff.loc[ff.index[i], 'day'] == 'mon': ff.loc[ff.index[i], 'day'] = 2
#     elif ff.loc[ff.index[i], 'day'] == 'tue': ff.loc[ff.index[i], 'day'] = 3
#     elif ff.loc[ff.index[i], 'day'] == 'wed': ff.loc[ff.index[i], 'day'] = 4
#     elif ff.loc[ff.index[i], 'day'] == 'thu': ff.loc[ff.index[i], 'day'] = 5
#     elif ff.loc[ff.index[i], 'day'] == 'fri': ff.loc[ff.index[i], 'day'] = 6
#     elif ff.loc[ff.index[i], 'day'] == 'sat': ff.loc[ff.index[i], 'day'] = 7

# ff.to_csv('forestfires.csv', index = False)

## GLASS SPECIFIC ACTIONS
    # NONE IN PYTHON

## MACHINE SPECIFIC ACTIONS
    # NONE IN PYTHON

## SEMGENTATION SPECIFIC ACTIONS
    # NONE IN PYTHON
    
# --------
# PROCESS ALL DATA
# --------
filenames = ["breast-cancer-wisconsin.csv", "glass.csv", "soybean-small.csv", "abalone.csv", "machine.csv", "forestfires.csv"]

for i in range(len(filenames)):
    print(filenames[i])
    npArr = np.genfromtxt(filenames[i], delimiter = ',')
    
    num_rows, num_cols = npArr.shape
    num_cols -= 1 
    
    for k in range(num_cols-1):
        tempList = npArr[:,[k]]
        
        x = tempList.mean()
        sd = tempList.std()
        
        for n in range(num_rows):
            npArr[n, k] = ((npArr[n, k]-x)/sd)
    np.savetxt(filenames[i], npArr, delimiter=',')
        
        