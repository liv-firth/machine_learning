# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 12:30:52 2020

@author: Claire
"""
import numpy
import pandas as pd
import random

bc = pd.read_csv(r'breast-cancer-wisconsin.csv')
gs = pd.read_csv(r'glass.csv')
hv = pd.read_csv(r'house-votes-84.csv')
ir = pd.read_csv(r'iris.csv')
sb = pd.read_csv(r'soybean-small.csv')

print("Fixing Missing Attributes: house votes")
for i in range(len(hv)):
    for j in range(len(hv.columns)):
        tempval = hv.iat[i,j]
        if tempval == "?":
            newtemp = random.choice(["n", "y"])
            
            hv.iat[i, j] = newtemp
            print(hv.iat[i, j])

hv.to_csv('house-votes-84-fixed.csv')

print("Fixing Missing Attributes: breast cancer")
for i in range(len(bc)):
    for j in range(len(bc.columns)):
        tempval = bc.iat[i,j]
        if tempval == "?":
            newtemp = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            
            bc.iat[i, j] = newtemp
            print(bc.iat[i, j])

bc.to_csv('breast-cancer-wisconsin-fixed.csv')

        
        


