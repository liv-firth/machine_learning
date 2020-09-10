############################ PROJECT 1 #################################

import numpy as np 
import csv 
import pandas as pd 
import random

# ----------------------------------------------------------------------
# TEST SET OBJECT 
# ----------------------------------------------------------------------

class Test_Set:
    #initialize our class variables
    def __init__ (self, name, attributes_total,  classes_holder, classes_total, twoDArray, classes_array, total_samples, attributes_array):
        self.name = name
        self.attributes_total = attributes_total
        self.classes_holder = classes_holder
        self.classes_total = classes_total
        self.twoDArray = twoDArray
        self.classes_array = classes_array
        self.total_samples = total_samples
        self.attributes_array = attributes_array
       
    #get methods
    def getName(self):
        return self.name

    def getAttributes(self):
        return self.attributes_total

    def getClassesHolder(self):
        return self.classes_holder

    def getClassesTotal(self):
        return self.classes_total

    def get2DArray(self):
        return self.twoDArray
    
    def getClassesArray(self):
        return self.classes_array
    
    def getTotalSamples(self):
        return self.total_samples

    # ----------------------------------------------------------------------
    # ALGORITHM IMPLEMENTATION
    # ----------------------------------------------------------------------

    # STEP 1 METHOD ###############################################################
    def Q(self): 
        # make a list to hold values of Q from each class 
        Q_list = []
    

        # For each class, divide the number of examples in that class by the total number of examples N in the training set
        for c in range(0, len(classes_array) -1): 
            temp = len(class_array[c])/self.total_samples # check that len()class_array[c] gives the correct value
            # populate Q_list with each value 
            Q_list.append(temp) 
        #turn it into an array 
        Q_array = np.array(Q_list)
        return Q_array


    # STEP 2 METHOD ###############################################################
    # d is the number of attributes andNci= #fx2cig. In other words, for each attribute value,divide the number of examples 
    # that match that attribute value (plus one) by the number of examples in the class (plusd)
    # for each attribute in a given class
    def F(self):
        # empty list of F values x attribute to populate
        F_attribute = [] 

        # for each class in array of classes, c
        for c in range(0, self.classes_total -1):
            # for each attribute in the set 
            current_class = self.classes_array[c]
            for a in range(0, self.attributes_total):
                # calculate the number of examples that match the attribute value (ask what that means) + 1 / attribute_total + the size of the class 
                # TODO

                # populate F_attribute with the value 
                return F_attribute

    # STEP 3 METHOD ###############################################################
    # To classify an example from the test set, do the following for each class. Calculate only for the attribute values that exist in the example.

    # this method could apply to all classes or just one depending on how we want to do this
    def C(self): 
        C_list = []
        # calculate C for each class 
        temp_array = self.Q
        for c in range(0, len(self.classes_array) -1):
            C = temp_array[c]
            for a in range(len(self.F), 0):
                C = C*self.F[a] # how do we do this with out recursion?

        #return arg max of C_list 
        



    
# CREATE THE TEST SET OBJECT METHOD
def create_test_set(filename):
    #read the file into a 2DArray 
    
    print("//////////////////////////////Reading file into 2DArray/////////////////////////////////////")
    #reader = pd.read_csv(r'glass.csv')
    #x = list(reader)
    #file = open(filename)
    #twoDArray = np.loadtxt(file, delimiter=",", skiprows=1)
    
    ### CHANGED TO PANDAS - CANNOT MAKE ARRAY WITH NUMPY, REQUIRES HOMOGENEOUS OBJECTS 
    twoDArray = pd.read_csv(filename)
    print("////////////////////////////Printing Array ////////////////////////////////////////////////")
    print(twoDArray)

    #set number of columns and rows so that they can be called   
    print("Getting number of rows!")
    num_rows = len(twoDArray) ## Transitioned to pandas
    print(num_rows)
    print("Getting number of columns!")
    num_columns = len(twoDArray.columns)
    print(num_columns)

    #set the name of the set 
    print("Getting the name!")
    name =  str(filename) 
    print(name)  

    #get the number of attributes from the numer of columns minus the sample id and class   
    print("Getting the total number of attributes!")    
    attributes_total = int(num_columns) - 1  
    print(attributes_total) 

    #create a list of unique possible class values 
    classes_holder = pd.unique(twoDArray['Class'])

    print("Printing classes_holder list!")
    print(classes_holder)
    
    ## Get Attributes List
    print("Grabbing Attributes Array")
    tempList = []
    for k in range(attributes_total+1):
        if k != 0:
            temp = pd.unique(twoDArray.iloc[:,k])
            for p in temp:
                tempList.append(k)
    attributes_array = pd.unique(tempList)
            
    ## Set total number of classes 
    print("Printing classes total!")
    classes_total = len(classes_holder)
    print(classes_total)


    ## Set the total number of samples based on how many rows you have     
    print("Printing total number of samples!") 
    total_samples = int(num_rows)
    print(total_samples)
    
    temp_test_set = Test_Set(name, attributes_total, classes_holder, classes_total, twoDArray, classes_holder, total_samples, attributes_array)
    return(temp_test_set)
   
# ----------------------------------------------------------------------
# ALGORITHM 
# ----------------------------------------------------------------------  

def Q(train_set, classVal):
    print("RUNNING Q FUNCTION")
    # Filter training set based off of class value
    arr = train_set.twoDArray
    is_classVal = arr['Class']==classVal
    arrClass = arr[is_classVal]
    
    # Declare N 
    N = train_set.total_samples
    
    q = len(arrClass) / N #Calculate Q
    print(q)
    return(q)

def F(train_set, classVal, attValList): #multiply
    print("RUNNING F FUNCTION")
    # Grab Relevant information from training set
    attList = train_set.attributes_array
    arr = train_set.twoDArray
    numAtt = train_set.attributes_total
    
    #Filter by class variable
    is_classVal = arr['Class']==classVal
    arrClass = arr[is_classVal]
    
    numClass = len(arrClass)
    
    f = 1 #Create standard F Value
    #For each attribute
    for i in range(train_set.attributes_total):
        #Filter class array for attribute val
        val = attValList[i]
        sumMatch = 0
        for k in range(len(arrClass)):
            if arrClass.iat[k, i+1]==val:
                sumMatch = sumMatch + 1
        tempF = (sumMatch + 1) / (numAtt + numClass)
        
        f = f*tempF

    #print(f)
    return(f)
    

def classify(test_set, train_set):
    print("CLASSIFYING DATA")
    cList = test_set.classes_holder
    
    testArr = test_set.twoDArray
    testArr["predClass"]=""
    testArr["correctBool"]=""
    
    
    for i in range(len(testArr)): # For each value of the test array
        cValArr = [] #Blank list to append to with values
        #Build row array
        rowArr = []
        #print(i)
        for m in range(test_set.attributes_total):
            rowArr.append(testArr.iat[i,m+1])
        #print(rowArr)
        
        for k in cList: #For each class available
            q = Q(train_set, k)
            f = F(train_set, k, rowArr)
            
            c = q*f
            cValArr.append(c)
        
        #Determine max index
        maxIndex = cValArr.index(max(cValArr))
        classDec = cList[maxIndex]
        testArr.at[i,"predClass"]=classDec
        
        if testArr.at[i, "Class"] == testArr.at[i, "predClass"]:
            testArr.at[i, "correctBool"] = True
        else: testArr.at[i, "correctBool"] = False
        
    print(cValArr)
    print(testArr) 

    return_set = test_set
    return_set.twoDArray=testArr     

    return(return_set)
    


# ----------------------------------------------------------------------
# PRE PROCESS DATA - 10% DATA SHUFFLE
# ----------------------------------------------------------------------
def tenPercentShuffle(item):
    print("Intaking Array to Shuffle")
    arr = item.twoDArray
    
    numRowsShuff = int(item.total_samples*0.1)
    print(numRowsShuff)
    
    #Grab attribute values
    attVal = pd.unique(arr.iloc[:, 1])
    #print(attVal)
    
    #Make list to pull random items from
    rowList = []
    for k in range(item.total_samples):
        if k != 0:
            rowList.append(k)
    #print(rowList)
    
    print("Going to Shuffle 10% of Rows")
    #Change and shuffle 10% of rows
    for i in range(numRowsShuff):
        rowIt = random.choice(rowList) #Pick random row
        rowList.remove(rowIt) #Remove from row list
        
        for j in range(item.attributes_total): #for each column
            if j != 0:
                arr.iat[rowIt, j] = random.choice(attVal)
       # print(arr.iloc[rowIt])
    
    print('All Rows Shuffled') 
    newItem = item
    
    newItem.twoDArray = arr
    return(newItem)

# ----------------------------------------------------------------------
# CROSS VALIDATION CREATION AND RUNNING
# ----------------------------------------------------------------------    
def tenFoldCreation(item):
    df = item.twoDArray
    
    #Shuffle Rows
    df = df.sample(frac=1)
    
    #Find number of rows to grab with each group
    numRow = int(item.total_samples * 0.1) #Number of rows to grab in each fold
    lastRow = int(item.total_samples - 1) #Final row index
    
    n = 0 #Row Iterative
    dfList = [] #Create blank list to append to
    for i in range (9): #Run nine times
        #print(i)
        m = n + numRow #Find last row to grab based off of iterative
        tempdf = df.iloc[n:m] #Grab only rows between n and m
        dfList.append(tempdf) #Append List with new item
        n = m + 1 #Update n
    
    #Final Iteration (Catches any missed rows)
    tempdf = df.iloc[n:lastRow] #Grab through current iterative through final row
    dfList.append(tempdf) #Append List with last df
    
    #print(dfList)
    return(dfList)
    
        
        



########################################################################
# ----------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------
########################################################################
def main(): 
# ----------------------------------------------------------------------
# IMPORTANT AND PRE PROCESS 
# ----------------------------------------------------------------------
    # List of all datasets
    filename = ["breast-cancer-wisconsin-fixed.csv", "glass.csv", "iris.csv", "soybean-small.csv", "house-votes-84-fixed.csv"]
    
    ## Create Test Sets and Modified sets for each dataset
    bc_set = create_test_set(filename[0])
    bc_mod = tenPercentShuffle(bc_set)
    
    gs_set = create_test_set(filename[1])
    gs_mod = tenPercentShuffle(gs_set)
       
    ir_set = create_test_set(filename[2])
    ir_mod = tenPercentShuffle(ir_set)
    
    sb_set = create_test_set(filename[3])
    sb_mod = tenPercentShuffle(sb_set)
    
    hv_set = create_test_set(filename[4])
    hv_mod = tenPercentShuffle(hv_set)
    

# ----------------------------------------------------------------------
# TEST THE ALGORITHM ON TWO DIFFERENT VERSIONS OF THE DATA
# ----------------------------------------------------------------------
    print("TESTING ALGORITHM ON TWO VERSIONS OF THE DATA")
    bc_s_pred = classify(bc_set, bc_set)
    bc_m_pred = classify(bc_mod, bc_set)
    

# ----------------------------------------------------------------------
# EVALUATION MEASURES
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# EXECUTE EXPERIMENTS USING 10 FOLD CROSS VALIDATION
# ----------------------------------------------------------------------   

    ## For BC Datasets
    bc_set_tenFolds = tenFoldCreation(bc_set)
    bc_mod_tenFolds = tenFoldCreation(bc_mod)
    
    ## For Glass Datasets
    gs_set_tenFolds = tenFoldCreation(gs_set)
    gs_mod_tenFolds = tenFoldCreation(gs_mod)
    
    ## For Iris Datasets
    ir_set_tenFolds = tenFoldCreation(ir_set)
    ir_mod_tenFolds = tenFoldCreation(ir_mod)
    
    ## For Soybean Datasets
    sb_set_tenFolds = tenFoldCreation(sb_set)
    sb_mod_tenFolds = tenFoldCreation(sb_mod)
    
    ## For House Votes Datasets
    hv_set_tenFolds = tenFoldCreation(hv_set)
    hv_mod_tenFolds = tenFoldCreation(hv_mod)

main()