import matplotlib.pylab as plt
from sklearn import linear_model

# 선형 회귀 모델을 생성한다
reg = linear_model.LinearRegression()

# 데이터는 파이썬의 리스트, 넘파이의 배열로 만들어도 된다
# 2차원 배열로 만들어야 한다
X = [[0], [1], [2]]
# y=x+3
y = [3, 3.5, 5.5]

# 학습을 시킨다
reg.fit(X,y)

print(reg.coef_)

print(reg.intercept_)

print(reg.score(X, y))

print(reg.predict([[5]]))

plt.scatter(X, y, color='black')
y_pred = reg.predict(X)
plt.plot(X, y_pred, color='blue', linewidth=3)
plt.show()