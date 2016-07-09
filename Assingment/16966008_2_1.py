#16966008 ERA Masayoshi
#!/usr/bin/python
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics

from sklearn import datasets
from sklearn.svm import SVC
iris = datasets.load_iris()
from sklearn import svm
n_samples = len(iris.data)

data = iris.data.reshape((n_samples, -1))
#classfilter = svm.SVC(gamma=0.001)
classfilter = svm.SVC(gamma=0.001,C=100)
from sklearn import datasets
iris = datasets.load_iris()
X,y = iris.data, iris.target

from sklearn.cross_validation import train_test_split
X_train, X_test,y_train,y_test=train_test_split(X,y,test_size=.3)

classfilter.fit(X_train, y_train)
#gaku
#classfilter.fit(data[:n_samples / 2], iris.target[:n_samples / 2])
classfilter.fit(X_train, y_train)
#yosoku
predicted = classfilter.predict(X_test)
expected = y_test
#expected = iris.target[n_samples / 2:]
#predicted = classfilter.predict(data[n_samples / 2:])

#print
print("Classification report for classifier %s:\n%s\n"
      % (classfilter, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
