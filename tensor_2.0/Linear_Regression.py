import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = [[2,81], [4,93], [6,91], [8,97]]
x = [i[0] for i in data]
y = [i[1] for i in data]

plt.figure(figsize=(8,5))
plt.scatter(x, y)
plt.show()

x_data = np.array(x)
y_data = np.array(y)

a = 0
b = 0

lr = 0.03
epochs = 2001

for i in range(epochs):
    y_pred = a * x_data + b
    error = y_data - y_pred
    a_diff = -(2/len(x_data)) * sum(x_data * (error))
    b_diff = -(2/len(x_data))* sum(error)

    a = a - lr * a_diff
    b = b - lr * b_diff

    if i % 100 == 0:
        print("epoch={0}, 기울기={1}, 절편={2}".format(i, a, b))

y_pred = a * x_data + b
plt.scatter(x,y)
plt.plot([min(x_data), max(x_data)], [min(y_pred), max(y_pred)])
plt.show()