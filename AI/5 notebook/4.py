import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import classification_report, confusion_matrix

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
target = [0, 0, 0, 1, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    target,
    test_size= 0.6
)

classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

tree.plot_tree(classifier)

y_pred = classifier.predict(X_test)

print(y_test)
print(y_pred)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
