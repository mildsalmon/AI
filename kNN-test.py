# -*- coding: utf-8 -*-
# 코드 내부에 한글을 사용가능 하게 해주는 부분입니다.
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = r'C:\Users\user\NanumBarunGothic.ttf'
fontprop = fm.FontProperties(fname=font_path, size=18)

data = [[175, 33, 0],
        [180, 35, 0],
        [160, 27, 1],
        [170, 31, 1]]   # 남 0 / 여 1

test = [[165, 28]]

classes = {0:"남자",
           1:"여자"}

color = ["Green", "Red"]

np_data = np.array(data)

X = np_data[:,0:2]
y = np_data[:,2:]

test_np = np.array(test)

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X, np.ravel(y, order='C'))

y_pred = knn.predict(test_np)

print(classes[y_pred[0]])
print(y_pred[0])

plt.scatter(np_data[ : , :1], np_data[ : ,1:2], c=np_data[ : , 2:])
plt.scatter(test_np[ : , :1], test_np[ : ,1:2], c="blue")

plt.xlabel("키")
plt.ylabel("허리")

plt.show()

