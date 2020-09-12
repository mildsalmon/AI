import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 가상적인 데이터 생성
X = data = np.linspace(1, 2, 200)
y = X*4 + np.random.randn(200) * 0.3

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(1, input_dim=1, activation='linear'))
model.compile(optimizer='sgd', loss='mse', metrics=['mse'])
model.fit(X, y, batch_size=1, epochs=30)

predict = model.predict(data)

# 첫 번째 그래프는 파란색 마커로
plt.plot(data, predict, 'b', data, y, 'k.')
# 두 번째 그래프는 검정색 점으로 그린다
plt.show()