## TO DO LIST ##
* Data Pre Propcessing 
    - A better approach is to sample according to the conditional probabilityof the values occurring, given the underlying class for that example. The choice of strategy is yours,but be sure to document your choice
    - Normalization of data to be on (-1, 1) Z scores 

	1. Data sets were transferred to CSV Files. Attribute Columns were named based off appropriate naming given in the .names file and class columns were renamed to 'Class' for easy access.
	2. All missing attribute information were randomly assigned (insert statment about how few missing attributes and how it is nominal)
	3. All Attribute values were transferred into Z-Scores
		a) All values for an attribute are assessed; mean and standard deviation are found
		b) using the mean, standard deviation and number of observations, the Z-score is calculated (insert traditional Z-score calc)
    - Normalization of data to be on (-1, 1) [Claire, Due 10/23]
* Base Python File Set-Up []
* Pseduocode for Hidden Nodes Tuning Process [All, Discuss 10/23]
    - You will need to determine the number of hidden nodes per layer via a tuning process
* Pseudocode for MLP (multi layer feedforward network with backpropogation) [All, Discuss 10/23] 
    -  arbitrary number of inputs, an arbitrary number of hidden layers, an arbitrary numberof hidden nodes by layer, and an arbitrary number of outputs
    -  (OLIVIA) Be able to specify whether a node uses a linear activation function for regression or a sigmoidal activation function for classification (you may choose between logistic or hyperbolic tangent) 
    So the main difference between using a hyper bolic tangent versus a logistic activation function is the range of the output. Hyperbolic tangent will fall between -1 and 1 and Logistic will fall between 0 and 1. I think that the logistic option will be easier to implement. It may be that we can try both pretty easily and see which one is more accurate. 

    Sigmoidal Activation Function (Logistic) : 

    output of the ith node = (1)/(1 + e ^ (- weighted sum of the input connections))

    Sigmoidal Activation Function (Hyperbolic Tangent) : 

    output of the ith node = tanh( weighted sum of the input connections )

    Linear Regression Function: 

    The tricky part of this one is that we need to figure out what the constant should be based on some sort of tuning . . . 

    output of the ith node = c(weighted sum of the input connections) where c is some coefficient we have to determine 

* A hypothesis focusing on convergence rate and final performance
* Test MLP Algorithm 
* Paper (OLIVIA)
* Define Regression and Clasification Functions 
    -  (OLIVIA)  
* Develop hypothesis focusing on convergence rate and final performance [All, Discuss 10/23]
* Implement MLP Algorithm 
* Paper 
* Video 
