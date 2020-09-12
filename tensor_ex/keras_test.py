from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow import keras

model = Sequential()
model.add(Dense(units=64, activation='sigmoid', input_dim=100))
model.add(Dense(units=10, activation='sigmoid'))

model.compile(loss='mse', optimizer = 'sgd', metrics = ['accuracy'])

model.compile(loss='mse', optimizer = keras.optimizers.SGD(lr=0.01, momentum=0.9))

model.fit(X, y, epochs=5, batch_size=32)

loss_and_metrics = model.evaluate(X, y, batch_size=128)

classes =model.predict(new_X, batch_size=128)