
############################ PROJECT 1 #################################

import numpy as np 
import csv 
import pandas as pd 

# ----------------------------------------------------------------------
# TEST SET OBJECT 
# ----------------------------------------------------------------------

class Test_Set:
    #initialize our class variables
    def __init__ (self, name, attributes_total, classes_holder, classes_total, twoDArray, classes_array, total_samples):
        self.name = name
        self.attributes_total = attributes_total
        self.classes_holder = classes_holder
        self.classes_total = classes_total
        self.twoDArray = twoDArray
        self.classes_array = classes_array
        self.total_samples = total_samples
       
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
    
# CREATE THE TEST SET OBJECT METHOD
def create_test_set(filename):
    #read the file into a 2DArray 
    
    print("//////////////////////////////Reading file into 2DArray/////////////////////////////////////")
    #reader = pd.read_csv(r'glass.csv')
    #x = list(reader)
    file = open(filename)
    twoDArray = np.loadtxt(file, delimiter=",", skiprows=1)
    print("////////////////////////////Printing Array ////////////////////////////////////////////////")
    print(twoDArray)

    #set number of columns and rows so that they can be called   
    print("Getting number of rows!")
    num_rows = np.shape(twoDArray)[0]
    print(num_rows)
    print("Getting number of columns!")
    num_columns = np.shape(twoDArray)[1]
    print(num_columns)

    #set the name of the set 
    print("Getting the name!")
    name =  str(filename) 
    print(name)  

    #get the number of attributes from the numer of columns minus the sample id and class   
    print("Getting the total number of attributes!")    
    attributes_total = int(num_columns) - 2  
    print(attributes_total) 

    #create a list of unique possible class values 
    classes_holder = []

    #set a temporary class value that doesnt exist in any of the data sets
    temp_class = 567890
    for row in range(0, num_rows -1): 
        #make an array to hold each different class
        if twoDArray[row][int(num_columns) -1] != temp_class:
            classes_holder.append(twoDArray[row][int(num_columns) -1])
            temp_class = twoDArray[row][int(num_columns) -1]
    print("Printing classes_holder list!")
    print(classes_holder)
    print("Printing classes holder array!")
    classes_holder = np.array(classes_holder)
    print(classes_holder)

    #set total number of classes 
    print("Printing classes total!")
    classes_total = len(classes_holder)
    print(classes_total)

    #set up classes array 
    #first sort the array by the last column 
    classes_array = twoDArray[twoDArray[:, -1].argsort()]
    print("Printing sorted classes array!")
    print(classes_array)

    k = 0
    print("Printing classes_holder index:")
    temp_class = classes_holder[k]
    print(temp_class)

    #problems start here 
    
    #split the array everytime the class changes 
    for row in range(0, int(num_rows) -1):
        if classes_array[row][int(num_columns) -1] != temp_class:
            classes_array = np.split(classes_array, classes_array[row], axis=0)
            k = k + 1
            temp_class = classes_holder[k]

    print("Printing classes_array!")
    print(classes_array)
    #set the total number of samples based on how many rows you have     
    print("Printing total number of samples!") 
    total_samples = int(num_rows)
    print(total_samples)
    
  

# ----------------------------------------------------------------------
# PRE PROCESS DATA 
# ----------------------------------------------------------------------
  #TODO CLAIRE  



########################################################################
# ----------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------
########################################################################
def main(): 
# ----------------------------------------------------------------------
# IMPORTANT AND PRE PROCESS 
# ----------------------------------------------------------------------
    create_test_set("glass.csv")


# ----------------------------------------------------------------------
# TEST THE ALGORITHM ON TWO DIFFERENT VERSIONS OF THE DATA
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# EVALUATION MEASURES
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# EXECUTE EXPERIMENTS USING 10 FOLD CROSS VALIDATION
# ----------------------------------------------------------------------   


main()
    
