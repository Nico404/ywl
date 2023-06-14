import os

class Config:
    # paths
    LAST_NEXT_TOKEN_PATH = 'fetch_data/checkpoint/last_next_token.txt'
    DATA_RAW_PATH_GLOBAL = 'data/raw/'
    DATA_PROCESSED_PATH = 'data/processed/'
    DATA_FINAL_PATH = 'data/final/'

    BOOKS_RAW_PATH = 'data/raw/books/'
    BOOKS_SHORTLIST_PATH = 'data/raw/books_shortlist/'
    BOOKS_TOP40_PATH = 'data/raw/books_top40/'

    TRAINED_MODELS_PATH = 'data/trained_models/'
    COMPILED_MODELS_PATH = 'data/compiled_models/'

    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_RAW_PATH_GLOBAL = 'data/raw/'
