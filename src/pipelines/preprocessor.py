import pandas as pd
from keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
from src.utils.cleaning import body, body_cleaning, strip_html
from src.utils.chunkify import chunk_text
from config.config import Config
import numpy as np


config = Config()

class Preprocessor:
## Preprocessing methods ##
    def body_preprocessor(self, df):
        ''' Extracts the body of a text without the header and the footer by gutenberg project '''
        df['Book'] = df['Book'].apply(body)
        return df

    def clean_body_preprocessor(self, df):
        ''' Cleans the body of a text by removing whitespaces, lowercasing, removing numbers and/or punctuation '''
        df['Book'] = df['Book'].apply(body_cleaning)
        return df

    def strip_html_preprocessor(self, df):
        ''' Removes html tags from a string '''
        df['Book'] = df['Book'].apply(strip_html)
        return df

    def chunk_text_preprocessor(self, df):
        ''' Chunks the text into 256 word parts
        ! NOT for pipeline use only !
        '''
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

    def chunk_text_preprocessor_nd(self, array: np.ndarray) -> pd.DataFrame:
        ''' Chunks the text into 256 word parts
        ! for pipeline use only !
        '''
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

    def padding_preprocessor(self, df): # normalement pas besoin, et du coup pas de masking
        ''' Pads the chunks right to have the same length for each chunk '''
        df['Book'] = df['Book'].str.ljust(256, '0')
        return df


    def encode_label_preprocessor(self, df):
        ''' Encodes the target variable into integers'''
        le = LabelEncoder()
        le.fit(df['Author'])
        df['Author'] = le.transform(df['Author'])
        return df

    def encode_categorical_preprocessor(self, df):
        ''' Encodes the target variable into integers then to categorical to get rid of potential weights in the integers ranks '''
        le = LabelEncoder()
        le.fit(df['Author'])
        df['Author'] = le.transform(df['Author'])
        df['Author'] = to_categorical(df['Author'], num_classes=10)
        return df
