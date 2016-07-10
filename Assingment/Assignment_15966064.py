"author: Sutthinan Anantarattanachai"
"ID: 15966064"

from sklearn import svm, metrics, datasets
from sklearn.cross_validation import train_test_split

#load Iris data
iris = datasets.load_iris()
X,y = iris.data,iris.target

#split test train randomly
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.33)
print("Training Size: %d and Testing Size: %d\n" % (X_train.shape[0],X_test.shape[0]))

#train SVM
classifier = svm.SVC(gamma=0.01)
classifier.fit(X_train, y_train)

#test SVM
predicted = classifier.predict(X_test)
expected = y_test
print("Classification report for classifier %s:\n%s\n" % \
(classifier,metrics.classification_report(expected,predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected,predicted))