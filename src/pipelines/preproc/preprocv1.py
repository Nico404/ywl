# from sklearn.compose import ColumnTransformer
# from sklearn.pipeline import FeatureUnion, FunctionTransformer, Pipeline
# from preprocessor import Preprocessor
# from keras.utils import to_categorical

# # Create the preprocessor pipeline
# text_pipeline = FeatureUnion([
#     ('body', FunctionTransformer(Preprocessor().body_preprocessor)),
#     ('clean_body', FunctionTransformer(Preprocessor().clean_body_preprocessor)),
#     ('chunk_text', FunctionTransformer(Preprocessor().chunk_text_preprocessor)),
#     ('tokenizer', FunctionTransformer(Preprocessor().tokenizer_preprocessor)),
#     ('embedder', FunctionTransformer(Preprocessor().word2vec_preprocessor))
# ])

# author_pipeline = Pipeline([
#     ('encoder', FunctionTransformer(lambda X: to_categorical(X, num_classes=10)))
# ])

# preprocessor = ColumnTransformer([
#     ('text_transformer', text_pipeline, ['X']),
#     ('author_transformer', author_pipeline, ['y'])
# ])

# # Apply the preprocessing steps on the dataframe
# preprocessed_data = preprocessor.fit_transform(df)
