############################ PROJECT 1 #################################

import numpy as np  
import pandas as pd 
import random
import copy

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
# EVALUATION RESULTS OBJECT 
# ----------------------------------------------------------------------

class Eval_Obj:
    #initialize our class variables
    def __init__ (self, zeroOneLoss, precisionClassArr, precisionArr):
        self.zeroOneLoss = zeroOneLoss
        self.precisionClassArr = precisionClassArr
        self.precisionArr = precisionArr
        
    def __str__(self):
        retString = "0/1 Loss: "+ str(self.zeroOneLoss)+"\nPrecision Results: \n"
        for i in range(len(self.precisionClassArr)):
            retString = retString + "Class: "+ str(self.precisionClassArr[i])+ "\tPrecision: "+str(self.precisionArr[i])+"\n"
        return(retString)

       
    
# CREATE THE TEST SET OBJECT METHOD
def create_test_set(filename):
    #read the file into a 2DArray 
    
    #print("//////////////////////////////Reading file into 2DArray/////////////////////////////////////")
    #reader = pd.read_csv(r'glass.csv')
    #x = list(reader)
    #file = open(filename)
    #twoDArray = np.loadtxt(file, delimiter=",", skiprows=1)
    
    ### CHANGED TO PANDAS - CANNOT MAKE ARRAY WITH NUMPY, REQUIRES HOMOGENEOUS OBJECTS 
    twoDArray = pd.read_csv(filename)
    #print("////////////////////////////Printing Array ////////////////////////////////////////////////")
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
    #print("RUNNING Q FUNCTION")
    # Filter training set based off of class value
    arr = train_set.twoDArray
    is_classVal = arr['Class']==classVal
    arrClass = arr[is_classVal]
    
    # Declare N 
    N = train_set.total_samples
    
    q = len(arrClass) / N #Calculate Q
    #print(q)
    return(q)

def F(train_set, classVal, attValList): #multiply
    #print("RUNNING F FUNCTION")
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
    #print("CLASSIFYING DATA")
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
        
    #print(cValArr)
    #print(testArr) 

    return_set = test_set
    return_set.twoDArray=testArr 
    
    return(return_set)
    
def evaluation(item):
    #print("EVALUATION BEGINS")
    testArr = item.twoDArray
    cList = item.classes_holder
    
    ## Evaluations     
    # Find percent correct, 0/1 Loss
    is_correct = testArr['correctBool']==True
    correct_testArr = testArr[is_correct]
    correct = len(correct_testArr)
    total = len(testArr)
    
    loss = correct / total
    #print("0/1: ", loss)
    
    # Precision
    precisionArr = []
    for i in range(len(cList)):
        #Filter for class
        is_class = testArr['Class']==cList[i]
        cArr = testArr[is_class]
        total = len(cArr)
        
        is_correct = cArr['correctBool']==True
        correctArr = cArr[is_correct]
        correct = len(correctArr)
        
        precision = correct / total
        precisionArr.append(precision)

    returnEval = Eval_Obj(precision, cList, precisionArr)
    
    return(returnEval)
    


# ----------------------------------------------------------------------
# PRE PROCESS DATA - 10% DATA SHUFFLE
# ----------------------------------------------------------------------
def tenPercentShuffle(item):
    print("Intaking Array to Shuffle")
    arr = copy.deepcopy(item.twoDArray)
    
    numRowsShuff = int(item.total_samples*0.1)
    print(numRowsShuff)
    
    #Grab attribute values
    attVal = item.attributes_array
    
    #Make list to pull random items from
    rowList = []
    for k in range(item.total_samples):
        if k != 0:
            rowList.append(k)
    #print(rowList)
    
    print("Going to Shuffle 10% of Rows")
    #Change and shuffle 10% of rows
    for i in range(numRowsShuff):
        #print(i)
        rowIt = random.choice(rowList) #Pick random row
        rowList.remove(rowIt) #Remove from row list
        
        for j in range(item.attributes_total): #for each column
            if j != 0:
                arr.iat[rowIt, j] = random.choice(attVal)
       # print(arr.iloc[rowIt])
    
    print('All Rows Shuffled') 
    newItem = copy.deepcopy(item)
    
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
    
def tenFoldCross(dfList):
    tenFoldArr = []
    for x in range(10):
        testArr = dfList[x]
        tempList = dfList
        del tempList[x]
        
        trainArr = pd.concat(tempList) #make large dataframe
        
        temp_train = makeTrainSet(trainArr)
        temp_test = makeTrainSet(testArr)
        
        tenFoldArr.append(classify(temp_test, temp_train))
    
    passArr = pd.concat(tenFoldArr)

    return_set = makeTrainSet(passArr)  #Make object for evaluations use
    
    return_eval = evaluation(return_set)
        
    return(return_eval)
    
    
        
        
        
    
def makeTrainSet(twoDArray):
    #set number of columns and rows so that they can be called   
    print("Getting number of rows!")
    num_rows = len(twoDArray) ## Transitioned to pandas
    print(num_rows)
    print("Getting number of columns!")
    num_columns = len(twoDArray.columns)
    print(num_columns)

    #set the name of the set 
    print("Getting the name!")
    name =  str("file") 
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
    print("/////////// TESTING ALGORITHM ON TWO VERSIONS OF THE DATA ///////////")
    
    print("## BREAST CANCER")
    print("BC - Not Mixed")
    bc_s_pred = evaluation(classify(bc_set, bc_set))
    print(bc_s_pred)
    
    print("BC - Mixed")
    bc_m_pred = evaluation(classify(bc_mod, bc_mod))
    print(bc_m_pred)
    
    print("## GLASS")
    print("GS - Not Mixed")
    gs_s_pred = evaluation(classify(gs_set, gs_set))
    print(gs_s_pred)
    
    print("GS - Mixed")
    gs_m_pred = evaluation(classify(gs_mod, gs_mod))
    print(gs_m_pred)
    
    print("## IRIS")
    print("IR - Not Mixed")
    ir_s_pred = evaluation(classify(ir_set, ir_set))
    print(ir_s_pred)
    
    print("IR - Mixed")
    ir_m_pred = evaluation(classify(ir_mod, ir_mod))
    print(ir_m_pred)
    
    print("## SOYBEANS")
    print("SB - Not Mixed")
    sb_s_pred = evaluation(classify(sb_set, sb_set))
    print(sb_s_pred)
    
    print("SB - Mixed")
    sb_m_pred = evaluation(classify(sb_mod, sb_mod))
    print(sb_m_pred)
    
    print("## HOUSE VOTES")
    print("HV - Not Mixed")
    hv_s_pred = evaluation(classify(hv_set, hv_set))
    print(hv_s_pred)
    
    print("HV - Mixed")
    hv_m_pred = evaluation(classify(hv_mod, hv_mod))
    print(hv_m_pred)
    

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