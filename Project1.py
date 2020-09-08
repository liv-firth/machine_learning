
############################ PROJECT 1 #################################

import numpy as np 
import csv 
import pandas

filename = #current test set - should be a file name 

# ----------------------------------------------------------------------
# TEST SET OBJECT 
# ----------------------------------------------------------------------

class Test_Set:
    #initialize our class variables
    def __init__ (test_set, name, attributes_total, classes_holder, classes_total, 2DArray, classes_array, total_samples):
        test_set.name = name
        test_set.attributes_total = attributes_total
        test_set.classes_holder = classes_holder
        test_set.classes_total
        test_set.2DArray = 2DArray
        test_set.classes_array = classes_array
        test_set.total_samples = total_samples
       
    #get methods
    def getName(test_set):
        return test_set.name

    def getAttributes(test_set):
        return test_set.attributes_total

    def getClassesHolder(test_set):
        return classes_holder

    def getClassesTotal(test_set):
        return test_set.classes_total

    def get2DArray(test_set):
        return 2DArray
    
    def getClassesArray(test_set):
        return classes_array
    
    def getTotalSamples(test_set):
        return total_samples
    
# CREATE THE TEST SET OBJECT METHOD
def create_test_set(filename):
    #read the file into a 2DArray 
    reader = csv.reader(open(file, "rb"), delimiter=",", skiprows=1)
    x = list(reader)
    2DArray = numpy.array(x).astype("int")

    #set number of columns and rows so that they can be called   
    num_rows, num_columns = 2DArray.shape

    #set the name of the set 
    name =  str(filename)   

    #get the number of attributes from the numer of columns minus the sample id and class       
    attributes_total = num_columns - 2   

    #create an array of unique possible class values 
    classes_holder = np.array([0])                    
    for row in range(0, num_rows -1): 
        #set a temporary class value that doesnt exist in any of the data sets
        temp_class = 0
        #make an array to hold each different class
        if 2DArray[row][num_columns -1] != temp_class:
            numpy.append(classes_holder,2DArray[row][num_columns -1])
            temp_class = 2DArray[row][num_columns -1]

    #set total number of classes 
    classes_total = len(classes_array)

    #set up classes array 
        #first sort the array by the last column 
        classes_array = 2DArray[2DArray[:, -1].argsort()]
        k = 0
        temp_class = classes_holder[k]
        #split the array everytime the class changes 
        for row in range(0, num_rows -1):
            if classes_array[row][num_columns -1] != temp_class:
                classes_array = np.vsplit(classes_array, row)
                k = k + 1

    #set the total number of samples based on how many rows you have      
    total_samples = num_rows 
    
    return test_set 

# ----------------------------------------------------------------------
# PRE PROCESS DATA 
# ----------------------------------------------------------------------
  #TODO CLAIRE  

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


########################################################################
# ----------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------
########################################################################
def main(): 
# ----------------------------------------------------------------------
# IMPORTANT AND PRE PROCESS 
# ----------------------------------------------------------------------

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
    
