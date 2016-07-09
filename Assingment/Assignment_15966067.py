import numpy
from sklearn import datasets, svm, metrics
from sklearn import datasets
from sklearn.svm import SVC
clf=svm.SVC()
iris = datasets.load_iris()
x,y=iris.data, iris.target

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3)

# train the classifier
clf.fit(x_train, y_train)
predicted = clf.predict(x_test)
expected = y_test
print("Classification report for classifier %s:\n%s\n"
      % (clf, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
