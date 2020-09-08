
############################ PROJECT 1 #################################

import numpy as np 

test_set = #current test set 
attribute_total = # number of attributes of imported class (should be close to number of columns)
# ----------------------------------------------------------------------
# PRE PROCESS DATA 
# ----------------------------------------------------------------------
# I am assuming we will turn a given set into a 2d numpy array and then separate it into classes
def process(test_set):
    classes = #array of 2d arrays containing each class?
    return classes 
    

# ----------------------------------------------------------------------
# ALGORITHM IMPLEMENTATION
# ----------------------------------------------------------------------

# STEP 1 ###############################################################
def Q(classes): 
    # make an array to hold values of Q from each class 
    Q_list = np.zeroes(len(classes)) 
    # get the total number of examples in the test set 
    N = #todo

    for n in classes: 
    # For each class, divide the number of examples in that class by the total number of examples N in the training set

    # populate Q_list with each value 

return Q_list

 

# STEP 2 ###############################################################
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


# STEP 3 ###############################################################
# To classify an example from the test set, do the following for each class. Calculate only for the attribute values that exist in the example.

# this method could apply to all classes or just one depending on how we want to do this
def C(class): 
    # calculate C 
    C = Q_list[#index for class]* the F value for each attribute


# ----------------------------------------------------------------------
# TEST THE ALGORITHM ON TWO DIFFERENT VERSIONS OF THE DATA
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# EVALUATION MEASURES
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# EXECUTE EXPERIMENTS USING 10 FOLD CROSS VALIDATION
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# MAIN 
# ----------------------------------------------------------------------
def main():
    process()
