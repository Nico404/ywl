from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras import optimizers
from config import Config
from package.ml_logic.models.gru import init_gru
from package.ml_logic.pipelines.pipeline_gru import build_pipeline_GRU
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import datetime
import tensorflow as tf

config = Config()

def preprocess_gru():
    ''' build pipeline, clean, encode and vectorize our data'''
    pipeline = build_pipeline_GRU()
    print('Pipeline loaded')
    data = pd.read_csv(os.path.join(config.DATA_PROCESSED_PATH, 'books_processed_top40.csv'))
    print('books_processed_top40.csv loaded')
    print('Preprocessing data...')
    df_vec = pipeline.fit_transform(data)
    print('Preprocessing DONE')
    print('Saving to file...')
    df_vec.to_csv(os.path.join(config.DATA_FINAL_PATH, 'data_vec.csv'), index=False)
    print('Data saved to data_vec.csv')


def compile_gru():
    ''' compile our model '''
    model = init_gru()
    print('Instanciation of neural network DONE')
    optimizer = optimizers.Adam(learning_rate=0.0001)
    model.compile(loss='categorical_crossentropy',
                  optimizer=optimizer,
                  metrics=['accuracy'])
    print('Compiled GRU model DONE')

    # save the compiled model
    model.save(os.path.join(config.COMPILED_MODELS_PATH, f'gru_model_compiled.h5'))
    print('gru_model_compiled model saved')
    return model


def train_gru():
    ''' train our model on the preprocessed data'''
    # load preprocessed data
    df_vec = pd.read_csv(os.path.join(config.DATA_FINAL_PATH, 'data_vec.csv'))
    print('Data final loaded')

    X = df_vec['Book']
    y = df_vec['Author']

    # One hot encoding the target variable
    enc = OneHotEncoder(handle_unknown='ignore')
    y = enc.fit_transform(np.array(y).reshape(-1, 1)).toarray()
    print('Encoded y')

    # Splitting the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)
    X_train = np.array([np.vstack(x) for x in X_train])
    X_test = np.array([np.vstack(x) for x in X_test])
    print('Test Train Split done')

    es = EarlyStopping(
        monitor="val_accuracy",
        patience=5,
        restore_best_weights=True,
        verbose=1)

    checkpoint = ModelCheckpoint(
        "gru_model.keras", save_weights_only=True, verbose=1)

    model = tf.keras.models.load_model(os.path.join(config.COMPILED_MODELS_PATH, f'gru_model_compiled.keras'))

    history = model.fit(
        X_train,
        y_train,
        validation_split=0.2,
        epochs=300,
        batch_size=32,
        callbacks=[es, checkpoint],
        verbose=1)
    print(history.history.keys())

    # save the trained model
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    tf.keras.models.save_model(model, os.path.join(config.TRAINED_MODELS_PATH, f'gru_model_{timestamp}.keras'))
    print('Trained model saved')
    return history


# def predict_gru():
    # model = tf.keras.models.load_model(os.path.join(config.TRAINED_MODELS_PATH, f'gru_model_TIMESTAMP.keras'))
    #prediction = model.predict
    # return prediction


if __name__ == '__main__':
    # preprocess_gru()
    # compile_gru()
    # train_gru()
    # predict_gru()
    pass
