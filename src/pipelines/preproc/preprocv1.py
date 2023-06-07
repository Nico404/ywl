from sklearn.compose import ColumnTransformer
from sklearn.pipeline import FeatureUnion, FunctionTransformer, Pipeline
import tensorflow as tf
import pandas as pd
from config.config import Config
import os
from src.pipelines.preprocessor import Preprocessor

config = Config()
preprocessor = Preprocessor()

def build_preprocessor_pipeline():
    # Create the preprocessor pipeline
    text_pipeline = Pipeline([
        ('body', Preprocessor().body_preprocessor),
        ('clean_body', Preprocessor().clean_body_preprocessor),
        ('chunk_text', Preprocessor().chunk_text_preprocessor)
    ])

    author_pipeline = Pipeline([
        ('encoder', Preprocessor().encode_label_preprocessor),
    ])

    preprocessor = ColumnTransformer([
        ('text_transformer', text_pipeline, ['Book']),
        ('author_transformer', author_pipeline, ['Author'])
    ])

    return preprocessor
