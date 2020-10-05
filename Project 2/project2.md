## TO DOS

* Pre-process data [complete] (Steps Below)
	+ All Data files were transferred to csv files for easy transfer into pandas dataframe
	+ Result / Class Attributes were renamed to 'Class' in all files
	+ Non predictive Attributes were removed (see each .names file for details on which attributes were removed, maybe we can put this in a table)
	+ Missing attribute values were assigned randomized values for that attribute (will add more details)
* Implement k - nearest neighbor [complete]
* Implement edited k - nearest neighbor [complete, with exeption of Error]
* Implement condensed knn [complete, with exception of Error]
* Implement k-means clustering [in-progress]
* Implement partitioning around k - medoids [in-progress]
* Employ a plurality vote [complete]
* Employ Regression assignment
* Test the above three algoriths using at least 5 values for (Isn't this tuning?) [in-progress]
* paper [in-progress]
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

# Condensed K NN

- uses a subset of the training set 
- creates a stored reference set for the NN rule 
- only uses points that are on the boundary of a neighborhood
- minimum consitent subset - minimum classified set that will correctly classify any obs 

Steps: 

1. Find consistent subset. To do so  . . .
    * Create two bins/arrays for storage, call one storage and one grab bag
    * Take a sample and place it in store 
    * Take a second sample - Second sample is classified by nn rule using contents of storage 
        If classified correclty, - put it in grab bag 
        If it is classified incorreclty - put it in storage 
    * Proceed through the examples, classify based on what is in storage 
        If classified correclty, - put it in grab bag 
        If it is classified incorreclty - put it in storage 
    * Once you loop through the sample/training set, loop through the grab bag until one of two things occurs:
        1. The grab bag is exhausted with all of its elements placed in storage 
        2. One complete pass has been made through grab bag without any obs being moved to storage 

2. Use consistent subset for NN Rule. Final contents of storage are used for your reference set when using the NN rule. 

http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.294.6968&rep=rep1&type=pdf
https://pdfs.semanticscholar.org/4473/1460f9a1ca3e30c376d2a4f0c843573b2c6b.pdf

# K means clustering 

- Find subgroups that are relatively similar and group them for classification 
- Unsuperivsed learning 

Steps: 

1. Specify number of clusters K (we can tune for this)
2. Initialize centroids by first shuffling the dataset and then randomly selecting K data points for the centroids without replacement.
3. Keep iterating until there is no change to the centroids - assignment of data points to clusters isn’t changing (I think this is the tricky part)
4. Compute the sum of the squared distance between data points and all centroids. 
5. Assign each data point to the closest cluster (centroid).
6. Compute the centroids for the clusters by taking the average of the all data points that belong to each cluster.
https://towardsdatascience.com/k-means-clustering-algorithm-applications-evaluation-methods-and-drawbacks-aa03e644b48a

# Regression

- Involves three variables x, x_i, and h
x = An evenly distributed (linearly spaced) list of all unique possible values of x in the data set in order
x_i = observed data point (the one we are trying to classify/predict)
h = bandwith (needs to be tuned) also presented as standard deviation

K = Ae^B

A = 1/(h sqrt(2pi)

B = -0.5[(x - x_i)/h]^2

If you graph x and K, x_i will be the mean 

https://towardsdatascience.com/kernel-regression-made-easy-to-understand-86caf2d2b844


For tuning h : About 68% of values drawn from a normal distribution are within one standard deviation σ away from the mean; about 95% of the values lie within two standard deviations; and about 99.7% are within three standard deviations.


# hypothesis 
knn works better for lower dimension data sets
base hypothesis on choosing k?


https://www.mygreatlearning.com/blog/knn-algorithm-introduction/
https://machinelearningmastery.com/k-nearest-neighbors-for-machine-learning/
https://towardsdatascience.com/k-medoids-clustering-on-iris-data-set-1931bf781e05
http://ijarcet.org/wp-content/uploads/IJARCET-VOL-5-ISSUE-6-1943-1946.pdf


# links 
https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761

https://www.geeksforgeeks.org/ml-k-medoids-clustering-with-example/

https://pdfs.semanticscholar.org/dc08/dbe7b7550ae0c10c568e8500df0bca94e267.pdf
