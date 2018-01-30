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

        self.learning_rate = 0.003
        self.batch_size = 16
        self.epochs = 20

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
        self.model.fit(X, y, validation_split=0.33, batch_size=self.batch_size, \
            epochs=self.epochs, verbose=1)

    def predict(self, X):
        print(X.ndim)
        if X.ndim == 2:
            return self.model.predict(X, verbose=0)
        elif X.ndim == 1:
            newX = np.array([X])
            return self.model.predict(newX, verbose=0)[0]
        else:
            return None

def load_data(data_path):
    data = np.loadtxt(data_path, delimiter=",")
    X = data[:, 0:-1]
    y = data[:, -1]
    return X, y

if __name__ == '__main__':
    X, y = load_data("../data/exampledata.csv")
    X_val, y_val = load_data("../data/exampledata_val.csv")
    input_dimensions = X.shape[1]
    output_dimensions = 1

    model = InjuryModel(input_dimensions, output_dimensions)
    model.train_model(X, y)

    #test_predictions = model.predict(X_val)
    #with open("../data/exampledata_val_predictions.csv", "w") as output:
    #    output.write(np.array_str(test_predictions))
