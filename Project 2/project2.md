## TO DOS

* Pre-process data
* Implement k - nearest neighbor 
* Implement edited k - nearest neighbor 
* Implement partitioning around k - medoids
* Employ a plurality vote 
* Test the above three algoriths using at least 5 values for k 
* paper 
* video 


# k - nearest neighbor outline 

input - data subset 

* training examples are vectors in a multidimensional feature space, each with a class label. The training phase of the algorithm consists only of storing the feature vectors and class labels of the training samples.

* In the classification phase, k is a user-defined constant, and an unlabeled vector (a query or test point) is classified by assigning the label which is most frequent among the k training samples nearest to that query point. 

- Steps 

So, first take the vector (example) to be classified and find nearest k training examples. This will require some kind of distance function. I think I remember him saying that any of them work. 

Then amongst those k examples, find the most common classification. 

Assign that classfification to the vector (example) being tested. 



Both for classification and regression, a useful technique can be to assign weights to the contributions of the neighbors, so that the nearer neighbors contribute more to the average than the more distant ones. For example, a common weighting scheme consists in giving each neighbor a weight of 1/d, where d is the distance to the neighbor.

The neighbors are taken from a set of objects for which the class (for k-NN classification) or the object property value (for k-NN regression) is known. This can be thought of as the training set for the algorithm, though no explicit training step is required.


output - classification 


# edited k - nearest neighbor outline 




# partinioning around k - medoids outline 
https://www.geeksforgeeks.org/ml-k-medoids-clustering-with-example/

# hypothesis 

https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761