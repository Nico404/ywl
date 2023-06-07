import pandas as pd
from keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
from src.utils.cleaning import body, body_cleaning
from src.utils.chunkify import chunk_text
from config.config import Config
import numpy as np


config = Config()

class Preprocessor:
## Preprocessing methods ##
    def body_preprocessor(self, df):
        df['Book'] = df['Book'].apply(body)
        return df

    def clean_body_preprocessor(self, df):
        df['Book'] = df['Book'].apply(body_cleaning)
        return df

    def chunk_text_preprocessor(self, df):
        new_rows = list()
        for index, row in df.iterrows():
            chunks = chunk_text(row['Book'])  # Get the chunks for the current row
            for chunk in chunks:
                new_row = {
                    'Author': row['Author'],
                    'Book': chunk
                }
                new_rows.append(new_row)
        new_df = pd.DataFrame(new_rows)
        return new_df

    def chunk_text_preprocessor_nd(self, array: np.ndarray):
        # for pipeline use only
        df = pd.DataFrame(array, columns=['Book', 'Author'])
        new_rows = list()
        for index, row in df.iterrows():
            chunks = chunk_text(row['Book'])  # Get the chunks for the current row
            for chunk in chunks:
                new_row = {
                    'Author': row['Author'],
                    'Book': chunk
                }
                new_rows.append(new_row)
        new_df = pd.DataFrame(new_rows)
        return new_df


    def encode_label_preprocessor(self, df):
        le = LabelEncoder()
        le.fit(df['Author'])
        df['Author'] = le.transform(df['Author'])
        return df

    def encode_categorical_preprocessor(self, df):
        # first label encode the target variable so we have integers to categorize
        le = LabelEncoder()
        le.fit(df['Author'])
        df['Author'] = le.transform(df['Author'])
        df['Author'] = to_categorical(df['Author'], num_classes=10)
        return df

    # def padding_preprocessor(self, df): # normalement pas besoin, et du coup pas de masking
    #     return df

# ## Embedding methods ##
#     def word2vec_preprocessor(self, df):
#         df['Book'] = df['Book'].apply(lambda x: Word2Vec(x, vector_size=10))
#         return df

#         # def glove_preprocessor(self, X):
#         #     return X
