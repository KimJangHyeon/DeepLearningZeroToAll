from keras.models import Sequential
from keras.layers import Dense
import numpy as np
xy = np.loadtxt('data-01-test-score.csv', delimiter=',')
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

print("x_data", x_data)
print("y_data", y_data)

model = Sequential()
model.add(Dense(input_dim=3, output_dim=1))

model.compile(loss='mse', optimizer='sgd')
model.fit(x_data, y_data, nb_epoch=2000)

print("0, 2, 1", model.predict(np.array([[0, 2, 1]])))
print("0, 9, -1", model.predict(np.array([[0, 9, -1]])))
