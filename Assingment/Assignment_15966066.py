#!/usr/bin/python
# author: Joshi Ravi Prakash
# student id: 15966066
# date: 04 July 2016

from sklearn.svm import SVC
from sklearn import svm, metrics

# default SVC values are showing higher f1 score
clf = svm.SVC()

# load the database 
from sklearn import datasets
iris = datasets.load_iris()
X,y = iris.data, iris.target

# split test train randomly
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)
print("Training Size: %d and Testing Size: %d\n" % (X_train.shape[0], X_test.shape[0]))

# train the classifier
clf.fit(X_train, y_train)

# test the classifier
predicted = clf.predict(X_test)
expected = y_test
print("Classification report for classifier %s:\n%s\n" % (clf, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
