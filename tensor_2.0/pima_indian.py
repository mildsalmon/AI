import pandas as pd

df = pd.read_csv('./deeplearning/dataset/pima-indians-diabetes.csv',
                 names=["pregnant", "plasma", "pressure", "thickness",
                        "insulin", "BMI", "pedigree", "age", "class"])

print(df.head(5))
print(df.info())
print(df.describe())
print(df[['pregnant', 'class']])

print(df[['pregnant', 'class']].
      groupby(['pregnant'], as_index=False).
      mean().
      sort_values(by='pregnant', ascending=True))
#
import matplotlib.pyplot as plt
import seaborn as sns
#
plt.figure(figsize=(12, 12))
sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap=plt.cm.gist_heat, linecolor='white', annot=True)
plt.show()

grid = sns.FacetGrid(df, col='class')
grid.map(plt.hist, 'plasma', bins=10)
plt.show()

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import tensorflow as tf

# seed 값 생성
np.random.seed(3)
tf.random.set_seed(3)

# 데이터 로드
dataset = np.loadtxt('./deeplearning/dataset/pima-indians-diabetes.csv', delimiter=",")
X = dataset[:, 0:8]
Y = dataset[:, 8]

# print("X: ", X)
# print("Y: ", Y)

# 모델의 설정
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 모델 컴파일
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# 모델 실행
model.fit(X, Y, epochs=200, batch_size=10)

# 결과 실행
# print("\nAccuracy: {0:.4f}".format())
print(model.evaluate(X, Y))
# # print("\nAccuracy: {0:.4f}".format(model.evaluate(X, Y)[2]))
# print("\nAccuracy: {0:.4f}".format(model.evaluate(X, Y)[50]))
# print("\nAccuracy: {0:.4f}".format(model.evaluate(X, Y)[767]))
# for i in range(1, 767):
#     print("\nAccuracy: {0:.4f}".format(model.evaluate(X, Y)[i]))