import numpy as np

fake_a_b = [3, 76]

data = [[2, 81], [4, 93], [6, 91], [8, 97]]

x = [i[0] for i in data]
y = [i[1] for i in data]

def predict(x):
    return fake_a_b[0]*x + fake_a_b[1]

def mse(y, y_hat):
    return ((y-y_hat) ** 2).mean()

def mse_val(y, predict_result):
    return mse(np.array(y), np.array(predict_result))

predict_result = []

for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print("공부시간={0}, 실제 점수={1}, 예측 점수={2}".format(x[i], y[i], predict(x[i])))

print("mse 최종값: " + str(mse_val(predict_result, y)))