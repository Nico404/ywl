import os

class Config:
    # paths
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_RAW_PATH_GLOBAL = 'data/raw/'
    DATA_RAW_PATH_GLOBAL_FR = 'data/raw/fr/'
    DATA_PROCESSED_PATH = 'data/processed/'
    DATA_FINAL_PATH = 'data/final/'
    LAST_NEXT_TOKEN_PATH = 'data/tmp/last_next_token.txt'
    BOOKS_SHORTLIST_PATH = 'data/raw/books_shortlist/'
    BOOKS_RAW_PATH = 'data/raw/books/'

    # vars
    GUTENDEX_INITIAL_ENDPOINT = 'https://gutendex.com/books?languages=en,fr'
    FR_GUTENDEX_INITIAL_ENDPOINT = 'https://gutendex.com/books?languages=fr'
