from sklearn.compose import ColumnTransformer
from sklearn.pipeline import FeatureUnion, FunctionTransformer, Pipeline, make_pipeline
import tensorflow as tf
import pandas as pd
from config.config import Config
import os
from src.pipelines.preprocessor import Preprocessor
from src.pipelines.models import Models

config = Config()

#     return pipeline
def build_preprocessor_pipeline_03():
    # Preprocessor and models custom class with our preprocessing, embeddings and models
    preprocessor = Preprocessor()
    models = Models()

    text_pipeline = Pipeline([
        ('body', FunctionTransformer(preprocessor.body_preprocessor)),
        ('clean_body', FunctionTransformer(preprocessor.clean_body_preprocessor)),
        ('strip_html', FunctionTransformer(preprocessor.strip_html_preprocessor))
    ])

    author_pipeline = Pipeline([
        ('encoder_categorical', FunctionTransformer(preprocessor.encode_label_preprocessor))
    ])

    text_author_parallel = ColumnTransformer([
        ('text_pipeline', text_pipeline, ['Book']),
        ('author_pipeline', author_pipeline, ['Author'])
    ])
     # nd version
    chunk_text_preprocessor_nd = FunctionTransformer(preprocessor.chunk_text_preprocessor_nd)

    padding_preprocessor = FunctionTransformer(preprocessor.padding_preprocessor)

    word2vec_model_60_12_2 = FunctionTransformer(models.word2vec_model_60_12_2)

    pipeline = make_pipeline(text_author_parallel,
                                 chunk_text_preprocessor_nd,
                                 padding_preprocessor,
                                 word2vec_model_60_12_2)

    return pipeline
