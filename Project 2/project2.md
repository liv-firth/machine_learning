## TO DOS

* Pre-process data [complete]
* Implement k - nearest neighbor 
* Implement edited k - nearest neighbor 
* Implement partitioning around k - medoids
* Employ a plurality vote 
* Test the above three algoriths using at least 5 values for k 
* paper 
* video 


# k - nearest neighbor outline 
non-parametric (no assumptions about the underlying distribution of the data)

input - data subset 

* training examples are vectors in a multidimensional feature space, each with a class label. The training phase of the algorithm consists only of storing the feature vectors and class labels of the training samples.

* In the classification phase, k is a user-defined constant, and an unlabeled vector (a query or test point) is classified by assigning the label which is most frequent among the k training samples nearest to that query point. 

- Steps 

1. So, first take the vector (example) to be classified and find nearest k training examples. This will require some kind of distance function. I think I remember him saying that any of them work. 

2. Then amongst those k examples, find the most common classification. 

3. Assign that classfification to the vector (example) being tested. 

Both for classification and regression, a useful technique can be to assign weights to the contributions of the neighbors, so that the nearer neighbors contribute more to the average than the more distant ones. For example, a common weighting scheme consists in giving each neighbor a weight of 1/d, where d is the distance to the neighbor.

The neighbors are taken from a set of objects for which the class (for k-NN classification) or the object property value (for k-NN regression) is known. This can be thought of as the training set for the algorithm, though no explicit training step is required.


output - classification 


# edited k - nearest neighbor outline 

In this rule, editing the reference set is first performed, every sample in the reference set is classified by using the k-NN rule and the set is formed by eliminating it from the reference set. All the samples mistakenly classified are then deleted from the reference set. Afterward, any input sample is classified using the k-NN rule and the edited reference set. Obviously, the editing k-nearest neighbors classifier (EK -NN) consists of the k-nearest neighbor classifier and an editing reference set. However, the editing reference set gained by this method is only a subset of the reference set. This may result in the loss of some important information and decline of classification accuracy.

- Steps 

1. Classify the reference set using the k-NN rule you developed 

2. Determine whether or not those examples have been correctly classfified or not. If they are incorrectly classified, remove them from the reference set.  

3. Use the edited reference set to perform k-NN again and classify points as desired. 

- Ignore this 
For every sample y in the edited reference set, all the k - or (k + 1) nearest neighbors of y must be in the class to which y belongs. Here n denotes the number of samples which tie with the kth nearest neighbor of y with respect to the distance from y (So all of the points that are the same distance as the k-th nearest neighbor). The performance of the rule proposed has been investigated using three classification examples. 


# partinioning around k - medoids outline 

* A medoid can be defined as the point in the cluster, whose dissimilarities with all the other points in the cluster is minimum.

* The dissimilarity of the medoid(Ci) and object(Pi) (example) is calculated by using E = |Pi - Ci|

- Steps 

1. Initialize: select k random points out of the n data points as the medoids.

2. Associate each data point to the closest medoid by using any common distance function 
    For each point, find the distance to each medoid, then find the minimum 
    Make the association (not sure what the best way to do that is)

        To find the cost - 
        For each medoid 
            For each point in your set 
                Calculate the absolute value of the difference (distance) (point - medoid)
            Sum the differences over all the points 
        Sum the sums for each medoid 

3. While the cost decreases:
        For each medoid m, for each data point p which is not a medoid:
                1. Swap m and p, associate each data point to the closest medoid, recompute the cost.
                2. If the total cost is more than that in the previous step, undo the swap.

At the end of this process, the classification of a given point is that of the nearest medoid. 

# hypothesis 
knn works better for lower dimension data sets
base hypothesis on choosing k?


https://machinelearningmastery.com/k-nearest-neighbors-for-machine-learning/
https://towardsdatascience.com/k-medoids-clustering-on-iris-data-set-1931bf781e05


# links 
https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761

https://www.geeksforgeeks.org/ml-k-medoids-clustering-with-example/

https://pdfs.semanticscholar.org/dc08/dbe7b7550ae0c10c568e8500df0bca94e267.pdf

