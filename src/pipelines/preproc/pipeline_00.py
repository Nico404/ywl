from sklearn.compose import ColumnTransformer
from sklearn.pipeline import FeatureUnion, FunctionTransformer, Pipeline, make_pipeline
import tensorflow as tf
import pandas as pd
from config.config import Config
import os
from src.pipelines.preprocessor import Preprocessor

config = Config()

def build_preprocessor_pipeline_00():
    # Preprocessor custom class with our preprocessing methods
    preprocessor = Preprocessor()

    text_pipeline = Pipeline([
        ('body', FunctionTransformer(preprocessor.body_preprocessor)),
        ('clean_body', FunctionTransformer(preprocessor.clean_body_preprocessor))
    ])

    author_pipeline = Pipeline([
        ('encoder_label', FunctionTransformer(preprocessor.encode_label_preprocessor))
    ])

    text_author_parallel = ColumnTransformer([
        ('text_pipeline', text_pipeline, ['Book']),
        ('author_pipeline', author_pipeline, ['Author'])
    ])

    preprocessor = make_pipeline(text_author_parallel, FunctionTransformer(preprocessor.chunk_text_preprocessor_nd))

    return preprocessor