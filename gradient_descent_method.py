import numpy as np
import matplotlib.pyplot as plt

X = np.array([0.0, 1.0, 2.0])
y = np.array([3.0, 3.5, 5.5])

# 기울기
# 절편
# 학습률
# 반복 횟수
W = 0
b = 0
lrate = 0.01
epochs = 1000

# 입력 데이터의 개수
n = float(len(X))

# 경사 하강법
for i in range(epochs):
    # 예측값
    y_pred = W*X + b
    dW = (2/n) * sum(X*(y_pred-y))
    db = (2/n) * sum(y_pred-y)
    # 기울기 수정
    # 절편 수정
    W = W - lrate * dW
    b = b - lrate * db

# 기울기와 절편을 출력한다
print(W, b)

# 예측값을 만든다
y_pred = W*X + b

# 입력 데이터를 그래프 상에 찍는다
plt.scatter(X, y)

# 예측값은 선그래프로 그린다
plt.plot([min(X), max(X)], [min(y_pred), max(y_pred)], color='red')
plt.show()