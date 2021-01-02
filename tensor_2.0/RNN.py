from keras.datasets import reuters
import numpy

(X_train, Y_train), (X_test, Y_test) = reuters.load_data(num_words=1000, test_split=0.2)


category = numpy.max(Y_train) + 1
print((Y_train.size))
print(type(Y_train))
# print(len(X_train))
#
# for i in Y_train:
#     print(i)

from keras.preprocessing import sequence

x_train = sequence.pad_sequences(X_train, maxlen=100)
x_test = sequence.pad_sequences(X_test, maxlen=100)

from keras.utils import np_utils
y_train = np_utils.to_categorical(Y_train)
y_test = np_utils.to_categorical(Y_test)

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding

model = Sequential()
model.add(Embedding(1000, 100))
model.add(LSTM(100, activation='tanh'))
model.add(Dense(46, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

history = model.fit(x_train, y_train, batch_size=100, epochs=20, validation_data=(x_test, y_test))

print("\n Test Accuracy: ")
print((model.evaluate(x_test, y_test)))