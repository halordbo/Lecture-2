# 16966041
# Masataka Hisano
# 4 July 2016

#usr/bin/python
from sklearn.svm import SVC
from sklearn import datasets, svm, metrics

classifier = svm.SVC()

#loading datasets
iris = datasets.load_iris()
iris.data
iris.target
iris.viewkeys()
x,y = iris.data, iris.target


#split test train
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=.3)
print("Training size: %d and testing size: %d\n" % (x_train.shape[0],x_test.shape[0]))

classifier.fit(x_train,y_train)

expected = y_test
predicted = classifier.predict(x_test)
print("Classification report for classifier %s:\n%s\n" %(classifier, metrics.classification_report(expected,predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
