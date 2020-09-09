
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


    # option 1 - split the array everytime the class changes 
    #set up classes array 
    #first sort the array by the last column 
    #classes_array = twoDArray[twoDArray[:, -1].argsort()]
    #print("Printing sorted classes array!")
    #print(classes_array)

    #k = 0
    #print("Printing classes_holder index:")
    #temp_class = classes_holder[k]
    #print(temp_class)

    #problems start here 

    #for row in range(0, int(num_rows) -1):
        #if classes_array[row][int(num_columns) -1] != temp_class:
            #classes_array = np.split(classes_array, classes_array[row], axis=0)
            #k = k + 1
            #temp_class = classes_holder[k]


    #option 2 - create a list of python lists 
    classes_list = []
    #make lists of 1D numpy arrays from each class and put them in classes_list 
    for c in classes_holder:
        c_list = []
        for row in range (0, int(num_rows)-1):
            if twoDArray[row][int(num_columns) -1] == c:
                #add the row to the correct list 
                c_list.append(twoDArray[row])
        #turn the list into an array 
        c_list = np.array(c_list)
        #add the list to the classes list
        classes_list.append(c_list)
    #turn the list of classes into an np array 
    classes_array = np.array(classes_list)

    print("Printing classes_array!")
    print(classes_array)

    #set the total number of samples based on how many rows you have     
    print("Printing total number of samples!") 
    total_samples = int(num_rows)
    print(total_samples)
    
  # ----------------------------------------------------------------------
# ALGORITHM IMPLEMENTATION
# ----------------------------------------------------------------------

# STEP 1 METHOD ###############################################################
def Q(test_set): 
    # make an array to hold values of Q from each class 
    Q_list = np.zeroes(len(classes)) 
    # get the total number of examples in the test set 
    N = #todo

    for n in classes: 
    # For each class, divide the number of examples in that class by the total number of examples N in the training set

    # populate Q_list with each value 

return Q_list


# STEP 2 METHOD ###############################################################
# d is the number of attributes andNci= #fx2cig. In other words, for each attribute value,divide the number of examples 
# that match that attribute value (plus one) by the number of examples in the class (plusd)
# for each attribute in a given class
def F(attribute_total, classes):
    # 2D array of F values x attribute to populate
    F_attribute = np.zeroes([len(classes), attribute_total]) 

    # for each class in array of classes, c
    for n in classes: 
        # for each attribute in the set 
        for i # I dont rememeber this notation 
            # calculate the number of examples that match the attribute value (ask what that means) + 1 / attribute_total + the size of the class 

            # populate F_attribute with the value 


# STEP 3 METHOD ###############################################################
# To classify an example from the test set, do the following for each class. Calculate only for the attribute values that exist in the example.

# this method could apply to all classes or just one depending on how we want to do this
def C(class): 
    # calculate C 
    C = Q_list[#index for class]* the F value for each attribute



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
    # to test 
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
    
