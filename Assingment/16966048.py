#藤田啓斗(Hiroto Fujita)
from sklearn import datasets
from sklearn.cross_validation import train_test_split
iris= datasets.load_iris()
from sklearn import metrics
from sklearn import svm
from sklearn.svm import SVC
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
classifier = svm.SVC(gamma=0.001)
clf = svm.SVC(gamma=0.001,C=100)
classifier.fit(X_train,y_train)
expected = y_test
predicted = classifier.predict(X_test)
print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
