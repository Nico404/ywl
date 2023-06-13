import pandas as pd
from package.ml_logic.preprocessing.utils import strip_html, clean_special_chars, del_numbers, chunk_text, body
import numpy as np

from sklearn.preprocessing import LabelEncoder
from keras.preprocessing.text import text_to_word_sequence
from keras.preprocessing.sequence import pad_sequences

from gensim.models import Word2Vec

import tensorflow as tf
from tensorflow import keras


from config import Config


config = Config()

class Preprocessor:
## Preprocessing methods ##
    def body_preprocessor(self, df):
        ''' Extracts the body of a text without the header and the footer by gutenberg project '''
        df['Book'] = df['Book'].apply(body)
        return df

    def strip_html_preprocessor(self, df):
        ''' Removes html tags from a string '''
        df['Book'] = df['Book'].apply(strip_html)
        return df

    def clean_special_chars(self, df):
        ''' Removes special chars from a string '''
        df['Book'] = df['Book'].apply(clean_special_chars)
        return df

    def del_numbers(self, df):
        ''' Removes numbers from string '''
        df['Book'] = df['Book'].apply(del_numbers)
        return df

    def chunk_text_preprocessor_nd(self, array: np.ndarray) -> pd.DataFrame:
        ''' Chunks the text into 256 word parts
        ! for pipeline use only !
        '''
        df = pd.DataFrame(array, columns=['Book', 'Author', 'Encoder'])
        new_rows = list()
        for _, row in df.iterrows():
            chunks = chunk_text(row['Book'])  # Get the chunks for the current row
            for chunk in chunks:
                new_row = {'Encoder': row['Encoder'],
                    'Author': row['Author'],
                    'Book': chunk
                }
                new_rows.append(new_row)
        new_df = pd.DataFrame(new_rows)

        # store the number of samples we want based on the author with the least number of chunks
        min_samples = new_df.groupby('Author').count().min()[0]
        print(f'Number of samples per author: {min_samples}')
        # For each author in df_chunks, to keep a balanced dataset we sample on the author with the least number of chunks
        new_df = new_df.groupby('Author').apply(lambda x: x.sample(n=min_samples, random_state=42)).reset_index(drop=True)
        return new_df


    def padding_sequence_preprocessor(self, df):
        ''' Pads the vect chunks right to have the same length of 256 vectors for each chunk '''
        df['Book'] = pad_sequences(df['Book'], dtype='float32', maxlen=256, padding='post', truncating='post').tolist()
        return df

    def encode_label_preprocessor(self, df):
        ''' Encodes the target variable into integers'''
        le = LabelEncoder()
        le.fit(df['Author'])
        df['Author'] = le.transform(df['Author'])
        return df

    def inverse_encoding_preprocessor(self, df):
        ''' Encodes the target variable into integers'''
        target = df['Author']
        le = LabelEncoder()
        authors_encoded=le.fit_transform(target)
        print(f"Label encoder has encoded authors into {le.classes_}")
        authors_encoded_df = pd.DataFrame({'author_name': le.inverse_transform(authors_encoded),
                                           'encoded_authors': authors_encoded})
        return authors_encoded_df


    def word2vec_model_60_12_2(self, df : pd.DataFrame, vector_size=60, window=12, min_count=1) -> pd.DataFrame:
        ''' Creates a word2vec embedding from the text and returns the dataframe with vectors instead of text '''
        df['Book'] = df['Book'].apply(lambda x: text_to_word_sequence(x))
        wordtovec = Word2Vec(df['Book'], vector_size=vector_size, window=window, min_count=min_count)
        df['Book'] = df['Book'].apply(lambda x: [wordtovec.wv[word] for word in x if word in wordtovec.wv])
        return df


    def authors_to_dic(self, df):
        ''' Returns a dictionary with author_names and their corresponding encoding int'''
        target = df['Author']
        le = LabelEncoder()
