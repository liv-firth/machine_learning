# machine_learning

Machine Learning Projects Repository 

Notes on Evaluating using Loss Function: 

* 0/1 Loss Function 

So, as far as I understand loss function is for introducing some kind of metric that we can measure the "cost" of an incorrect decision with.

So let's say I have a dataset of 30 objects, I divided them to training / testing sets like 20 / 10. I will be using 0-1 loss function, so lets say my set of class labels is M and the function looks like this:

So I build some model on my training data, lets say I am using Naive Bayes classifier, and this model classified 7 objects correctly (assigned them the correct class labels) and 3 objects were classified incorrectly.

You have correctly summarized the 0-1 loss function as effectively looking at accuracy. Your 1's become indicators for misclassified items, regardless of how they were misclassified. Since you have three 1's out of 10 items, your classification accuracy is 70%.

If you change the weighting on the loss function, this interpretation doesn't apply anymore. For example, in disease classification, it might be more costly to miss a positive case of disease (false negative) than to falsely diagnose disease (false positive). In this case, your loss function would weight false negative misclassification more heavily. The sum of your losses would no longer represent accuracy in this case, but rather the total "cost" of misclassification. The 0-1 loss function is unique in its equivalence to accuracy, since all you care about is whether you got it right or not, and not how the errors are made.

So my loss function would return "0" 7 times and "1" 3 times

FOR EACH TEST GROUP, YOU JUST NEED TO ASSIGN 1 TO CORRECT CLASSIFICATION AND 0 FOR INCORRECT. BASICALLY THIS IS THE FRACTION/PERCENT OF CORRECT CLASSIFICATIONS IN EACH DATASET. 

* Precision Function

The output of this one will also just be a proportion. However, I think that we need a proportion for each class in a given data set. 

For each class  . . .  precision = (# samples correclty classified as being part of the class) / (# samples correclty classified as being part of the class + # samples classified as being part of that class even though they are not part of that class)

In other words precision = (TP)/(TP + FP)

We may be able to average these across a data set, but I'm not certain yet. 
