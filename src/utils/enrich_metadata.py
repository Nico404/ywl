import os
from config.config import Config

def count_words(id):
    ''' Count words in the book '''
    config = Config()
    file_path = os.path.join(config.PROJECT_ROOT, config.DATA_RAW_PATH_GLOBAL, 'books', f'{id}.txt')
    # first check if file exists
    if not os.path.isfile(file_path):
        return None
    # if it exists, count words
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

def count_chars(id):
    ''' Count chars in the book '''
    # first check if file exists
    config = Config()
    file_path = os.path.join(config.PROJECT_ROOT, config.DATA_RAW_PATH_GLOBAL, 'books', f'{id}.txt')
    if not os.path.isfile(file_path):
        return None
    # if it exists, count chars
    with open(file_path, 'r') as file:
        text = file.read()
        chars = list(text)
        return len(chars)
