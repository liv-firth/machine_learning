# -*- coding: utf-8 -*-
"""
CSCI 447 - Machine Learning 
Project 2

K-Nearest Neighbor Implementation
"""
## IMPORT THE FOLLOWING PACKAGES
import pandas as pd
import math as m
from math import sqrt
import copy

## IMPORT DATA SET CLASS FILE
import dataset_class
from ExtraFuncs import euclidean_distance, zeroOneLoss
import ExtraFuncs


class k_near_neighbor:
    # -----------------------------------------
    # ORDER OF FUNCTIONS WITHIN THE CLASS 
        # UNIVERSAL INTERNAL FUNCTIONS
            # INITALIZER FOR KNN OBJECT
            # FIT FUNCTION TO DEFINE TRAIN AND TEST SETS WITHIN THE KNN OBJECT
            # PREDICT FUNCTION TO PREDICT THE CLASS FROM NEAREST K NEIGHBORS
            # TUNE FUNCTION TO REFINE THE K VALUE INPUTTED INTO EACH KNN FUNCTION
        # KNN ALORITHM FUNCTIONS
            # BASE KNN FUNCTION
            # KNN EDITED FUNCTION
            # KNN CONDENSED FUNCTION
            # K PARTITIONED FUNCTION
            # K MEANS CLUSTERING FUNCTION
    # -----------------------------------------
    
    # ----------------------------------------- #
    # ------ UNIVERSL INTERNAL FUNCTIONS ------ #  
    # ----------------------------------------- #
    
    # ----
    # FUNCTION TO INITALIZE KNN OBJECT
    # ----
    def __init__(self, k, data_obj):
        self.k = k
        self.regression = data_obj.regression
        self.trainArr = data_obj.trainArr
        self.testArr = data_obj.testArr  
        self.tuneArr = data_obj.tuneArr
        self.numObs = data_obj.numObsv
        self.numAttr = data_obj.numAttr
        self.baseData = data_obj.dataArr
        self.data_obj = data_obj
    # ----
    # FUNCTION TO DEFINE WHAT THE TRAIN AND TEST SETS ARE TO USE
    # ----
    def fit(self, train, test):
        self.train = train
        self.test = test
               
    # ----
    # FUNCTION TO PREDICT THE CLASS OF A ROW FROM THE TEST SET
    # ----   
    def predict(self, testRow):
        #print("--- Predict Class by KNN ---")
        distances = []
        # Calculate Distances For All Neighbors
        for i in range(len(self.train)): #For all training set values
            tempDist = euclidean_distance(testRow, self.train.iloc[[i]], self.numAttr) #Return euclidean distance
            distances.append(tempDist) #Append distances list with temp distance calculated
        #print(distances)
        
        # Sort dataset by ascending distances
        newTrain = copy.deepcopy(self.train) #Create deepcopy of train (not connected with original)
        newTrain['Distances'] = distances #Add Distances column to data frame
        newTrain = newTrain.sort_values(by = 'Distances', ascending = True) #Order by distances column
        
        # Grab top k neighbors
        topNeighbors = newTrain.head(self.k) #Grab top k rows
        
        # Find Predicted Class
        if self.regression == False: #If not regressive, use prediction method
            predictedClass = topNeighbors['Class'].value_counts()[:1].index.tolist()
        else:
            print("Run Regression")
        
        testRow['PredClass'] = predictedClass
        
        if(testRow.iloc[0]['PredClass'] == testRow.iloc[0]['Class']):
            testRow['Correct'] = True
        else:
            testRow['Correct'] = False
            
        #print(testRow)
        return testRow 

        #Regression

        # Step 1: Get an array (later called array x) of equidistant unique possible values for an observation based on the data set i.e. for house -votes 
        # it would just be {democrat, republican} (however the classes may need to be represented numerically)

        #Step 2: Tune the band width (h) (this is similar to standard deviation)
            #To do this we will need to get a distribution of the data or K values, and find the range that 68% of the data falls into. 
            #based on that we can find the standard deviation and then we can tune within a small range centered at whatever the standard deviation was
            # The best way to do this is a little confusing for me, I am waiting for an email back from Giorgio
             
        #Step 3: For a given observation x_i that we wish to calculate, we calculate K at every value in array x 
            #Create a k_array to store K values for each element in x
            #To calculate K 
                    #Calculate A = 1/(h sqrt(2pi) (same for every value in array x) 
                    #Calulate B = -0.5[(x - x_i)/h]^2 where x_i is the observation value and x is the particular value from array x we are at 
                    #Calculate K = Ae^B  
                    #Put that value in k_array

            #Find the mean of k_array 
            #The prediciotn/classification is the value from array x, where the mean of the k_array occurs                  

        

 

    # ----
    # FUNCTION TO TUNE K USING THE ZERO ONE LOSS FUNCTION
    # ----
    def tune(self):
    # extract 10% of data 
#        tenPer = len(self.tuneArr)*.1 # calculate how many rows are ten percent  
#        df = self.dataArr #define data frame as data array
#        df = df.sample(frac=1) #shuffle data frame rows
#        r = 0 #set a starting point 
#        self.tuneArr = df.iloc[r:tenPer] #Grab Rows within r tenPer range

        #todo - remove tuningSet from the dataset 
        
        # find k values to be tuned to 
        kvalues =  []
        k1 = int(sqrt(self.numObs))
        kvalues.append(k1)
        k2 = int(k1 + (self.numObs*.05))
        kvalues.append(k2)
        k3 = int(k2 + (self.numObs*.05))
        kvalues.append(k3)
        k4 = int(k1 - (self.numObs*.05))
        kvalues.append(k4)
        k5 = int(k3 + (self.numObs*.05))
        kvalues.append(k5)
        loss_values = []

        #test on each k value 
        for v in range(len(kvalues)):
            temp_k = kvalues[v]
            #run knn on tuniing set 
            self.k = temp_k
            tempDataFrame = self.run_knn()
            lossValue = zeroOneLoss(tempDataFrame) #run a loss function to approximate accuracy 
            
            loss_values.append(lossValue) #store accuracy result in loss_values 
        max_value = max(loss_values) #Find Highest Precision Value
        max_index = loss_values.index(max_value) #grab index of max value
        best_k = kvalues[max_index] #grab best k value with the index of the max values
        
        self.k = best_k #reset self.k to be the best k

    # for training set, test against this 10 percent with different parameter values 
    
    
    # ----------------------------------------- #
    # -------- KNN ALGORITHM FUNCTIONS -------- #  
    # ----------------------------------------- #
    
    # ----
    # FUNCTION TO RUN THE KNN ALGORITHM
    # ----   
    def run_knn(self):
        print("--- Original KNN ---")
        allTestPred = []
        ## Run for each 10 fold cross
        for i in range(10): #Run for each set, 10 times
            self.fit(self.trainArr[i], self.testArr[i]) #Define train and test data sets
            numRows = len(self.test) #Define the number of rows to classify
            
            for x in range(numRows):
                tempTestRow = self.test.iloc[[x]]
                returnRow = self.predict(tempTestRow)
                allTestPred.append(returnRow)
        allPredRows = pd.concat(allTestPred)
        #print(allPredRows)
        return(allPredRows)
        
    # ----
    # FUNCTION TO RUN THE EDITED KNN ALGORITHM
    # ----   
    def run_edited_knn(self):
        print("--- Edited KNN ---")
        referenceRows = []
        ## Run for each 10 fold cross
        for i in range(10): #Run for each set, 10 times
            self.fit(self.trainArr[i], self.testArr[i]) #Define train and test data sets
            numRows = len(self.test) #Define the number of rows to classify
            
            for x in range(numRows):
                tempTestRow = self.test.iloc[[x]]
                returnRow = self.predict(tempTestRow)
                referenceRows.append(returnRow)
        referenceSet = pd.concat(referenceRows) #Turn into data frame
        
        ## Remove Incorrect Rows
        i = 0 #Build iterator for indexing rows during search and removal, set at 0
        while i < len(referenceSet):
            if referenceSet.iloc[i]['Correct'] == False: #If classified incorrectly,
                referenceSet.drop(referenceSet.index[i])
            #If not false, do nothing
            i += 1 #Iterate i by one
        
        ## Run with reference set as the training Array
        allTestPred = [] #Blank list to collect all predicted rows
        for n in range(10): #Run for each fold set, 10 times
            self.fit(referenceSet, self.testArr[n]) #Define train set as reference set, and test set as fold
            
            for x in range(len(self.test)): # For each test row
                returnRow = self.predict(self.test.iloc[[x]]) #Build return row from prediction on test row
                allTestPred.append(returnRow) #Append to row list
        returnDataFrame = pd.concat(allTestPred) #Concat all rows into a dataframe to return
        return returnDataFrame
    
    # ----
    # FUNCTION TO RUN THE CONDENSED K NN ALGORITHM
    # ---- 
    def run_condensed_knn(self):
        print("--- Condensed KNN ---")
        # Create storage and grab bag arrays
        storageArr = [] #Create blank storage array
        grabBagArr = [] #Create blank grab back
        
        numRows = len(self.baseData) #Define number of rows to reference
        
        #Put every other row into storage, test on other row
        for x in range(numRows):
            if(len(storageArr) != 0): # If not the first run      
                storage = pd.concat(storageArr)
                self.fit(storage, self.baseData)
            
            if x == 0: #If the first sample
                firstStorageRow = copy.deepcopy(self.baseData.iloc[[x]]) #Make Deep copy of first row in main data set
                firstStorageRow['PredClass'] = firstStorageRow['Class']
                firstStorageRow['Correct'] = True
                storageArr.append(firstStorageRow) #Place sample in storage
            else: #If not an even number
                returnRow = self.predict(self.test.iloc[[x]]) #Predict using KNN 
                # Check if correct
                if returnRow.iloc[0]['Correct']: #If classification was correct
                    grabBagArr.append(returnRow)
                else:
                    storageArr.append(returnRow)
        # Test Until grab bag is exhausted or complete pass is made without any grab bag objects moved to storage
        complete = False #Set complete to false
        while complete==False: #while not complete
            numIncorrect = 0 #Iterative for number incorrect reset to 0
            x = 0
            while x < len(grabBagArr):
                storage = pd.concat(storageArr) #Concatinate all storage Array rows into a single pandas dataframe
                self.fit(storage, self.baseData) #Reset test and training sets to equal the storage and base data information
                testRow = grabBagArr[x] #Set test row to be predicted upon
                returnRow = self.predict(testRow) #Predict using KNN 
                
                # Check if not correct
                if returnRow.iloc[0]['Correct'] == False: #If classification was not correct
                    storageArr.append(returnRow) #Add to the storage array
                    del grabBagArr[x]
                    numIncorrect += 1 #Add one to num incorrect
                # Do nothing if it was correct
                x += 1
            
            # Check for Completness
            if len(grabBagArr) == 0: #If grab back is empty
                complete = True #Set Complete to True, ending While Loop
            elif numIncorrect == 0: #If complete pass has been made without any being move to storage from the grab bag
                complete = True #Set Complete to True, ending while Loop
            
        # Set Consistent subset
        self.c_subset = pd.concat(storageArr)
        
        # Run KNN with condensed KNN as the reference set
        allTestPred = [] #Create blank array for predicted rows
        for i in range(10): #For each fold
            self.fit(self.c_subset, self.testArr[i]) #Set test array to the ith test fold and set the train array to the condensed data set
            numRows = len(self.test)
            
            for k in range(numRows): #For each test row
                returnRow = self.predict(self.test.iloc[[k]]) #Predict for the row
                allTestPred.append(returnRow)
        predictedTable = pd.concat(allTestPred) #concatinate all predicted rows into a data frame for returning
        return predictedTable     
             
    # ----
    # FUNCTION TO RUN THE PARTITIONED K ALGORITHM
    # ----   
    def run_partitioned_knn(self):
        print("--- Partitioning K ---")
        allTestPred = [] #Blank List for Predicted Rows
        df = copy.deepcopy(self.baseData)
        #Select k random points out of the data points in datas to use as medoids
        self.data_obj.makeMediodsCentroids(self.k) #Run MakeMediods for the data object
        self.data_obj.make10Fold() #Rebuild the Ten folds
        
        # Re assign several self objects
        self.trainArr = data_obj.trainArr
        self.testArr = data_obj.testArr  
        self.baseData = data_obj.dataArr
        self.mediods = data_obj.mediods #Add mediods variable to the class        
    
        #For each point in datas, find the closest medoid and make collect them (list of lists)
    
    
        #Set initial cost 
    
        #While current cost is less that 
    
        #Classify based on nearest medoid
    
     
     #Function for calculating cost 
        #For each medoid 
                    #For each point in your set 
                        #Calculate the absolute value of the difference (distance) (point - medoid)
                    #Sum the differences over all the points 
                #Sum the sums for each medoid  
    # ----
    # FUNCTION TO RUN THE K MEANS CLUSTERING
    # ---- 
    def run_k_means_cluster(self):
        print("--- K Means Clustering ---")
        #Initalize Centroids by first shuffling the dataset then randomly selecting k data points for the centroids without replacement
        self.data_obj.makeMediodsCentroids(self.k)
        self.centroids = self.data_obj.centroids # Initalize centroids data table
        self.baseData = self.data_obj.dataArr # Re-initalize base dat with new data object data array
        
        #Keep iterating until there is no change to the centroids
        iterations = 0 #Initalize for bookeeping
        oldCentroids = None #Blank object for holding the old centroids
        stopIterating = False #Flag for while loop
        allData = copy.deepcopy(self.baseData) #Create Copy of Base Data to reference
        
        while stopIterating != True: 
            # Save old centroids and iterate by one
            oldCentroids = self.centroids #save current centroids to old centroids
            iterations += 1 #Iterate iterations by one
            
            # Assign centroids to each data point
            for x in range(len(self.baseData)): #For every row in the base data
                #Find the closest centroid
                indexArray = [] #Blank Array to Record Row / Centroid Indexes Into
                distanceArray = [] #Blank Array to record Distances 
                for y in range(len(self.centroids)): #Measure Distance for each centroid
                    tempCentRow = self.centroids.iloc[[y]] #Move centroid row inot temporary variable for easy access
                    indexCentRow = tempCentRow.iloc[[0]].index # record the index for easy reference
                    indexArray.append(indexCentRow) #Append to list for later reference
                    
                    distCentroid = euclidean_distance(tempCentRow, allData.iloc[[x]], self.numAttr) #Calculate euclidean distance to Centroid
                    distanceArray.append(distCentroid) #Append to list for easy reference
                    
                #Determine centroid with minimium distance to row
                minDist = min(distanceArray)
                minDistIndex = distanceArray.index(minDist)
                minIndex = indexArray[minDistIndex] # Grab index of minimum value to assign as centroid
                
                allData.iloc[x]['Centroid'] = minIndex #Assign to Centroid
            
            # Assign Centroids based off of Centroid Assignment to Data points
            
            
            # Sort centroids datasets by index values
            self.centroids.sort_index() #Sort centroids
            oldCentroids.sort_index() #Sort oldCentroids data frame
            # Determine if while loop can stop
            if oldCentroids == self.Centroids: stopIterating = True #If new centroids equals the old centroids, stop Iterating
            
                
        #Compute the sum of the squared distance between data points and all centroids
        #Assign each data point to the closests cluster
        #Compute the centroids for the clusters by taking the average of all the data points that belong to each cluster
        
 