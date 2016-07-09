#1 usr/bin/python
#ID 16966063
#Name Yuki Yoshida

from sklearn.svm import SVC
from sklearn import svm,metrics

#default SVC values are showing ...
clf = svm.SVC()

#load the database
from sklearn import datasets
iris = datasets.load_iris()
X,y = iris.data, iris.target

#split test train randomly
from sklearn.cross_validation import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=100)
print("training size: %d and Testing size: %d\n" % (X_train.shape[0],X_test.shape[0]))

#train the classifier
clf.fit(X_train,y_train)

#test the classifier
predicted = clf.predict(X_test)
expected = y_test
print("classification report for classifier %s:\n%s\n" % (clf,metrics.classification_repo