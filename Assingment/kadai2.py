# -*- coding: utf-8 -*-

from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn.cross_validation import train_test_split

import numpy

iris = datasets.load_iris()

classifier = svm.SVC()

x, y = iris.data, iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .3)

classifier.fit(x_train, y_train)

predicted = classifier.predict(x_test)
expected = y_test

#iris_samples = len(iris.data)

#classifier.fit(iris.data[:iris_samples / 2], iris.target[:iris_samples / 2])

#expected = iris.target[iris_samples / 2:]
#predicted = classifier.predict(iris.data[iris_samples / 2:])

print("Classification report for classifier %s:\n%s\n" %(classifier, metrics.classification_report(expected, predicted)))

print("Confusion matrix:\n%s" %metrics.confusion_matrix(expected, predicted))

#print iris.target.size
