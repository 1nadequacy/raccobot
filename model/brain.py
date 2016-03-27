import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
import random
import re


def build_nn(input_shape, num_outputs):
    """Simple deep LSTM."""
    model = Sequential()
    model.add(LSTM(512, return_sequences=True, input_shape=input_shape))
    model.add(Dropout(0.2))
    model.add(LSTM(512, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(num_outputs))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
    return model


def save_model(model, model_name):
    """Saved model's arch and weights."""
    with open('%s.json' % model_name, 'w') as f:
        f.write(model.to_json())
    model.save_weights('%s.h5' % model_name, overwrite=True)


def load_model(model_name):
    """Loads model's arch and weights by name."""
    with open('%s.json' % model_name, 'r') as f:
        model = model_from_json(f.read())
    model.load_weights('%s.h5' % model_name)
    return model
