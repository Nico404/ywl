from sklearn.compose import ColumnTransformer
from sklearn.pipeline import FeatureUnion, FunctionTransformer, Pipeline, make_pipeline
import tensorflow as tf
import pandas as pd
from config.config import Config
import os
from src.pipelines.preprocessor import Preprocessor
from src.pipelines.models import Models

config = Config()

#  fit_transform() took 3 minutes and 5 seconds
def build_preprocessor_pipeline_02():
    # Preprocessor custom class with our preprocessing methods
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

    embedder = FunctionTransformer(models.word2vec_model_100_12_1)

    pipeline = make_pipeline(text_author_parallel,
                                 chunk_text_preprocessor_nd,
                                 padding_preprocessor,
                                 embedder)


    return pipeline
