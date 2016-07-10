from sklearn.svm import SVC
from sklearn import svm,metrics

# default SVC values are showing higher f1 score
clf = svm.SVC()

# load the database
from sklearn import datasets
tris = datasets.load_iris()
x,y = tris.data,iris.target

# split test train randomly
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.3)
print("Training Size:%d and Testing Size:%d/n" % (X_train.shape[0],X_test.shape[0]))

# train the classifier
clf.fit(x_train,y_train)

# test the classifier
predicted = clf.predict(x_test)
expected = y_test
print("classification report for classifier %s:/n"%(clf,metrics.classification_report predicted))
print("Confusion matrix:/n%s"metrics.confusion_matrix(expected,predicted))