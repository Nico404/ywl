from gensim.models import Word2Vec, KeyedVectors
import gensim.downloader as api

import pandas as pd
import numpy as np

from typing import Tuple

from tensorflow import keras
from keras import Model, Sequential, layers, regularizers, optimizers
from keras.callbacks import EarlyStopping


class Models:
    def word2vec_model_100_12_1(self, df : pd.DataFrame, vector_size=100, window=12, min_count=1) -> pd.DataFrame:
        wordtovec = Word2Vec(df['Book'], vector_size=vector_size, window=window, min_count=min_count)
        df['Book'] = df['Book'].apply(lambda x: [wordtovec.wv[word] for word in x if word in wordtovec.wv])
        return df

    def word2vec_model_200_12_2(self, df : pd.DataFrame, vector_size=200, window=12, min_count=2) -> pd.DataFrame:
        wordtovec = Word2Vec(df['Book'], vector_size=vector_size, window=window, min_count=min_count)
        df['Book'] = df['Book'].apply(lambda x: [wordtovec.wv[word] for word in x if word in wordtovec.wv])
        return df

    # word2vec-google-news-300
    # def word2vec_model_pretrained(self, df : pd.DataFrame) -> pd.DataFrame:
    #     return df

    # def glove_model_(self, df : pd.DataFrame) -> pd.DataFrame:
    #     # TBD our version
    #     return df

    # glove-twitter-25
    # def glove_model_pretrained(self, df : pd.DataFrame) -> pd.DataFrame:
    #     return df


############ MODEL 1 ############
############ (base) ############
    def ict_model_RNN_1(X_train, y_train):
        def init_model_1():
            """
            Initialize the Neural Network
            """
            model = Sequential()

            model.add(layers.Masking())

            model.add(layers.LSTM(100, activation='relu'))
            # ou bien  model.add(layers.Dense(100, activation='relu'))

            model.add(layers.Dense(10, activation="softmax"))
            print("Model initialized")
            return model

        def compile_model_1(model: Model, learning_rate=0.0001) -> Model:
            """
            Compile the Neural Network
            """
            optimizer = optimizers.Adam(learning_rate=learning_rate)

            model.compile(loss='categorical_crossentropy',
                        optimizer=optimizer,
                        metrics=['accuracy', "f1score"])
            
            print("Model compiled")
            return model


        def train_model_1(
                model: Model,
                X: np.ndarray,
                y: np.ndarray,
                batch_size=32,
                patience=2,
                validation_data=None, # overrides validation_split
                validation_split=0.3,
                epochs=5
            ) -> Tuple[Model, dict]:
            """
            Fit the model and return a tuple (fitted_model, history)
            """
            print("\nTraining model...")

            es = EarlyStopping(
                monitor="val_loss",
                patience=patience,
                restore_best_weights=True,
                verbose=1
            )

            history = model.fit(
                X,
                y,
                validation_data=validation_data,
                validation_split=validation_split,
                epochs=epochs,
                batch_size=batch_size,
                callbacks=[es],
                verbose=0
            )

            print(history.history.keys())
            print(f"Model trained on {len(X)} rows with min val MAE: {round(np.min(history.history['val_mae']), 2)}")
            return model, history

        def evaluate_model_1(
                model: Model,
                X: np.ndarray,
                y: np.ndarray,
                batch_size=32,
            ) -> Tuple[Model, dict]:
            """
            Evaluate trained model on the dataset
            """
            print(f"\nEvaluating model on {len(X)} rows...")

            metrics = model.evaluate(
                x=X,
                y=y,
                batch_size=batch_size,
                verbose=1,
                # callbacks=None,
                return_dict=True
            )

            loss = metrics["loss"]
            accuracy = metrics['accuracy']
            f1score = metrics['f1score']

            print(f"Model evaluated, Loss:{round(loss, 2)}  Accuracy: {round(accuracy, 2)}, F1Score: {round(f1score, 2)}")

            return metrics

        RNN_1_init = init_model_1()
        RNN_1_comp = compile_model_1(model=RNN_1_init,learning_rate=0.0001)
        RNN_1_train = train_model_1(model=RNN_1_comp, X=X_train, y=y_train)

        return RNN_1_train
