from sklearn.compose import ColumnTransformer
from sklearn.pipeline import FeatureUnion, FunctionTransformer, Pipeline, make_pipeline
import tensorflow as tf
import pandas as pd
from config.config import Config
import os
from src.pipelines.preprocessor import Preprocessor
from src.pipelines.models import Models

config = Config()

def build_preprocessor_pipeline_06():
    # Preprocessor and models custom class with our preprocessing, embeddings and models
    models = Models()

    ict_model_RNN_1 = FunctionTransformer(models.ict_model_RNN_1)

    pipeline = make_pipeline(ict_model_RNN_1)

    return pipeline
