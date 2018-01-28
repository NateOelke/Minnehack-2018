import csv
import numpy as np
from collections import deque
from keras.layers import Dense
from keras.optimizers import Adam
from keras.models import Sequential

class InjuryModel:
    def __init__(self, input_dimensions, output_dimensions):
        self.input_dimensions = input_dimensions
        self.output_dimensions = output_dimensions

        self.learning_rate = 0.005
        self.batch_size = 16
        self.epochs = 15

        self.model = self.create_model()

    def create_model(self):
        # data should be 2d numpy array
        model = Sequential()
        model.add(Dense(30, input_dim=self.input_dimensions, activation='relu',
                            kernel_initializer='he_uniform'))
        model.add(Dense(15, activation='relu',
                            kernel_initializer='he_uniform'))
        model.add(Dense(self.output_dimensions, activation='linear',
                            kernel_initializer='he_uniform'))
        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))
        return model

    def train_model(self, X, y):
        self.model.fit(X, y, validation_split=0.33, batch_size=16, epochs=self.epochs, verbose=1)

    def predict(self, X):
        newX = np.reshape(X, (1, self.input_dimensions))
        return self.model.predict(newX, batch_size=1, verbose=0)

def load_data(data_path):
    # Column 34 is start of output values
    data = np.loadtxt(data_path, delimiter=",")
    X = data[:, 0:33]
    y = data[:, -1]
    return X, y

if __name__ == '__main__':
    X, y = load_data("../data/exampledata.csv")
    input_dimensions = X.shape[1]
    output_dimensions = 1

    print("\nInput dim: " + str(input_dimensions))
    print("Output dim: " + str(output_dimensions))

    model = InjuryModel(input_dimensions, output_dimensions)
    model.train_model(X, y)
    #print("\n")
    #print(X[2])
    #print(model.predict(X[0]))
