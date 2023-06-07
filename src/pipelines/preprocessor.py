import pandas as pd
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer
import tensorflow as tf
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec
from keras.utils import to_categorical

# Read the dataframe
df = pd.read_csv('df_final.csv')

# Define preprocessing methods

class Preprocessor:
## Preprocessing methods ##
    def body_preprocessor(self, X):
        # Apply preprocessing operations on text
        # Example: cleaning, normalization, etc.
        return X

    def clean_body_preprocessor(self, X):
        # Apply cleaning operations on text
        return X

    def encode_categorical(self, X):
        # Apply encoding operations on target
        return X

    def encode_label(self, X):
    # Apply encoding operations on target
        return X

    def chunk_text_preprocessor(self, X):
    # Apply chunking operations on text
        return X

    def padding_preprocessor(self, X):
    # Apply padding operations on text
        return X

## Tokenization methods ##
    def nltk_preprocessor(self, X):
    # Apply tokenization operations on text
        return X

    def text_to_sequence_preprocessor(self, X):
    # Apply tokenization operations on text
        return X


    def ngrams_preprocessor(self, X):
    # Apply tokenization operations on text
        return X

## Embedding methods ##
    def word2vec_preprocessor(self, X):
        # Apply Word2Vec operations on tokenized text
        return X

    def glove_preprocessor(self, X):
        # Apply GloVe operations on tokenized text
        return X
