# -*- coding: utf-8 -*-
"""
Spyder Editor

Claire Yang
"""

import numpy as np
from sklearn import datasets
digits = datasets.load_digits()
digits_X = digits.data
digits_y = digits.target
np.unique(digits_y)


np.random.seed(0)
indices = np.random.permutation(len(digits_X))
digits_X_train = digits_X[indices[:-100]]
digits_y_train = digits_y[indices[:-100]]
digits_X_test  = digits_X[indices[-100:]]
digits_y_test  = digits_y[indices[-100:]]
from sklearn.neighbors import KNeighborsClassifier

def accuracy(a,b):
    count = 0.0
    for ai,bi in zip(a,b):
        if ai == bi:
            count += 1
    total = count/len(a)
    return total
    
for k in range(1,51):   
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(digits_X_train, digits_y_train)
    list1 = knn.predict(digits_X_test) #it will be a string
    list2 = digits_y_test
    print ("Accuracy is "+ str(accuracy(list1,list2))+" Neighbors: "+str(k))
    
#Any value of k under 23 appears to work about equally well,(mostly) 
#there are few outliers when k=9,=11,12,13 since the accuracy = 0.99.These may occur for underfitting, 
#optimal value of k lays b/w 14 to 23
    
    








