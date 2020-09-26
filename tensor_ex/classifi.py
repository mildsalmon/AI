import tensorflow.compat.v1 as tf
import numpy as np

data = np.loadtxt('./data.csv', delimiter=',', unpack=True, dtype='float32')

x_data = np.reanspose(data[0:2])
y_data = np.transpose(data[2:])

global_step