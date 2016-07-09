# ID : 16966023
# Akio Saito

from sklearn import svm,metrics
from sklearn.svm import SVC

clf=svm.SVC()
from sklearn import datasets
iris=datasets.load_iris()
X,y=iris.data, iris.target

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
print("Training Size: %d and Testing Size: %d\n" % (X_train.shape[0], X_test.shape[0]))

clf.fit(X_train, y_train)

predicted = clf.predict(X_test)
expected = y_test
print("Classification report for classifier %s:\n%s\n" % (clf, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
