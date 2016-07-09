#!/usr/bin/env python
from sklearn import datasets,metrics
from sklearn.svm import SVC
import numpy as np
iris = datasets.load_iris()

classifier = SVC(gamma=0.001)
classifier.fit(np.array([iris.data[x] for x in range(150) if x/25%2==0]), np.array([iris.target[x] for x in range(150) if x/25%2==0]))

expected = np.array([iris.target[x] for x in range(150) if x/25%2==1])
predicted = classifier.predict(np.array([iris.data[x] for x in range(150) if x/25%2==1]))

print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))

print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))