from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
#
# print(iris.data)
#
# print(iris.feature_names)
#
# print(iris.target)

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)

print(X_train.shape)
print(X_test.shape)

from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

knn = KNeighborsClassifier(n_neighbors=50)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
score = metrics.accuracy_score(y_test, y_pred)

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X, y)

classes = {0:'setosa', 1:'versicolor', 2:'virginica'}

x_new = [[3, 4, 5, 2],
         [5, 4, 2, 2]]
y_predict = knn.predict(x_new)

print(classes[y_predict[0]])
print(classes[y_predict[1]])