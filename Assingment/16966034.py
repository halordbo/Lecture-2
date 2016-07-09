#!/usr/bin/env python

# library import
from sklearn import datasets
from sklearn.svm import SVC
from sklearn import svm,metrics
from sklearn.cross_validation import train_test_split

iris = datasets.load_iris()			# data load
x,y = iris.data,iris.target			# x,y input
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state = 3)

# data devide
classifier = svm.SVC()

classifier.fit(x_train, y_train)			# model training
predicted = classifier.predict(x_test)		
expected = y_test

print(metrics.accuracy_score(expected,predicted))

