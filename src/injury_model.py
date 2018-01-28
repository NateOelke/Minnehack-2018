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

        self.learning_rate = 0.01
        self.batch_size = 16
        self.epochs = 10

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
        model.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.01))
        return model

    def train_model(self, X, y):
        self.model.fit(X, y, 16, epochs=10, verbose=1)

    def predict(self, X):
        return self.model.predict(X, batch_size=1, verbose=0)

def load_data(data_path):
    # Load classes
    '''
    with open(data_path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        attribute_sets = []
        for row in reader:
            for value in row:
    '''
    return None, None



if __name__ == '__main__':
    X, y = load_data("../data/flavors_of_cacao.csv")
    input_dimensions = X.shape[1]
    output_dimensions = 1

    print("Creating model")
    model = InjuryModel(input_dimensions, output_dimensions)
    print("Training model")
    model.train_model(X, y)
    print("Done")
