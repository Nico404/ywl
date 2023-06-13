from sklearn.compose import ColumnTransformer
from sklearn.pipeline import FunctionTransformer, Pipeline, make_pipeline
import tensorflow as tf
from package.ml_logic.preprocessing.preprocessor import Preprocessor

def build_pipeline_GRU():
    # Preprocessor and models custom class with our preprocessing, embeddings and models
    preprocessor = Preprocessor()

    text_pipeline = Pipeline([
        ('body', FunctionTransformer(preprocessor.body_preprocessor)),
        ('clean_special_chars', FunctionTransformer(preprocessor.clean_special_chars)),
        ('del_numbers', FunctionTransformer(preprocessor.del_numbers)),
        ('strip_html', FunctionTransformer(preprocessor.strip_html_preprocessor))
    ])

    author_pipeline = Pipeline([
        ('encoder', FunctionTransformer(preprocessor.inverse_encoding_preprocessor))
    ])

    text_author_parallel = ColumnTransformer([
        ('text_pipeline', text_pipeline, ['Book']),
        ('author_pipeline', author_pipeline, ['Author'])
    ])
     # nd version
    chunking = FunctionTransformer(preprocessor.chunk_text_preprocessor_nd)

    word2vec = FunctionTransformer(preprocessor.word2vec_model_60_12_2)

    padding = FunctionTransformer(preprocessor.padding_sequence_preprocessor)

    pipeline = make_pipeline(text_author_parallel,
                                 chunking,
                                 word2vec,
                                 padding)

    return pipeline
