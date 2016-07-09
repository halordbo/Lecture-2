from sklearn import datasets,svm,metrics
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
import numpy  as np

clf= svm.SVC()
iris = datasets.load_iris()
X,y=iris.data,iris.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
print("training size: %d and testing size: %d\n" %(X_train.shape[0],X_test.shape[0]))

clf.fit(X_train,y_train)
predicted= clf.predict(X_test)
expected=y_test
#ata_and_labels=list(zip(iris.data,iris.target))
#n_samples =len(iris.data)
#print(n_samples)
#data= iris.data.reshape((n_samples,-1))
#classifier=svm.SVC(gamma=0.001)
#classifier.fit(iris.data[:n_samples/2], iris.target[:n_samples/2])
#expected= iris.target[n_samples /2:]
#predicted= classifier.predict(iris.data[n_samples/2:])
print("classification report for classifier %s:\n%s\n"
     %(clf,metrics.classification_report(expected,predicted)))
print("confusion matrix:\n%s"% metrics.confusion_matrix(expected,predicted))

