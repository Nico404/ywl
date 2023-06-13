import tensorflow as tf
from tensorflow import keras
from keras import regularizers, Input, Sequential, layers, optimizers
from keras.layers import Dropout, Dense


def init_gru():
    model = Sequential()

    model.add(Input(shape=(None, 40)))
    model.add(layers.Masking())

    model.add(layers.GRU(240, activation='relu'))
    model.add(Dropout(0.1))
    model.add(layers.Dense(120, activation='relu'))
    model.add(Dropout(0.1))

    model.add(layers.Dense(40, activation='softmax'))
    return model
